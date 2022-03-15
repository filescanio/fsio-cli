import os
from typing import Optional
from core.logger import Logger
import json

FILE_READ_BLOCK_SIZE = 5242880  # 5M
USER_AGENT = 'Filescan Client'
API_KEY = os.environ.get('API_KEY', '')
SERVICE_BASE_URL = os.environ.get('SERVICE_BASE_URL', 'https://filescan.io')


def load_config(conf: Optional[str] = None):
    if not conf:
        return

    with open(conf, 'r') as reader:
        try:
            global API_KEY, SERVICE_BASE_URL
            config = json.load(reader)
            if 'API_KEY' in config:
                API_KEY = config['API_KEY']
            if 'SERVICE_BASE_URL' in config:
                SERVICE_BASE_URL = config['SERVICE_BASE_URL']
        except Exception as ex:
            Logger().exception(ex)
