import json
from typing import Dict
from core.http import HttpRequests
from common.utils import run_safe
from .endpoints import DOWNLOAD_FILE, get_endpoint
from .headers import get_private_header


class File:
    """Get reports or a report"""

    def __init__(self):
        self.http_client = HttpRequests()
        self.headers = get_private_header()


    async def get_file(self, hash: str, password: str):
        """Get reports from scan"""

        endpoint = get_endpoint(DOWNLOAD_FILE, file_hash=hash)
        result = await run_safe(
            self.http_client.get,
            endpoint,
            headers=self.headers,
            params={
                'type': 'raw',
                'password': password
            }
        )

        if result['success']:
            return { 'content': result['content'] }
        else:
            return { 'error': result['content'] }
