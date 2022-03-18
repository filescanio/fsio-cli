import asyncio
from halo import Halo
from filescan_cli.core.logger import Logger
from filescan_cli.service.scan import Scan
from filescan_cli.service.report import Report
from filescan_cli.formatter.reports import ReportsFormatter


class ScanFlow:
    """Scanning flow"""

    def __init__(self):
        self.logger = Logger()
        self.scanner = Scan()
        self.report = Report()
        self.formatter = ReportsFormatter()


    async def run(
        self,
        file,
        link,
        desc,
        tags,
        prop_tags,
        password,
        is_private
    ):
        """Upload a file or link and receive its report"""

        scan_id = await self.__upload(file, link, desc, tags, prop_tags,password, is_private)

        self.logger.success(f'Flow ID: {scan_id}')
        
        reports = await self.__get_scan_reports(scan_id)
        self.logger.debug(self.formatter.format(reports))


    async def __upload(self, file, link, desc, tags, prop_tags, password, is_private):

        spinner = Halo(text=f'Uploading a file {file} ... ', spinner='dots', placement='right')
        spinner.start()

        result = await self.scanner.upload(file, link, desc, tags, prop_tags,password, is_private)

        if 'error' in result:
            spinner.fail(result['error'])
            return

        response = result['content']
        if 'flow_id' not in response:
            spinner.fail('Invalid response')
            return

        spinner.succeed()

        return response['flow_id']


    async def __get_scan_reports(self, scan_id):
        """Get reports related to scan"""

        spinners = {}
        spinners['main'] = Halo(text=f'Fetching reports ... ', placement='right')
        spinners['main'].start()

        while True:
            await asyncio.sleep(1)

            result = await self.report.get_scan_reports(scan_id)
            if 'error' in result:
                spinners['main'].fail(result['error'])
                return

            scan_report = result['content']
            if 'reports' not in scan_report or not scan_report['reports']:
                continue

            reports = scan_report['reports']
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
            result = []
            for id in scan_report['reports']:
                report = scan_report['reports'][id]
                report['id'] = id
                result.append(report)
            return result
        else:
            spinners['main'].fail()
            return None
