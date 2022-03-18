import json
from filescan_cli.core.http import HttpRequests
from filescan_cli.common.utils import run_safe
from filescan_cli.service.endpoints import GET_FORMATTED_REPORT, GET_SCAN_REPORTS, GET_SPECIFIC_REPORT, SEARCH_REPORT, get_endpoint, GET_REPORTS
from filescan_cli.service.headers import get_private_header

DEFAULT_FILTERS = [
    'general', 'allSignalGroups', 'allTags', 'overallState',
    'positionInQueue', 'taskReference', 'subtaskReferences',
    'finalVerdict', 'fd:fileDownloadResults', 'fd:extractedUrls',
    'dr:domainResolveResults', 'v:visualizedSample.compressedBase64',
    'v:renderedImages', 'wi:whoisLookupResults', 'f:all', 'o:all'
]
DEFAULT_SORTS = [
    'allSignalGroups(description:asc,allMitreTechniques:desc,averageSignalStrength:desc)',
    'allOsintTags(tag.name:asc)',
    'f:disassemblySections(levelOfInformation:desc)',
    'f:extendedData.importsEx(module.suspicious:desc)'
]

class Report:
    """Get reports or a report"""

    def __init__(self):
        self.http_client = HttpRequests()
        self.headers = get_private_header()


    async def get_scan_reports(self, scan_id, filters = (), sorts = (), graph = False):
        """Get reports from scan"""

        endpoint = get_endpoint(GET_SCAN_REPORTS, scan_id=scan_id)
        filters = filters or DEFAULT_FILTERS
        sorts = sorts or DEFAULT_SORTS

        result = await run_safe(
            self.http_client.get,
            endpoint,
            headers=self.headers,
            params={
                'filter': filters or DEFAULT_FILTERS,
                'sort': sorts or DEFAULT_SORTS,
                'other': ['emulationGraph'] if graph else []
            }
        )

        if result['success']:
            return { 'content': json.loads(result['content']) }
        else:
            return { 'error': result['content'] }


    async def get_reports(self, page, page_size):
        """Get reports"""

        endpoint = get_endpoint(GET_REPORTS)
        result = await run_safe(
            self.http_client.get,
            endpoint,
            headers=self.headers,
            params={ 'page': page, 'page_size': page_size }
        )

        if result['success']:
            result = json.loads(result['content'])
            if 'items' not in result:
                return { 'content': [] }
            else:
                return { 'content':result['items'] }
        else:
            return { 'error': result['content'] }


    async def get_report(self, id, hash, filters = (), sorts = (), graph = False):
        """Get a specific report"""

        endpoint = get_endpoint(GET_SPECIFIC_REPORT, report_id=id, file_hash=hash)
        result = await run_safe(
            self.http_client.get,
            endpoint,
            headers=self.headers,
            params={
                'filter': filters or DEFAULT_FILTERS,
                'sort': sorts or DEFAULT_SORTS,
                'other': ['emulationGraph'] if graph else []
            }
        )

        if result['success']:
            return { 'content': json.loads(result['content']) }
        else:
            return { 'error': result['content'] }


    async def search_reports(self, params):
        """Search reports"""

        endpoint = get_endpoint(SEARCH_REPORT)
        result = await run_safe(
            self.http_client.get,
            endpoint,
            headers=self.headers,
            params=params
        )

        if result['success']:
            result = json.loads(result['content'])
            if 'items' not in result:
                return { 'content': [], 'total': 0 }
            else:
                return { 'content':result['items'], 'total': result['count'] }
        else:
            return { 'error': result['content'] }


    async def download_report(self, report_id, format):
        """Download a formatted report"""

        endpoint = get_endpoint(GET_FORMATTED_REPORT, report_id=report_id)
        result = await run_safe(
            self.http_client.get,
            endpoint,
            headers=self.headers,
            params={ 'format': format }
        )

        if result['success']:
            return { 'content': result['content'] }
        else:
            return { 'error': result['content'] }
