import aiofiles
import colorama
from typing import Dict, Tuple
from core.logger import Logger
from halo import Halo
from formatter.report import ReportFormatter
from service.report import Report

class ReportFlow:

    def __init__(self):
        self.report = Report()
        self.logger = Logger()
        self.formatter = ReportFormatter()


    async def get_report(self, id: str, hash: str, filters: Tuple, sorts: Tuple, graph: bool) -> Dict:

        spinner = Halo(text=f'Fetching a report ... ', placement='right')
        spinner.start()

        report = await self.report.get_report(id, hash, filters, sorts, graph)

        if not report or 'reports' not in report:
            spinner.fail()
            return
        else:
            reports: Dict = report['reports']
            flow_id = report['flowId'] if 'flowId' in report else ''
            if len(reports.keys()) != 1:
                spinner.fail()
                return

            spinner.succeed()

            if id not in reports:
                return

            report = reports[id]
            report['id'] = id
            report['flowId'] = flow_id

            self.logger.debug(self.formatter.format(report))


    async def get_formatted_report(self, report_id: str, format: str, output):

        spinner = Halo(text=f'Getting {format}-formatted report ... ', placement='right')
        spinner.start()

        report = await self.report.download_report(report_id, format)

        if report:
            spinner.succeed()
            async with aiofiles.open(output, 'w+' if isinstance(report, str) else 'wb') as writer:
                await writer.write(report)
        else:
            spinner.fail()
