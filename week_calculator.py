from logging import getLogger
import pretty_errors
from tqdm import tqdm
from rich import print
import datetime

pretty_errors.activate

logger = getLogger(__name__)

def log_message():
    logger.debug("debug message from week_calculator.py")
    logger.info("info message from week_calculator.py")
    logger.warning("warning message from week_calculator.py")


def get_week_of_month(year, month, day):
    first_day_of_month = datetime.date(year, month, 1)
    first_day_weekday = first_day_of_month.weekday()  # weekday()で曜日を取得してる。月曜日が０、火曜日が１・・・

    print(first_day_weekday)  # 曜日を出力

    week_of_month = ((day + first_day_weekday)// 7) + (1 if (day + first_day_weekday)% 7 > 0 else 0)
    return week_of_month

date = datetime.date.today()
week_of_month = get_week_of_month(date.year, date.month, date.day)
print(f'{date}は{week_of_month}の週です。')