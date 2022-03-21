import asyncclick as aclick
from filescan_cli.flow.scan import ScanFlow
from filescan_cli.common.config import load_config


@aclick.group(name='scan')
def scan():
    pass


@scan.command('upload', short_help='Upload a file')
@aclick.option('--config', type=str, is_flag=False, default='', help='Path to the config file')
@aclick.option('-f', '--file', type=str, required=True, help='File path to scan')
@aclick.option('-d', '--desc', type=str, is_flag=False, default='', help='Additional description of the file')
@aclick.option('-t', '--tags', type=str, is_flag=False, default='', help='| separated tags to propagate to the report')
@aclick.option('-p', '--prop-tags', type=bool, is_flag=True, default=False, help='Whether propagate tags to the report or not')
@aclick.option('--password', type=str, is_flag=False, default='', help='Custom password of the file to scan')
@aclick.option('--private', type=bool, is_flag=True, default=False, help='Whether the file can be shared or not')
async def upload(
    config,
    file,
    desc,
    tags,
    prop_tags,
    password,
    private
):

    load_config(config)

    scan_flow = ScanFlow()
    await scan_flow.run(file, None, desc, tags, prop_tags, password, private)


@scan.command('upload_link', short_help='upload a link')
@aclick.option('--config', type=str, is_flag=False, default='', help='Path to the config file')
@aclick.option('-l', '--link', type=str, required=True, is_flag=False, help='Link URL to scan. One of the link or file must be valid.')
@aclick.option('-d', '--desc', type=str, is_flag=False, default='', help='Additional description of the file')
@aclick.option('-t', '--tags', type=str, is_flag=False, default='', help='| separated tags to propagate to the report')
@aclick.option('-p', '--prop-tags', type=bool, is_flag=True, default=False, help='Whether propagate tags to the report or not')
@aclick.option('--password', type=str, is_flag=False, default='', help='Custom password of the file to scan')
@aclick.option('--private', type=bool, is_flag=True, default=False, help='Whether the file can be shared or not')
async def upload(
    config,
    link,
    desc,
    tags,
    prop_tags,
    password,
    private
):

    load_config(config)

    scan_flow = ScanFlow()
    await scan_flow.run(None, link, desc, tags, prop_tags, password, private)
