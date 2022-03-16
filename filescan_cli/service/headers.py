from typing import Dict
import filescan_cli.common.config as config


def get_public_header() -> Dict:
    return {
        'accept': 'application/json',
        'User-Agent': config.USER_AGENT
    }


def get_private_header() -> Dict:
    return {
        'X-Api-Key': config.API_KEY,
        'accept': 'application/json',
        'User-Agent': config.USER_AGENT
    }
