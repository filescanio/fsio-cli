import json
from core.http import HttpRequests
from common.utils import run_safe
from .endpoints import get_endpoint, SYSTEM_INFO, SYSTEM_CONFIG
from .headers import get_public_header


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

        return json.loads(result)


    async def get_config(self):

        endpoint = get_endpoint(SYSTEM_CONFIG)
        result = await run_safe(
            self.http_client.get,
            endpoint,
            headers=self.headers
        )

        return json.loads(result)
