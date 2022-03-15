from typing import Dict
from .base import BaseFormatter
from common.colors import colorize
from ..types.osint_types import ResourceTypes
from ..utils import captialize_key, format_dict, format_string, format_tags, format_verdict


class OsintFormatter(BaseFormatter):

    def __init__(self):
        super().__init__()


    def format(self, report: Dict) -> str:
        resource = self._get_resource(report, 'osint')

        if resource is None or 'results' not in resource:
            return ''

        osint = resource['results']
        if not osint:
            return ''

        result = f'''
        {colorize('Open Source Intelligence Lookup')}
        '''

        for item in osint:
            result += f'''
            {colorize(item['resource'])}
            '''

            result += f'''
                Type: {ResourceTypes[item['type'].lower()]}
                Origin: {captialize_key(item['origin']['type'])}
                Provider: {captialize_key(item['osintProvider'])}
                Verdict: {format_verdict(captialize_key(item['verdict']))}
            '''

            if 'tags' in item and item['tags']:
                result += f'''
                Tags: {format_tags(item['tags'])}
                '''

            provider_data = {}
            exceptions = ['resource', 'response_code', 'sha256', 'scans']
            for key in item['data']:
                if key in exceptions:
                    continue

                provider_data[key] = item['data'][key]

            result += format_dict(provider_data)

        return result

