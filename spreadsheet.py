from logging import getLogger
import pretty_errors
from tqdm import tqdm
from rich import print

pretty_errors.activate

logger = getLogger(__name__)

def log_message():
    logger.debug("debug message from spreadsheet.py")
    logger.info("info message from spreadsheet.py")
    logger.warning("warning message from spreadsheet.py")