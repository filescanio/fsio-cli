import json
from typing import Dict, List, Tuple
from core.http import HttpRequests
from common.utils import run_safe
from .endpoints import GET_FORMATTED_REPORT, GET_SCAN_REPORTS, GET_SPECIFIC_REPORT, SEARCH_REPORT, get_endpoint, GET_REPORTS
from .headers import get_private_header

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


    async def get_scan_reports(
        self, scan_id: str, filters: Tuple = (), sorts: Tuple = (), graph: bool = False
    ) -> Dict:
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

        return json.loads(result)


    async def get_reports(self, page: int, page_size: int) -> List:
        """Get reports"""

        endpoint = get_endpoint(GET_REPORTS)
        result = await run_safe(
            self.http_client.get,
            endpoint,
            headers=self.headers,
            params={ 'page': page, 'page_size': page_size }
        )

        result = json.loads(result)
        if not result or 'items' not in result:
            return None

        return result['items']


    async def get_report(
        self, id: str, hash: str, filters: Tuple = (), sorts: Tuple = (), graph: bool = False
    ) -> Dict:
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

        return json.loads(result)


    async def search_reports(self, params: Dict) -> List:
        """Search reports"""

        endpoint = get_endpoint(SEARCH_REPORT)
        result = await run_safe(
            self.http_client.get,
            endpoint,
            headers=self.headers,
            params=params
        )

        result = json.loads(result)
        if not result or 'items' not in result:
            return None

        return result['items']


    async def download_report(self, report_id: str, format: str):
        """Download a formatted report"""

        endpoint = get_endpoint(GET_FORMATTED_REPORT, report_id=report_id)
        result = await run_safe(
            self.http_client.get,
            endpoint,
            headers=self.headers,
            params={ 'format': format }
        )

        if result == '':
            return None

        return result
