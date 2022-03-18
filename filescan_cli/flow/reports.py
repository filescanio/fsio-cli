from typing import List, Dict, Tuple
from halo import Halo
from filescan_cli.core.logger import Logger
from filescan_cli.service.report import Report
from filescan_cli.formatter.reports import ReportsFormatter


class ReportsFlow:

    def __init__(self):
        self.report = Report()
        self.logger = Logger()
        self.formatter = ReportsFormatter()


    async def get_scan_reports(self, scan_id, filters, sorts, graph):

        spinner = Halo(text=f'Fetching reports ... ', placement='right')
        spinner.start()

        result = await self.report.get_scan_reports(scan_id, filters, sorts, graph)

        if 'error' in reports:
            spinner.fail(result['error'])
            return

        scan_report = result['content']
        if 'allFinished' in scan_report and not scan_report['allFinished']:
            spinner.warn('Not finished yet')
            return

        if 'reports' not in scan_report or not scan_report['reports']:
            spinner.fail('No data')
            return

        reports = scan_report['reports']
        spinner.succeed()

        self.__view_reports(reports)


    async def get_reports(self, page, size):

        spinner = Halo(text=f'Fetching reports ... ', placement='right')
        spinner.start()

        reports = await self.report.get_reports(page, size)

        if 'error' in reports:
            spinner.fail(reports['error'])
            return
        else:
            spinner.succeed()

        self.__view_reports(reports['content'])


    async def search(self, params):

        spinner = Halo(text=f'Searching reports ... ', placement='right')
        spinner.start()

        reports = await self.report.search_reports(params)

        if 'error' in reports:
            spinner.fail(reports['error'])
            return
        else:
            spinner.succeed()

        self.__view_reports(reports['content'], total=reports['total'])


    def __view_reports(self, reports: List, total=-1):
        """View reports"""

        self.logger.debug(self.formatter.format(reports, total))
