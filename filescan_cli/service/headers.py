import filescan_cli.common.config as config


def get_public_header():
    return {
        'accept': 'application/json',
        'User-Agent': config.USER_AGENT
    }


def get_private_header():
    return {
        'X-Api-Key': config.API_KEY,
        'accept': 'application/json',
        'User-Agent': config.USER_AGENT
    }
