from filescan_cli.formatter.features.base import BaseFormatter
from filescan_cli.formatter.utils import format_dict
from filescan_cli.common.colors import colorize


class OfficeFormatter(BaseFormatter):

    def __init__(self):
        super().__init__()


    def format(self, report):

        if self._get_short_type(report) != 'office':
            return ''

        result = f'''
        {colorize('MS Office Details')}
        '''

        overview_output = self.__format_overview(report)
        result += overview_output
        
        return result


    def __format_overview(self, report):
        overview = self._get_details_overview(report)
        extended = self._get_extended_data(report)

        keys = ['vbaStomping']
        for key in keys:
            if key in extended:
                overview[key] = extended[key]

        overview_output = f'''
            {colorize('Overview')}{format_dict(overview)}
        '''

        return overview_output
