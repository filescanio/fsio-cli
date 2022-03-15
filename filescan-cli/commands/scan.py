import asyncclick as aclick
from flow.scan import ScanFlow
from common.config import load_config


@aclick.group(name='scan')
def scan():
    pass


@scan.command('upload', short_help='upload a file')
@aclick.option('--config', type=str, is_flag=False, default='', help='Path to the config file')
@aclick.option('-f', '--file', type=str, is_flag=False, default='', help='File path to scan')
@aclick.option('-l', '--link', type=str, is_flag=False, default='', help='Link URL to scan. One of the link or file must be valid.')
@aclick.option('-d', '--desc', type=str, is_flag=False, default='', help='Additional description of the file')
@aclick.option('-t', '--tags', type=str, is_flag=False, default='', help='| separated tags to propagate to the report')
@aclick.option('-p', '--prop-tags', type=bool, is_flag=True, default=False, help='Whether propagate tags to the report or not')
@aclick.option('--password', type=str, is_flag=False, default='', help='Custom password of the file to scan')
@aclick.option('--private', type=bool, is_flag=True, default=False, help='Whether the file can be shared or not')
async def upload(
    config: str,
    file: str,
    link: str,
    desc: str,
    tags: str,
    prop_tags: bool,
    password: str,
    private: bool
):

    load_config(config)

    scan_flow = ScanFlow()
    await scan_flow.run(file, link, desc, tags, prop_tags, password, private)
