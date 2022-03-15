from typing import Dict
from common.colors import colorize
from .utils import format_tag, format_verdict


class ReportsFormatter:

    def __init__(self):
        pass

    def format(self, reports: list) -> str:

        result = ''
        for report in reports:
            result += self.__format_report(report)

        return result


    def __format_report(self, report: Dict) -> str:

        return f'''
            id: {report['id']}
            name: {colorize(report['file']['name'])}
            type: {report['file']['short_type']}
            hash: {report['file']['sha256']}
            verdict: {format_verdict(report['verdict'])}
            tags: {' '.join([format_tag(tag) for tag in report['tags']])}
            updated: {report['updated_date']}
        '''
