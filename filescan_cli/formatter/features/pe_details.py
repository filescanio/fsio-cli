from filescan_cli.formatter.features.base import BaseFormatter
from filescan_cli.common.colors import colorize
from filescan_cli.formatter.utils import format_dict


class PeFormatter(BaseFormatter):

    def __init__(self):
        super().__init__()


    def format(self, report):

        if self._get_short_type(report) != 'pe':
            return ''

        result = f'''
        {colorize('PE Details')}
        '''

        overview_output = self.__format_overview(report)
        result += overview_output
        
        return result


    def __format_overview(self, report):
        overview = self._get_details_overview(report)
        extended = self._get_extended_data(report)

        keys = ['architecture', 'subsystemReadable', 'language', 'packers', 'isDigitallySigned', 'isDotNet', 'isPacked']
        for key in keys:
            if key in extended:
                overview[key] = extended[key]

        if 'dates' in extended:
            overview['date'] = extended['dates']['dateUtc']

        overview_output = f'''
            {colorize('Overview')}{format_dict(overview)}
        '''

        return overview_output
