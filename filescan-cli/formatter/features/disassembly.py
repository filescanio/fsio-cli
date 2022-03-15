from typing import Dict
from .base import BaseFormatter
from common.colors import colorize


class DisassemblyFormatter(BaseFormatter):

    def __init__(self):
        super().__init__()


    def format(self, report: Dict) -> str:
        resource = self._get_resource(report, 'file')

        if 'disassemblySections' not in resource or not resource['disassemblySections']:
            return ''

        result = f'''
        {colorize('Disassembly Sections')}
        '''
        sections = resource['disassemblySections']
        for section in sections:
            result += f'''
            RVA: {section['fileRva']}, {section['humanDescriptor']}, {len(section['instructions'])} instructions'''

        return result + '\n\n'
