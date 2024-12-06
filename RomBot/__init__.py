import asyncio

from github import Auth, Github
from telegram.ext import ApplicationBuilder

from RomBot.config import Config

loop = asyncio.get_event_loop()

application = ApplicationBuilder().token(token=Config.BOT_TOKEN).build()

gh = Github(auth=Auth.Token(token=Config.GH_TOKEN))
