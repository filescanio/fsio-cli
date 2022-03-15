from typing import Dict
from .base import BaseFormatter
from common.colors import colorize
from ..utils import captialize_key, format_dict, format_string


class GeoFormatter(BaseFormatter):

    def __init__(self):
        super().__init__()


    def format(self, report: Dict) -> str:
        resource = self._get_resource(report, 'domain-resolve')
        if not resource or 'domainResolveResults' not in resource:
            return ''

        dr_result = resource['domainResolveResults']
        if not dr_result:
            return ''

        result = f'''
        {colorize('Located IPs')}
        '''

        for item in dr_result:
            result += f'''
            {colorize(item['inetAddr'])}
            '''
            result += f'''
                Domain: {item['resource']['data']}'''

            if 'geoData' in item and item['geoData']:
                geo_data = item['geoData']
                location = []
                if 'country_name' in geo_data:
                    location.append(geo_data['country_name'])
                if 'city' in geo_data:
                    location.append(geo_data['city'])
                result += f'''
                Location: {', '.join(location)}'''

                other = {}
                keys = ['country_code', 'latitude', 'longitude']
                for key in keys:
                    if key in geo_data:
                        other[key] = geo_data[key]

                if 'connection' in geo_data:
                    connection = geo_data['connection']
                    if 'asn' in connection:
                        other['ASN'] = connection['asn']
                    if 'isp' in connection:
                        other['ISP'] = connection['isp']

                result += format_dict(other)

        return result

