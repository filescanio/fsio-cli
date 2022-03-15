from typing import Dict
from .base import BaseFormatter
from common.colors import colorize
from ..utils import format_dict


class EmulationFormatter(BaseFormatter):

    def __init__(self):
        super().__init__()


    def format(self, report: Dict) -> str:

        resource = self._get_resource(report, 'file')
        if 'emulationData' not in resource:
            return ''

        result = f'''
        {colorize('Emulation Data')}
        '''

        meta_output = self.__format_meta(report)
        result += meta_output
        data_output = self.__format_data(report)
        result += data_output

        return result


    def __format_meta(self, report: Dict) -> str:
        resource = self._get_resource(report, 'file')
        if 'emulationMetaData' not in resource:
            return ''

        result = ''
        metaData = resource['emulationMetaData']
        if 'Overview' not in metaData:
            return ''

        overview = metaData['Overview']
        if overview is not None and 'FunctionCount' in overview:
            meta = []
            for key in overview['FunctionCount']:
                meta.append({ 'function': key, 'count': overview['FunctionCount'][key] })

            meta.sort(key=lambda func: func['count'])

            if len(meta) > 0:
                result += f'''
            {colorize('Meta Data')}

                Function Count'''

                for item in meta:
                    result += f'''
                {item["function"]}: {item["count"]}'''

        for key in overview:
            if key == 'FunctionCount':
                continue

            if isinstance(overview[key], dict):
                result += f'''

                {key}{format_dict(overview[key])}'''
            elif isinstance(overview[key], list):
                result += f'''

                {key}'''
                for item in overview[key]:
                    result += f'''
                {item}'''
            else:
                result += f'''

                {key}: {overview[key]}'''

        return result


    def __format_data(self, report) -> str:
        resource = self._get_resource(report, 'file')
        data = resource['emulationData']

        if len(data) == 0:
            return ''

        result = f'''

            {colorize('Emulation Result')}
        '''
        for item in data:
            if 'action' not in item:
                continue
            if item['action'] == 'CallAPI':
                if 'additionalInformation' in item and 'Arguments' in item['additionalInformation']:
                    args = item['additionalInformation']['Arguments']
                    if isinstance(args, list):
                        item['additionalInformation']['Arguments'] = map(lambda arg: self.__split_api(arg), args)

            header = f'Action: {item["action"]}'
            if 'interesting' in item and item['interesting']:
                header += f'({colorize("interesting")})'

            if 'additionalInformation' in item:
                info = item['additionalInformation']
                if item['action'] == 'CallAPI':
                    if 'Library' in info and 'Alias' in info:
                        header += f' {info["Library"]}@{info["Alias"]}'
                else:
                    keys = ['Address', 'Alias', 'Class', 'Url', 'URI', 'Command', 'Program', 'ProcessName', 'Path', 'Event', 'Section', 'CodeModule', 'Dir', 'Duration', 'Language']
                    for key in keys:
                        if key in info:
                            header += f' {info[key]}'
                            break

            result += f'''
                {header}'''

            keys = ['dataUUID', 'additionalInformation', 'metaData', 'action', 'interesting']
            for key in item:
                if key in keys:
                    continue
                result += f'''
                    {key}: {item[key]}'''

            if 'additionalInformation' in item:
                info = item['additionalInformation']
                except_keys = ['Content']
                for key in info:
                    if key in except_keys:
                        continue

                    data = info[key]
                    if isinstance(data, list):
                        output = ', '.join([f'{item}' for item in data])
                    elif isinstance(data, dict):
                        output = format_dict(data, depth=2, eol='')
                    else:
                        output = f'{data}'

                    result += f'''
                    {key}: {output}'''

            result += '\n'

        return result


    def __split_api(self, arg: str) -> str:
        argList = []
        if arg.find('(VbValue ') >= 0:
            strArguments: list[str] = filter(lambda item: item, arg.split('(VbValue '))
            for idx in range(len(strArguments)):
                value = strArguments[idx]
                if idx >= len(strArguments) - 1:
                    value = value[:len(value) - 1]
                else:
                    value = value[:len(value) - 2]

                pair = value.split(' ')
                argList.append({ 'name': pair[0], 'value': pair[1] })
        else:
            strArguments: list[str] = filter(lambda item: item, arg.split(', '))
            for value in strArguments:
                if value.find('=') > 0:
                    pair = value.split('=')
                    argList.append({ 'name': pair[0], 'value': pair[1] })
                else:
                    argList.append({ 'name': 'Param', 'value': value })

        return argList
