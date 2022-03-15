import asyncclick as aclick
from common.config import load_config

@aclick.group(name='files')
def files():
    pass


@files.command('file', short_help='Download a file')
@aclick.option('--config', type=str, is_flag=False, default='', help='Path to the config file')
@aclick.option('--hash', type=str, required=True, is_flag=False, help='File hash to be downloaded')
async def download_file(config: str, hash: str):

    load_config(config)
    
    print(f'{hash}')
