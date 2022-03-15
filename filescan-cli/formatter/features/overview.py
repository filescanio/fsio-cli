from typing import Dict, List, Any
from common.colors import colorize, get_verdict_color
from .base import BaseFormatter
from ..utils import format_dict
import re

class OverviewFormatter(BaseFormatter):
    """Report overview"""

    def __init__(self):
        super().__init__()


    def format(self, report: Dict) -> str:
        submission_info: Dict[str, Any] = self.__format_submission_info(report)
        result = f'''
        {colorize('Overview')}
        '''

        if 'finalVerdict' in report:
            result += self.__format_verdict_level(report['finalVerdict'])
        result += submission_info
        result += self.__format_tags(report)
        result += self.__format_signals(report)

        return result


    def __format_submission_info(self, report: Dict) -> str:

        result = f'''
            Submission Info'''

        submission_info: Dict[str, Any] = self.__get_submission_info(report)
        return result + format_dict(submission_info)


    def __format_verdict_level(self, verdict: Dict) -> str:
        level = f' / {int(verdict["confidence"] * 100)}%'
        verdict = verdict['verdict']
        return f'''
            Verdict: {colorize(verdict.capitalize() + level, get_verdict_color(verdict))}
        '''


    def __format_tags(self, report: Dict) -> str:

        if 'allTags' not in report:
            return ''

        tags = report['allTags']
        return f'''
            Tags: ''' + ', '.join([self.__format_tag(tag) for tag in tags]) + '\n'


    def __format_signals(self, report: Dict) -> str:

        if 'allSignalGroups' not in report or len(report['allSignalGroups']) == 0:
            return ''

        def get_key(signal: Dict):
            threat_level = signal['verdict']['threatLevel'] if 'verdict' in signal and 'threatLevel' in signal['verdict'] else ''
            return 1 - threat_level

        signal_groups: List = report['allSignalGroups']
        signal_groups.sort(key=get_key)

        result = ''
        old_verdict = ''
        for group in signal_groups:
            signal_output = ''
            verdict = group['verdict']['verdict'].lower()
            if old_verdict != verdict:
                old_verdict = verdict
                signal_output += f'''
            {colorize(verdict.capitalize() + ' Signal Groups', get_verdict_color(verdict))}'''
            signal_output += f'''
                Description: {group['description']}'''

            if 'allTags' in group and len(group['allTags']) > 0:
                signal_output += f'''
                Tags: ''' + ', '.join([self.__format_tag(tag) for tag in group['allTags']])

            if 'allMitreTechniques' in group and len(group['allMitreTechniques']) > 0:
                techniques = group['allMitreTechniques']
                techs = []
                for tech in techniques:
                    if 'relatedTactic' in tech:
                        techs.append(f'{tech["relatedTactic"]["name"]} / {tech["name"]}')
                    else:
                        techs.append(f'{tech["name"]}')

                signal_output += f'''
                Mitre Techniques: ''' + ', '.join(techs)

            if 'signals' in group and len(group['signals']) > 0:
                signals = group['signals']
                for signal in signals:
                    signal['signalReadable'] = re.sub(' *\n+ *', ' ', signal['signalReadable'])
                signal_output += f'''
                Signals: ''' + ', '.join(
                    [f'''
                    {signal["signalReadable"]} / {' '.join(map(lambda substr: substr.capitalize(), signal["originType"].split('_')))}'''
                    for signal in signals]
                )

            signal_output += '\n'
            result += signal_output

        return result


    def __format_tag(self, tag: Dict) -> str:
        if 'tag' in tag and 'verdict' in tag['tag']:
            verdict = tag['tag']['verdict']['verdict']
            return colorize(tag['tag']['name'], get_verdict_color(verdict))
        else:
            return tag['tag']['name']


    def __get_submission_info(self, report: Dict) -> Dict:
        
        submission_info = { 'report_id': report['id'] }

        resource = self.__get_resource(report, 'file')
        scan_url = (
            'metaData' in resource and 
            'isUrlToFileAnalysis' in resource['metaData'] and
            resource['metaData']['isUrlToFileAnalysis']
        )

        if scan_url:
            submission_info['URL'] = report['file']['name']
            submission_info['SHA-256 (URL)'] = report['file']['hash']
            submission_info['SHA-256 (File)'] = resource['digests']['SHA-256']
        else:
            submission_info['name'] = report['file']['name']
            submission_info['SHA-256'] = resource['digests']['SHA-256']

        submission_info['media_type'] = resource['mediaType']['string']
        if 'flowId' in report:
            submission_info['submission_id'] = report['flowId']
        if 'created_date' in report:
            submission_info['submission_date'] = report['created_date']

        return submission_info


    def __get_resources(self, report: Dict) -> Dict:
        return report['resources'] if 'resources' in report else {}


    def __get_resource(self, report: Dict, type: str) -> Dict:
        resources = self.__get_resources(report)
        for key in resources:
            resource = resources[key]
            if 'resourceReference' not in resource:
                continue
            if 'name' not in resource['resourceReference']:
                continue
            if resource['resourceReference']['name'] == type:
                return resource
