from filescan_cli.formatter.features.base import BaseFormatter
from filescan_cli.common.colors import colorize
from filescan_cli.formatter.utils import format_dict


class MboxFormatter(BaseFormatter):

    def __init__(self):
        super().__init__()


    def format(self, report):

        if self._get_short_type(report) != 'mbox':
            return ''

        result = f'''
        {colorize('Mbox Details')}
        '''

        overview_output = self.__format_overview(report)
        result += overview_output
        
        return result


    def __format_overview(self, report):
        overview = self._get_details_overview(report)
        resource = self._get_resource(report, 'file')

        if 'metaData' in resource:
            meta = resource['metaData']
            keys = ['Subject', 'From', 'To', 'Date', 'In-Reply-To']
            for key in keys:
                if key in meta:
                    overview[key] = meta[key]

        overview_output = f'''
            {colorize('Overview')}{format_dict(overview)}
        '''

        return overview_output
