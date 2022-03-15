from typing import Dict
from .base import BaseFormatter
from common.colors import colorize
from ..utils import format_dict, format_size, format_string, format_tag


class FilesFormatter(BaseFormatter):

    def __init__(self):
        super().__init__()


    def format(self, report: Dict) -> str:
        resource = self._get_resource(report, 'file')

        if 'extractedFiles' not in resource or not resource['extractedFiles']:
            return ''

        result = f'''
        {colorize('Extracted Files')}
        '''

        files = resource['extractedFiles']
        for file in files:
            result += self.__format_file(file)

        return result + '\n'


    def __format_file(self, file: Dict) -> str:
        overview = {}
        name = file['submitName'] if 'submitName' in file else ''
        if 'extendedData' in file and 'fileMagicDescription' in file['extendedData']:
            overview['description'] = format_string(file['extendedData']['fileMagicDescription'])
        if 'fileSize' in file:
            overview['size'] = format_size(file['fileSize'])
        if 'mediaType' in file and 'string' in file['mediaType']:
            overview['type'] = file['mediaType']['string']

        hashes = {
            'MD5': file['digests']['MD5'],
            'SHA1': file['digests']['SHA-1'],
            'SHA256': file['digests']['SHA-256'],
            'SHA512': file['digests']['SHA-512']
        }

        meta = file['metaData'] if 'metaData' in file else {}
        tags = file['allTags'] if 'allTags' in file else []

        result = f'''
            {colorize(name)}
        '''
        if tags:
            result += f'''
                Tags: {', '.join([format_tag(tag) for tag in tags])}
            '''

        result += f'''
                Overview{format_dict(overview)}'''
        result += f'''
                Hashes{format_dict(hashes)}'''
        result += f'''
                Meta{format_dict(meta)}'''

        return result
