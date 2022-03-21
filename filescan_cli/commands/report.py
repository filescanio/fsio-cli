import asyncclick as aclick
from filescan_cli.flow.report import ReportFlow
from filescan_cli.flow.reports import ReportsFlow
from filescan_cli.common.config import load_config


@aclick.group(name='report')
def report():
    pass


@report.command('report', short_help='Get reports or report related to the report id and file hash')
@aclick.option('--config', type=str, is_flag=False, default='', help='Path to the config file')
@aclick.option('--id', type=str, required=True, is_flag=False, help='''
Report id: Must be given when flow option is absent, or will be ignored
''')
@aclick.option('--hash', type=str, required=True, is_flag=False, help='''
File hash the report contains. Must be given when id is specified
''')
@aclick.option('-f', '--filters', type=str, is_flag=False, multiple=True, default=[], help='Filters that apply to the report')
@aclick.option('-s', '--sorts', type=str, is_flag=False, multiple=True, default=[], help='Sorting that apply to the report')
@aclick.option('-g', '--graph', type=bool, is_flag=True, default=False, help='Whether get emulation graph or not')
async def get_report(
    config,
    id,
    hash,
    filters,
    sorts,
    graph
):

    load_config(config)

    report_flow = ReportFlow()
    await report_flow.get_report(id, hash, filters, sorts, graph)


@report.command('scan_reports', short_help='Get reports or report related to scan')
@aclick.option('--config', type=str, is_flag=False, default='', help='Path to the config file')
@aclick.option('--flow', type=str, required=True, is_flag=False, help='Flow id')
async def get_report(config, flow):

    load_config(config)

    reports_flow = ReportsFlow()
    await reports_flow.get_scan_reports(flow)


@report.command('export', short_help='Export report in the given format')
@aclick.option('--config', type=str, is_flag=False, default='', help='Path to the config file')
@aclick.option('--id', type=str, required=True, help='Report id to be exported')
@aclick.option('--format', required=True, type=aclick.Choice(['misp', 'stix', 'html', 'pdf'], case_sensitive=True), default='misp', help='Export format')
@aclick.option('--output', '-o', type=str, is_flag=False, default='report.out', help='Output path where report is saved')
async def export_report(config, id, format, output):

    load_config(config)

    report_flow = ReportFlow()
    await report_flow.get_formatted_report(id, format, output)
