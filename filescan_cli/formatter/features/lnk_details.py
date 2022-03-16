from typing import Dict
from filescan_cli.formatter.features.base import BaseFormatter
from filescan_cli.common.colors import colorize
from filescan_cli.formatter.utils import format_dict


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
