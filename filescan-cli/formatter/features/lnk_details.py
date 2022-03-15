from typing import Dict
from .base import BaseFormatter
from common.colors import colorize
from ..utils import format_dict


class LnkFormatter(BaseFormatter):

    def __init__(self):
        super().__init__()


    def format(self, report: Dict) -> str:

        if self._get_short_type(report) != 'lnk':
            return ''

        result = f'''
        {colorize('Lnk Details')}
        '''

        overview_output = self.__format_overview(report)
        result += overview_output
        
        return result


    def __format_overview(self, report: Dict) -> str:
        overview = self._get_details_overview(report)
        overview_output = f'''
            {colorize('Overview')}{format_dict(overview)}
        '''

        return overview_output
