import asyncclick as aclick
from filescan_cli.common.config import load_config
from filescan_cli.flow.file import FileFlow

@aclick.group(name='files')
def files():
    pass


@files.command('file', short_help='Download a file')
@aclick.option('--config', type=str, is_flag=False, default='', help='Path to the config file')
@aclick.option('--hash', type=str, required=True, is_flag=False, help='File hash to be downloaded')
@aclick.option('--password', type=str, required=False, default='', help='Password used to encrypt the file')
@aclick.option('--output', type=str, required=False, default='downloaded.zip', help='Output path')
async def download_file(config: str, hash: str, password: str, output: str):

    load_config(config)

    file_flow = FileFlow()
    await file_flow.get_file(hash, password, output)
