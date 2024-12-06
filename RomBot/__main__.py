import importlib

from NoobStuffs.libformatter import MARKDOWN
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import CommandHandler, ContextTypes

from RomBot import application, loop
from RomBot.config import Config
from RomBot.logger import LOGGER
from RomBot.modules import ALL_MODULES

for module_name in ALL_MODULES:
    imported_module = importlib.import_module("RomBot.modules." + module_name)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_first_name = update.effective_user.first_name
    bot_first_name = context.bot.first_name
    START_TEXT = ""
    START_TEXT += f"Hey {MARKDOWN.bold(f'{user_first_name}')}, I'm {MARKDOWN.bold(f'{bot_first_name}')}!\n\n"
    START_TEXT += f"{MARKDOWN.bold(f'•')} A bot made to provide information about the {MARKDOWN.hyperlink(f'{Config.ROM_NAME}', str(Config.WEBSITE_URL))} Official Devices.\n"
    START_TEXT += f"{MARKDOWN.bold(f'•')} Hit /help to find out more about how to use me to my full potential."
    keyboard = [
        [
            InlineKeyboardButton(
                text="Channel",
                url=f"https://t.me/{Config.CHANNEL_USERNAME}",
            ),
            InlineKeyboardButton(
                text="Support",
                url=f"https://t.me/{Config.SUPPORT_GROUP_USERNAME}",
            ),
        ],
        [
            InlineKeyboardButton(text="Website", url=Config.WEBSITE_URL),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.effective_message.reply_markdown(
        text=START_TEXT,
        reply_markup=reply_markup,
        disable_web_page_preview=True,
    )


async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    HELP_TEXT = ""
    HELP_TEXT += f"{MARKDOWN.bold('Available Commands:')}\n"
    HELP_TEXT += f"- /start: To start me.\n"
    HELP_TEXT += f"- /help: To get this message.\n"
    HELP_TEXT += (
        f"- /devicelist: To get a list of all the Officially Supported devices.\n"
    )
    HELP_TEXT += f"- /device {MARKDOWN.mono('{codename}')}: To get info about an Officially Supported device (case sensitive).\n"
    await update.effective_message.reply_markdown(text=HELP_TEXT)


def main():
    botcmds = [
        ("start", "to start the bot"),
        ("help", "to get help message"),
        ("devicelist", "to get a list of all the supported devices"),
        ("device", "to get info about an officially supported device"),
    ]
    loop.run_until_complete(application.bot.set_my_commands(botcmds))
    start_handler = CommandHandler("start", start)
    help_handler = CommandHandler("help", help)
    application.add_handler(start_handler)
    application.add_handler(help_handler)
    LOGGER.info("Using long polling.")
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    LOGGER.info("Successfully loaded modules: " + str(ALL_MODULES))
    main()
