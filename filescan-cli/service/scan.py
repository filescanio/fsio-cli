import os
import json
from typing import Optional
from core.http import HttpRequests
from common.utils import run_safe
from .endpoints import get_endpoint, FILE_SCAN
from .headers import get_private_header


class Scan():
    """Scan a file"""

    def __init__(self):
        self.http_client = HttpRequests()
        self.headers = get_private_header()


    async def upload(
        self,
        file: Optional[str],
        link: Optional[str],
        desc: str,
        tags: str,
        prop_tags: bool,
        password: str,
        is_private: bool
    ):
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

        return json.loads(result)
