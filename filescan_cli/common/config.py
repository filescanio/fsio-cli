import os
import json
from filescan_cli.core.logger import Logger

FILE_READ_BLOCK_SIZE = 5242880  # 5M
USER_AGENT = 'Filescan Client'
API_KEY = os.environ.get('API_KEY', '')
SERVICE_BASE_URL = os.environ.get('SERVICE_BASE_URL', 'https://filescan.io')


def load_config(path = None):

    config_path = path
    if not config_path:
        config_path = prepare_store_path()

    with open(config_path, 'r') as reader:
        try:
            global API_KEY, SERVICE_BASE_URL
            config = json.load(reader)
            if 'API_KEY' in config:
                API_KEY = config['API_KEY']
            if 'SERVICE_BASE_URL' in config:
                SERVICE_BASE_URL = config['SERVICE_BASE_URL']

            if path:
                save_config(config)

        except Exception as ex:
            Logger().exception(ex)


def save_config(config):
    path = prepare_store_path()
    with open(path, 'w') as writer:
        writer.write(json.dumps(config))


def prepare_store_path():
    home = os.path.expanduser('~')
    conf_folder = os.path.join(home, '.filescan')

    if not os.path.exists(conf_folder):
        os.makedirs(conf_folder, exist_ok=True)

    return os.path.join(conf_folder, 'config.json')
