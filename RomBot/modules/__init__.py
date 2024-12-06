import glob
from os.path import basename, dirname, isfile

from RomBot.logger import LOGGER


def list_all_modules():
    mod_paths = glob.glob(dirname(__file__) + "/*.py")
    all_modules = [
        basename(files)[:-3]
        for files in mod_paths
        if isfile(files) and files.endswith(".py") and not files.endswith("__init__.py")
    ]
    return all_modules


ALL_MODULES = list_all_modules()
LOGGER.info("Modules to load: %s", str(ALL_MODULES))
__all__ = ALL_MODULES + ["ALL_MODULES"]
