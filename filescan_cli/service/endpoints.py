import filescan_cli.common.config as config

FILE_SCAN = '/api/scan/file'

GET_SCAN_REPORTS = '/api/scan/{scan_id}/report'
GET_FORMATTED_REPORT = '/api/reports/{report_id}/download'
GET_SPECIFIC_REPORT = '/api/reports/{report_id}/{file_hash}'
GET_REPORTS = '/api/users/uploads'

DOWNLOAD_FILE = '/api/files/{file_hash}'

SEARCH_REPORT = '/api/reports/search'

SYSTEM_INFO = '/api/system/info'
SYSTEM_CONFIG = '/api/system/config'


def get_endpoint(ep, **kwargs):

    result = ep
    for key in kwargs:
        result = result.replace(f'{{{key}}}', kwargs[key])

    return f'{config.SERVICE_BASE_URL}{result}'
