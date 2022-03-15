from typing import Dict
from .base import BaseFormatter
from common.colors import colorize
from ..utils import captialize_key, format_string


class StringsFormatter(BaseFormatter):

    def __init__(self):
        super().__init__()


    def format(self, report: Dict) -> str:
        resource = self._get_resource(report, 'file')

        if 'strings' not in resource or not resource['strings']:
            return ''

        result = f'''
        {colorize('Strings')}
        '''

        strings = resource['strings']
        for string in strings:
            origin = string['origin']['type']
            references = string['references']
            if not references:
                continue

            output = ''
            for reference in references:
                if 'interesting' in reference and reference['interesting']:
                    output += f'''
            {format_string(reference['str'])}'''

            if not output:
                continue

            output = f'''
            Origin: {captialize_key(origin)}''' + output
            result += (output + '\n')

        return result + '\n'
