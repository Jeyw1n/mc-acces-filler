import json


def get_settings() -> dict:
    with open('config.json', 'r', encoding='UTF-8') as f:
        config: dict = json.load(f)
    return config
