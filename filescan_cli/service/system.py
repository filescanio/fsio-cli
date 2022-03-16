import json
from filescan_cli.core.http import HttpRequests
from filescan_cli.common.utils import run_safe
from filescan_cli.service.endpoints import get_endpoint, SYSTEM_INFO, SYSTEM_CONFIG
from filescan_cli.service.headers import get_public_header


class System:
    
    def __init__(self):
        self.http_client = HttpRequests()
        self.headers = get_public_header()


    async def get_info(self):

        endpoint = get_endpoint(SYSTEM_INFO)
        result = await run_safe(
            self.http_client.get,
            endpoint,
            headers=self.headers
        )

        if result['success']:
            return { 'content': json.loads(result['content']) }
        else:
            return { 'error': result['content'] }


    async def get_config(self):

        endpoint = get_endpoint(SYSTEM_CONFIG)
        result = await run_safe(
            self.http_client.get,
            endpoint,
            headers=self.headers
        )

        if result['success']:
            return { 'content': json.loads(result['content']) }
        else:
            return { 'error': result['content'] }
