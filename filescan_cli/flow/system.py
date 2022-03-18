from halo import Halo
from filescan_cli.core.logger import Logger
from filescan_cli.service.system import System

class SystemFlow:

    def __init__(self):
        self.logger = Logger()
        self.system = System()


    async def get_info(self):

        spinner = Halo(text=f'Getting system information ... ', spinner='dots', placement='right')
        result = await self.system.get_info()
        if 'error' in result:
            spinner.fail(result['error'])
        else:
            spinner.succeed()
            self.show_result(result['content'])


    async def get_config(self):

        spinner = Halo(text=f'Getting system configuration ... ', spinner='dots', placement='right')
        result = await self.system.get_config()
        if 'error' in result:
            spinner.fail(result['error'])
        else:
            spinner.succeed()
            self.show_result(result['content'])


    def show_result(self, result):

        formatted = ''
        for key in result:
            formatted += f'''
            {key}: {result[key]}'''

        self.logger.debug(formatted)
