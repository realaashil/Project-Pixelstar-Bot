import json
from typing import Any, Dict, List, Set, Union

from github import GithubException

from RomBot import gh
from RomBot.config import Config

from .placeholder_helper import call_bot_placeholder


def extract_data(
    data: Dict[str, Any],
    structure: Dict[str, Any],
) -> Dict[str, Union[str, int, bool]]:
    items = {}
    for key, value in structure.items():
        if key in data:
            if isinstance(value, Dict):
                items.update(extract_data(data[key], value))
            elif isinstance(value, List):
                if isinstance(data[key], List):
                    for item in data[key]:
                        items.update(extract_data(item, value[0]))
                else:
                    items[key] = data[key]
            else:
                items[key] = data[key]
    return items


def get_all_devices() -> Set[str]:
    devices = set()
    repo = gh.get_repo(Config.OFFICIAL_DEVICES_REPO)
    for path in Config.DEVICE_JSON_PATHS:
        contents = repo.get_contents(path)
        for content_file in contents:
            if content_file.name.endswith(".json"):
                devices.add(content_file.name.replace(".json", ""))
    return devices


def check_device(device: str) -> bool:
    return device in get_all_devices()


def get_info(device: str) -> Dict[str, Dict[str, Union[bool, int, str]]]:
    device_info = {}
    repo = gh.get_repo(Config.OFFICIAL_DEVICES_REPO)
    for path in Config.DEVICE_JSON_PATHS:
        try:
            content = repo.get_contents(
                f"{path}/{device}.json",
            ).decoded_content.decode()
            info = json.loads(content)
            path_info = extract_data(info, Config.DEVICE_JSON_STRUCTURE)
            for key, placeholder in Config.BOT_PLACEHOLDERS.items():
                path_info[key] = call_bot_placeholder(placeholder, device)
            device_info[path] = path_info
        except GithubException:
            pass
    return device_info
