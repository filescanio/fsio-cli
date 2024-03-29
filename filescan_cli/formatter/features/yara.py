from filescan_cli.formatter.features.base import BaseFormatter
from filescan_cli.common.colors import colorize
from filescan_cli.formatter.utils import format_verdict, format_dict


class YaraFormatter(BaseFormatter):

    def __init__(self):
        super().__init__()


    def format(self, report):
        resource = self._get_resource(report, 'file')

        if 'yaraMatches' not in resource or not resource['yaraMatches']:
            return ''

        result = f'''
        {colorize('Matched Yara Rules')}
        '''
        yaras = resource['yaraMatches']
        for yara in yaras:
            result += self.__format_rule(yara)

        return result


    def __format_rule(self, rule):
        header = rule['ruleName']
        if 'verdict' in rule and 'verdict' in rule['verdict']:
            verdict = rule["verdict"]["verdict"].lower()
            header += f' ({format_verdict(verdict)})'

        matches = rule['matchedStrings']
        body = f'''
                Matches'''
        for match in matches:
            body += f'''
                    {match}'''

        if 'metaData' in rule:
            body += format_dict(rule['metaData'])

        return f'''
            {header}''' + body

        
        