from filescan_cli.formatter.features.base import BaseFormatter
from filescan_cli.common.colors import colorize
from filescan_cli.formatter.utils import format_dict


class DefaultDetailsFormatter(BaseFormatter):

    def __init__(self):
        super().__init__()


    def format(self, report):
        
        result = f'''
        {colorize('File Details')}'''

        overview_output = self.__format_overview(report)
        result += overview_output
        
        return result


    def __format_overview(self, report):
        overview = self._get_details_overview(report)
        overview_output = f'''
            {format_dict(overview)}
        '''

        return overview_output
