import asyncio
import json
from typing import Optional, Dict
from core.logger import Logger
from halo import Halo
from service.scan import Scan
from service.report import Report
from formatter.reports import ReportsFormatter


class ScanFlow:
    """Scanning flow"""

    def __init__(self):
        self.logger = Logger()
        self.scanner = Scan()
        self.report = Report()
        self.formatter = ReportsFormatter()


    async def run(
        self,
        file: Optional[str],
        link: Optional[str],
        desc: str,
        tags: str,
        prop_tags: bool,
        password: str,
        is_private: bool
    ):
        """Upload a file or link and receive its report"""

        scan_id = await self.__upload(file, link, desc, tags, prop_tags,password, is_private)

        self.logger.success(f'Flow ID: {scan_id}')
        
        reports = await self.__get_scan_reports(scan_id)
        self.logger.debug(self.formatter.format(reports))


    async def __upload(
        self,
        file: Optional[str],
        link: Optional[str],
        desc: str,
        tags: str,
        prop_tags: bool,
        password: str,
        is_private: bool
    ) -> str:

        spinner = Halo(text=f'Uploading a file {file} ... ', spinner='dots', placement='right')
        spinner.start()

        response = await self.scanner.upload(file, link, desc, tags, prop_tags,password, is_private)

        if 'flow_id' not in response:
            self.logger.warning('Invalid response')
            spinner.fail()
            return None

        spinner.succeed()

        return response['flow_id']


    async def __get_scan_reports(self, scan_id: str) -> Dict:
        """Get reports related to scan"""

        spinners: Dict[str, Halo] = {}
        spinners['main'] = Halo(text=f'Fetching reports ... ', placement='right')
        spinners['main'].start()

        while True:
            await asyncio.sleep(1)
            
            scan_report = await self.report.get_scan_reports(scan_id)

            if 'reports' not in scan_report or not scan_report['reports']:
                continue

            reports: Dict = scan_report['reports']
            report_ids = reports.keys()
            for id in report_ids:
                if id not in spinners:
                    spinners[id] = Halo(text=f'Report {id} ', placement='right')
                    spinners[id].start()

                report = reports[id]
                if 'overallState' not in report:
                    continue
                if report['overallState'] == 'success':
                    spinners[id].succeed()
                elif report['overallState'] == 'failed':
                    spinners[id].fail()

            if 'allFinished' in scan_report and scan_report['allFinished']:
                break


        if 'reports' in scan_report:
            spinners['main'].succeed()
            return scan_report['reports']
        else:
            spinners['main'].fail()
            return None
