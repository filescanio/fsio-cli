from typing import Dict
from core.logger import Logger
from halo import Halo
from service.system import System

class SystemFlow:

	def __init__(self):
		self.logger = Logger()
		self.system = System()


	async def get_info(self):

		spinner = Halo(text=f'Getting system information ... ', spinner='dots', placement='right')
		result = await self.system.get_info()
		if result is None:
			spinner.fail()
		else:
			spinner.succeed()
			self.show_result(result)


	async def get_config(self):

		spinner = Halo(text=f'Getting system configuration ... ', spinner='dots', placement='right')
		result = await self.system.get_config()
		if result is None:
			spinner.fail()
		else:
			spinner.succeed()
			self.show_result(result)


	def show_result(self, result: Dict):

		formatted = ''
		for key in result:
			formatted += f'''
			{key}: {result[key]}'''

		self.logger.debug(formatted)
