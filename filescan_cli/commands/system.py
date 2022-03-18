import asyncclick as aclick
from filescan_cli.flow.system import SystemFlow
from filescan_cli.common.config import load_config


@aclick.group(name='system')
def system():
    pass


@system.command('sysinfo', short_help='Get system information')
@aclick.option('--config', type=str, is_flag=False, default='', help='Path to the config file')
async def sysinfo(config):

    load_config(config)

    system_flow = SystemFlow()
    await system_flow.get_info()


@system.command('sysconfig', short_help='Get system configuration')
@aclick.option('--config', type=str, is_flag=False, default='', help='Path to the config file')
async def sysconfig(config):

    load_config(config)

    system_flow = SystemFlow()
    await system_flow.get_config()
