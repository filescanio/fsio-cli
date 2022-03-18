import os
import json
from filescan_cli.core.http import HttpRequests
from filescan_cli.common.utils import run_safe
from filescan_cli.service.endpoints import get_endpoint, FILE_SCAN
from filescan_cli.service.headers import get_private_header


class Scan():
    """Scan a file"""

    def __init__(self):
        self.http_client = HttpRequests()
        self.headers = get_private_header()


    async def upload(self, file, link, desc, tags, prop_tags, password, is_private):
        """Upload a file for scanning"""

        if file:
            name = os.path.basename(file)
        else:
            name = link[link.rindex('/') + 1:]

        result = await run_safe(
            self.http_client.post_file,
            get_endpoint(FILE_SCAN),
            self.headers,
            {
                'name': name,
                'path': file,
                'link': link,
                'extra': {
                    'description': desc,
                    'tags': tags,
                    'propagate_tags': f'{prop_tags}',
                    'password': password,
                    'is_private': f'{is_private}'
                }
            }
        )

        if result['success']:
            return { 'content': json.loads(result['content']) }
        else:
            return { 'error': result['content'] }
