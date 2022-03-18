from typing import Dict
from filescan_cli.common.colors import colorize
from filescan_cli.formatter.utils import format_tag, format_verdict


class ReportsFormatter:

    def __init__(self):
        pass

    def format(self, reports, total = -1):

        result = f'''
            Total Count: {total}
        ''' if total >= 0 else ''

        for report in reports:
            result += self.__format_report(report)

        return result


    def __format_report(self, report):

        type = report['file']['short_type'] if 'short_type' in report['file'] else report['file']['type']
        tags = report['tags'] if 'tags' in report else report['allTags']
        date = report['updated_date'] if 'updated_date' in report else report['created_date']
        verdict = report['verdict'] if 'verdict' in report else report['finalVerdict']['verdict'].lower()
        return f'''
            id: {report['id']}
            name: {colorize(report['file']['name'])}
            type: {type}
            hash: {report['file']['hash']}
            verdict: {format_verdict(verdict)}
            tags: {' '.join([format_tag(tag) for tag in tags])}
            updated: {date}
        '''
