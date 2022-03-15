from typing import List, Dict, Tuple
from core.logger import Logger
from halo import Halo
from service.report import Report
from formatter.reports import ReportsFormatter
import json


class ReportsFlow:

    def __init__(self):
        self.report = Report()
        self.logger = Logger()
        self.formatter = ReportsFormatter()


    async def get_scan_reports(self, scan_id: str, filters: Tuple, sorts: Tuple, graph: bool) -> Dict:

        spinner = Halo(text=f'Fetching reports ... ', placement='right')
        spinner.start()

        scan_report = await self.report.get_scan_reports(scan_id, filters, sorts, graph)

        if 'allFinished' in scan_report and not scan_report['allFinished']:
            spinner.warn('Not finished yet')
            return

        if 'reports' not in scan_report or not scan_report['reports']:
            spinner.fail('No data')
            return

        reports: Dict = scan_report['reports']
        spinner.succeed()

        self.__view_reports(reports)


    async def get_reports(self, page: int, size: int) -> List:

        spinner = Halo(text=f'Fetching reports ... ', placement='right')
        spinner.start()

        reports = await self.report.get_reports(page, size)

        if not reports:
            spinner.fail()
            return
        else:
            spinner.succeed()

        self.__view_reports(reports)


    async def search(self, params: Dict[str, str]) -> List:

        spinner = Halo(text=f'Searching reports ... ', placement='right')
        spinner.start()

        reports = await self.report.search_reports(params)

        if reports is None:
            spinner.fail()
        else:
            spinner.succeed()

        if not reports:
            return

        self.__view_reports(reports)


    def __view_reports(self, reports: List):
        """View reports"""

        self.logger.debug(self.formatter.format(reports))
