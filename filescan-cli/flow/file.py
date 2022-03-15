import aiofiles
from typing import Dict
from core.logger import Logger
from halo import Halo
from service.file import File

class FileFlow:

    def __init__(self):
        self.file = File()
        self.logger = Logger()


    async def get_file(self, hash: str, password: str, output: str) -> Dict:

        spinner = Halo(text=f'Downloading a file ... ', placement='right')
        spinner.start()

        result = await self.file.get_file(hash, password)

        if 'error' in result:
            spinner.fail(result['error'])
            return


        async with aiofiles.open(output, 'wb') as writer:
            await writer.write(result['content'])

        spinner.succeed(f'File saved as {output}')
