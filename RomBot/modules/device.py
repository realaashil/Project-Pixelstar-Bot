from NoobStuffs.libformatter import MARKDOWN
from telegram import InlineKeyboardMarkup, Update
from telegram.constants import ParseMode
from telegram.ext import CommandHandler, ContextTypes

from RomBot import application
from RomBot.config import Config
from RomBot.helpers import (
    check_device,
    convert_to_inline_buttons,
    get_all_devices,
    get_info,
    process_message,
)


async def devicelist(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = await update.effective_message.reply_markdown(
        text=f"{MARKDOWN.mono('Getting a list of official devices...')}",
    )
    TEXT = f"{MARKDOWN.bold('Here is the list of all the supported devices:')}\n"
    count = 1
    for device in get_all_devices():
        TEXT += f"{count}. {MARKDOWN.mono(f'{device}')}\n"
        count += 1
    TEXT += f"\n{MARKDOWN.bold('Use')} {MARKDOWN.mono('/device {codename}')} {MARKDOWN.bold('to get info about specific device')}"
    await message.edit_text(
        text=TEXT,
        parse_mode=ParseMode.MARKDOWN,
    )


async def get_device(update: Update, context: ContextTypes.DEFAULT_TYPE):
    device_name = context.args
    if len(device_name) == 1:
        codename = device_name[0]
        message = await update.effective_message.reply_markdown(
            text=f"{MARKDOWN.mono(f'Getting info about {codename}...')}",
        )
        if not check_device(codename):
            TEXT = f"Device {MARKDOWN.mono(f'{codename}')} is not supported"
            return await message.edit_text(text=TEXT, parse_mode=ParseMode.MARKDOWN)
        TEXT = ""
        BUTTONS = []
        device_info = get_info(codename)
        use_path_in_buttons = True if len(device_info) > 1 else False
        for path, info in device_info.items():
            path = path.split("/")[-1].capitalize()
            message_content, buttons = process_message(Config.MESSAGE_TEMPLATE, info)
            if Config.SHOW_DEVICE_INFO_OF_ALL_PATHS and len(device_info) > 1:
                TEXT += f"{MARKDOWN.bold(f'{path}:')}\n"
                TEXT += message_content
                TEXT += "\n\n"
            else:
                TEXT = message_content
            keyboard_buttons = (
                convert_to_inline_buttons(buttons, f" - {path}")
                if use_path_in_buttons
                else convert_to_inline_buttons(buttons)
            )
            BUTTONS.extend(keyboard_buttons)
        reply_markup = InlineKeyboardMarkup(BUTTONS)
        await message.edit_text(
            text=TEXT,
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=reply_markup,
            disable_web_page_preview=True,
        )
    else:
        TEXT = f"{MARKDOWN.bold('Usage:')} {MARKDOWN.mono('/device {codename}')}"
        await update.effective_message.reply_markdown(text=TEXT)


devicelist_handler = CommandHandler("devicelist", devicelist)
device_handler = CommandHandler("device", get_device)
application.add_handler(devicelist_handler)
application.add_handler(device_handler)
