from typing import Any, Dict, List

from NoobStuffs.libyamlconfig import YAMLConfig

config = YAMLConfig("config.yaml")


class Config:
    BOT_TOKEN: str = config.getConfig("bot_token", is_required=True)
    GH_TOKEN: str = config.getConfig("gh_token", is_required=True)
    ROM_NAME: str = config.getConfig("rom_name", is_required=True)
    CHANNEL_USERNAME: str = config.getConfig("channel_username", is_required=True)
    SUPPORT_GROUP_USERNAME: str = config.getConfig(
        "support_group_username",
        is_required=True,
    )
    WEBSITE_URL: str = config.getConfig("website_url", is_required=True)
    OFFICIAL_DEVICES_REPO: str = config.getConfig(
        "official_devices_repo",
        is_required=True,
    )
    DEVICE_JSON_PATHS: List[str] = config.getConfig(
        "device_json_paths",
        is_required=True,
        return_type=list,
    )
    SHOW_DEVICE_INFO_OF_ALL_PATHS: bool = config.getConfig(
        "show_device_info_of_all_paths",
        is_required=True,
        return_type=bool,
    )
    DEVICE_JSON_STRUCTURE: Dict[str, Any] = config.getConfig(
        "device_json_structure",
        is_required=True,
        return_type=dict,
    )
    MESSAGE_TEMPLATE: str = config.getConfig("message_template", is_required=True)
