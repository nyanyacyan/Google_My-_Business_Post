from logging import getLogger, Formatter, FileHandler, DEBUG
import pretty_errors
from tqdm import tqdm
from rich import print

pretty_errors.activate
import spreadsheet

# %(asctime)s  ログメッセージの生成と日付と時刻を出力する
# %(name)s  loggerの名前を出力する
# %(levelname)s  ログレベルを出力する
# %(message)s  メッセージを出力する
formatter = Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler = FileHandler("log_text")  # FileHandler:保存先の指定
file_handler.setFormatter(formatter)  # file_handlerに保存されたものをFormatterでログの表示形式を設定をセットする

main_logger = getLogger(__name__)
main_logger.addHandler(file_handler)  # 保存先に追加をするよってこと
main_logger.setLevel(DEBUG)

main_logger.debug("debug message from main.py")
main_logger.info("info message from main.py")
main_logger.warning("warning message from main.py")

spreadsheet_logger = getLogger("spreadsheet")
spreadsheet_logger.addHandler(file_handler)  # 保存先に追加をするよってこと
spreadsheet_logger.setLevel(DEBUG)

spreadsheet.log_message()
