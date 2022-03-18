from filescan_cli.formatter.features.base import BaseFormatter
from filescan_cli.formatter.types.ioc_types import IOCTypes
from filescan_cli.common.colors import colorize
from filescan_cli.formatter.utils import captialize_key


class IOCFormatter(BaseFormatter):

    def __init__(self):
        super().__init__()


    def format(self, report):

        resource = self._get_resource(report, 'file')
        result = f'''
        {colorize('IOCs')}
        '''
        for type in IOCTypes:
            key = type.value

            if key not in resource or not resource[key]:
                continue

            result += f'''
            {colorize(type.name)}'''

            values = resource[key]
            for value in values:
                origin = value['origin']['type']
                result += f'''
                Origin: {captialize_key(origin)}'''
                references = value['references']
                for reference in references:
                    output = f'{reference["data"]}'
                    if 'interesting' in reference and reference['interesting']:
                        output += f' ({colorize("interesting")})'

                    result += f'''
                {output}'''
                result += '\n'

        return result + '\n\n'
