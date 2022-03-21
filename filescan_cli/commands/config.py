import asyncclick as aclick
from filescan_cli.common import config


@aclick.group(name='config')
def conf():
    pass


@conf.command('config', short_help='Configure global parameters')
@aclick.option('-x', '--api-key', type=str, is_flag=False, help='Set API key used for all commands')
@aclick.option('-s', '--service-base-url', type=str, is_flag=False, default='', help='Set base URL of the service for all commands')
async def global_config(api_key, service_base_url):

    if not api_key and not service_base_url:
        config.load_config()
        config.print_config()
        print('You can set values using the below options\n')
        print(global_config.get_help(aclick.get_current_context()))
        return

    if api_key:
        config.API_KEY = api_key
    if service_base_url:
        config.SERVICE_BASE_URL = service_base_url

    config.save_config()
