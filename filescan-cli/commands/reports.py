import asyncclick as aclick
from flow.reports import ReportsFlow
from common.config import load_config


@aclick.group(name='reports')
def reports():
    pass


@reports.command('reports', short_help='Get reports')
@aclick.option('--config', type=str, is_flag=False, default='', help='Path to the config file')
@aclick.option('--page', type=int, is_flag=False, default=1, help='Page number')
@aclick.option('--page-size', type=int, is_flag=False, default=10, help='Page size')
async def get_reports(config: str, page: int, page_size: int):
    """Get reports"""

    load_config(config)

    reports_flow = ReportsFlow()
    await reports_flow.get_reports(page, page_size)


@reports.command('search', short_help='Search reports')
@aclick.option('--config', type=str, is_flag=False, default='', help='Path to the config file')
@aclick.option('--filename', type=str, is_flag=False, help='File name')
@aclick.option(
    '--filetype',
    is_flag=False,
    type=aclick.Choice([
        '64bits', 'apk', 'bat', 'bmp', 'doc',
        'docm', 'docx', 'dot', 'dotm', 'dotx',
        'eml', 'elf', 'gif', 'hta', 'htm',
        'html', 'img', 'java', 'java-bytecode',
        'javascript', 'jpg', 'lnk', 'mbox',
        'mthml', 'msg', 'msi', 'mso', 'ole',
        'pdf', 'pedll', 'peexe', 'png', 'ppt',
        'pptm', 'pptx', 'pot', 'potm', 'potx',
        'ps', 'pub', 'powershell', 'rfc822',
        'rtf', 'svg', 'txt', 'vbs', 'wsf',
        'xls', 'xlsm', 'xlsb', 'xlsx',
        'xlt', 'xltm', 'xltx'
    ], case_sensitive=False),
    help='File type'
)
@aclick.option('--media-type', type=str, is_flag=False, help='Media type')
@aclick.option(
    '--verdict',
    type=aclick.Choice([
        'benign', 'informational', 'suspicious', 'likely_malicious', 'malicious', 'unknown'
    ], case_sensitive=False),
    is_flag=False,
    help='Verdict'
)
@aclick.option('--tag', type=str, is_flag=False, help='Tag')
@aclick.option('--date-from', type=str, is_flag=False, help='Start of the date range of when report created at')
@aclick.option('--date-to', type=str, is_flag=False, help='End of the date range of when report created at')
@aclick.option('--domain', type=str, is_flag=False, help='Domain')
@aclick.option('--ip', type=str, is_flag=False, help='IP')
@aclick.option('--url', type=str, is_flag=False, help='URL')
@aclick.option('--uuid', type=str, is_flag=False, help='UUID')
@aclick.option('--email', type=str, is_flag=False, help='Email')
@aclick.option('--reg-path', type=str, is_flag=False, help='Registry path')
@aclick.option('--rev-id', type=str, is_flag=False, help='Revision save id')
@aclick.option('--sha1', type=str, is_flag=False, help='SHA1')
@aclick.option('--sha256', type=str, is_flag=False, help='SHA256')
@aclick.option('--sha512', type=str, is_flag=False, help='SHA512')
@aclick.option('--md5', type=str, is_flag=False, help='MD5')
@aclick.option('--imphash', type=str, is_flag=False, help='Imphash')
@aclick.option('--ssdeep', type=str, is_flag=False, help='Ssdeep')
@aclick.option('--fuzzyfsiohash', type=str, is_flag=False, help='Fuzzyfsiohash')
@aclick.option('--authentihash', type=str, is_flag=False, help='Authentihash')
@aclick.option('--yara-rule', type=str, is_flag=False, help='Yara rule')
@aclick.option('--age', type=int, is_flag=False, help='Search reports with age of "age" days')
@aclick.option('--page', type=int, is_flag=False, default=1, help='Page number starting from 1')
@aclick.option('--page-size', type=int, is_flag=False, default=10, help='Page size')
async def search_reports(**kwargs):
    """Get reports"""

    load_config(kwargs['config'])
    del kwargs['config']

    params = {}
    for param in kwargs:
        value = kwargs[param]
        if value is not None:
            params[param] = value

    reports_flow = ReportsFlow()
    await reports_flow.search(params)
