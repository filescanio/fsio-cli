import aiohttp
import asyncio
from aiohttp.http_exceptions import HttpProcessingError
from typing import Any, Dict
from common.singleton import Singleton


class HttpRequests(metaclass=Singleton):
    """Http requests.

    All requests are performed asyncronously.
    """

    def __init__(self):
        pass


    async def post_file(
        self,
        url: str,
        headers: Dict,
        file_data: Dict
    ):
        """Post file"""

        if "extra" in file_data:
            body_headers = file_data["extra"]
        else:
            body_headers = {}

        async with aiohttp.ClientSession(
            connector=self.__getConnector()
        ) as session:

            form_data = aiohttp.FormData()

            if "path" in file_data and file_data["path"]:
                form_data.add_field(
                    'file',
                    open(file_data['path'], 'rb'),
                    content_type="application/octet-stream"
                )

            elif "link" in file_data:
                form_data.add_field("link", file_data["link"])

            async with session.post(
                url, data=form_data, headers={**headers, **body_headers}
            ) as response:

                json = await response.text()
                if response.status >= 200 and response.status < 300:
                    return json
                else:
                    raise HttpProcessingError(code=response.status, message=json)


    async def get_multiple(self, data):
        """Perform multiple get requests"""

        async with aiohttp.ClientSession(connector=self.__getConnector()) as session:
            tasks = []
            for item in data:
                tasks.append(self.__get_multiple_item(item, session))

            return await asyncio.gather(*tasks)


    async def __get_multiple_item(self, data, session):
        """Perform single get request from a list of many requests"""

        json = await self.__get(data["url"], data["headers"], session)

        return {"group": data["group_id"], "json": json}


    async def get(self, url: str, headers: Dict, params = {}):
        """Perform get request"""

        async with aiohttp.ClientSession(connector=self.__getConnector()) as session:
            return await self.__get(url, headers, params, session)


    async def __get(self, url: str, headers: Dict, params: Any, session: aiohttp.ClientSession):
        """Perform get request with provided session object"""

        async with session.get(url, headers=headers, params=params) as response:
            if response.content_type == 'application/json':
                result = await response.text()
            else:
                result = await response.read()

            return result


    def __getConnector(self):
        """Get connector with options for handling connection"""

        # TODO: verify SSL certificates instead of skipping verification
        return aiohttp.TCPConnector(ssl=False)
