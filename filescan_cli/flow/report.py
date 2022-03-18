import aiofiles
from halo import Halo
from filescan_cli.core.logger import Logger
from filescan_cli.formatter.report import ReportFormatter
from filescan_cli.service.report import Report

class ReportFlow:

    def __init__(self):
        self.report = Report()
        self.logger = Logger()
        self.formatter = ReportFormatter()


    async def get_report(self, id, hash, filters, sorts, graph):

        spinner = Halo(text=f'Fetching a report ... ', placement='right')
        spinner.start()

        result = await self.report.get_report(id, hash, filters, sorts, graph)

        if 'error' in result:
            spinner.fail(result['error'])
            return

        reports = result['content']['reports']
        flow_id = result['flowId'] if 'flowId' in result else ''
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


    async def get_formatted_report(self, report_id, format, output):

        spinner = Halo(text=f'Getting {format}-formatted report ... ', placement='right')
        spinner.start()

        report = await self.report.download_report(report_id, format)

        if 'error' in report:
            spinner.fail(report['error'])
        else:
            spinner.succeed()
            async with aiofiles.open(output, 'w+' if isinstance(report, str) else 'wb') as writer:
                await writer.write(report['content'])
