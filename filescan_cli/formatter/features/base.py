from filescan_cli.formatter.types.file_types import file_categories
from filescan_cli.formatter.utils import format_size


class BaseFormatter:

    def __init__(self):
        pass


    def format(self, report):
        pass


    def _get_details_overview(self, report):
        resource = self._get_resource(report, 'file')

        overview = {}
        if 'extendedData' in resource and 'fileMagicDescription' in resource['extendedData']:
            overview['fileMagicDescription'] = resource['extendedData']['fileMagicDescription']
        if 'fileSize' in resource:
            overview['size'] = format_size(resource['fileSize'])
        overview = { **overview, **resource['digests'] }

        if 'extendedData' in resource:
            extended = resource['extendedData']
            hashes = ['imphash', 'ssdeep', 'authentihash', 'sdhash', 'tlsh']
            for hash in hashes:
                if hash in extended:
                    overview[hash] = extended[hash]

        return overview


    def _get_resources(self, report):
        return report['resources'] if 'resources' in report else {}


    def _get_resource(self, report, type):
        resources = self._get_resources(report)
        for key in resources:
            resource = resources[key]
            if 'resourceReference' not in resource:
                continue
            if 'name' not in resource['resourceReference']:
                continue
            if resource['resourceReference']['name'] == type:
                return resource


    def _get_extended_data(self, report):
        resource = self._get_resource(report, 'file')
        if 'extendedData' in resource:
            return resource['extendedData']


    def _get_tags(self, report):
        return report['allTags'] if 'allTags' in report else []


    def _get_short_type(self, report):
        
        tags = self._get_tags(report)
        for tag in tags:
            if 'source' not in tag or tag['source'] != 'MEDIA_TYPE':
                continue
            if 'isRootTag' not in tag or not tag['isRootTag']:
                continue

            file_type = tag['tag']['name']
            for type in file_categories:
                if file_type in file_categories[type]:
                    return type

        return 'other'
                