import aiofiles
from typing import Dict
from halo import Halo
from filescan_cli.core.logger import Logger
from filescan_cli.service.file import File

class FileFlow:

    def __init__(self):
        self.file = File()
        self.logger = Logger()


    async def get_file(self, hash, password, output):

        spinner = Halo(text=f'Downloading a file ... ', placement='right')
        spinner.start()

        result = await self.file.get_file(hash, password)

        if 'error' in result:
            spinner.fail(result['error'])
            return


        async with aiofiles.open(output, 'wb') as writer:
            await writer.write(result['content'])

        spinner.succeed(f'File saved as {output}')
