import re
from typing import Dict, List, Optional, Set, Tuple

from telegram import InlineKeyboardButton


def extract_placeholders(message: str) -> Set[str]:
    res = re.findall(r"\{(\w+?)\}", message)
    return set(res)


def extract_message_content(message: str) -> str:
    button_pattern = r"\[\[.*? \| .*?\]\]"
    message_without_buttons = re.sub(button_pattern, "", message).strip()
    return message_without_buttons


def extract_buttons(message: str) -> List[List[Dict[str, str]]]:
    button_pattern = r"\[\[(.*?) \| (.*?)\]\]"
    buttons = []
    message_lines = message.splitlines()
    for line in message_lines:
        line_buttons = re.findall(button_pattern, line)
        if line_buttons:
            buttons.append([{"text": btn[0], "url": btn[1]} for btn in line_buttons])
    return buttons


def process_message(
    message: str,
    data: Dict[str, str],
) -> Tuple[str, List[List[Dict[str, str]]]]:
    placeholders_in_message = extract_placeholders(message)
    for placeholder in placeholders_in_message:
        value = data.get(placeholder, f"({placeholder}_MISSING>")
        message = message.replace(f"{{{placeholder}}}", str(value))
    message_content = extract_message_content(message)
    buttons = extract_buttons(message)
    return message_content, buttons


def convert_to_inline_buttons(
    buttons: List[List[Dict]],
    append_text: Optional[str] = "",
) -> List[List[InlineKeyboardButton]]:
    inline_buttons = []
    for button_row in buttons:
        inline_button_row = []
        for button in button_row:
            button["text"] += append_text
            inline_button_row.append(
                InlineKeyboardButton(text=button["text"], url=button["url"]),
            )
        inline_buttons.append(inline_button_row)
    return inline_buttons
