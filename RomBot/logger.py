import logging

from NoobStuffs.liblogging import setup_logging

logging.getLogger("ptb").setLevel(logging.ERROR)
logging.getLogger("httpx").setLevel(logging.ERROR)

LOGGER = setup_logging("RomBot")
