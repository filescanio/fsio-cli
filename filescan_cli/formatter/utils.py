import math
import re
from filescan_cli.common.colors import colorize, get_verdict_color


MAX_LINE_SIZE = 64

def captialize_key(key):
    return ' '.join(map(lambda substr: substr.capitalize(), key.split('_')))


def format_dict(dict, *, depth = 0, eol = '\n'):

    result = ''
    for key in dict:
        name = captialize_key(key)
        if depth == 0:
            result += f'''
                {name}: {dict[key]}'''
        elif depth == 1:
            result += f'''
                    {name}: {dict[key]}'''
        else:
            result += f'''
                        {name}: {dict[key]}'''

    return result + eol


def format_verdict(verdict):
    return colorize(verdict, get_verdict_color(verdict))


def format_tag(tag):
    if 'tag' in tag and 'verdict' in tag['tag']:
        verdict = tag['tag']['verdict']['verdict']
    else:
        verdict = 'unknown'

    return colorize(tag['tag']['name'], get_verdict_color(verdict))


def format_tags(tags):
    return ', '.join([format_tag(tag) for tag in tags])


def format_size(size):
    idx = math.floor(math.log(size) / math.log(1024))
    return "{:.2f}".format(size / math.pow(1024, idx)) + ['B', 'kB', 'MB', 'GB', 'TB'][idx]


def format_string(text, max = MAX_LINE_SIZE):
    text = re.sub(' *\n+ *', ' ', text.strip())
    if len(text) > (max + 10):
        return text[:max] + '...'
    else:
        return text
