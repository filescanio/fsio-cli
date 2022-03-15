import aiofiles
import os
from common.utils import run_async
from common.config import FILE_READ_BLOCK_SIZE


class File():
    """File utility class"""

    def __init__(self):
        pass


    async def open(self, path: str, mode: str):
        """Open a file"""

        return aiofiles.open(path, mode)


    async def streamer(self, path: str, mode: str):
        """Async iterator for file streaming"""

        if not await self.file_exists(path):
            raise FileNotFoundError

        resource = await self.open(path, mode)
        async with resource as reader:
            chunk = await reader.read(FILE_READ_BLOCK_SIZE)
            while chunk:
                yield chunk
                chunk = await reader.read(FILE_READ_BLOCK_SIZE)


    async def file_exists(self, path: str) -> bool:
        """Check if a give path exist"""

        return await run_async(os.path.exists, path)
