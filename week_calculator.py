from logging import getLogger
import pretty_errors
from rich import print
import datetime
import calendar

pretty_errors.activate

logger = getLogger(__name__)

def log_message():
    logger.debug("debug message from week_calculator.py")
    logger.info("info message from week_calculator.py")
    logger.warning("warning message from week_calculator.py")


# 今日の日付から何週目かを出す
def get_week_of_month(year, month, day):
    month_calendar = calendar.monthcalendar(year, month)
    for index, week in enumerate(month_calendar):
        if day in week:
            return index + 1  # indexは０スタートのため＋１

today = datetime.date.today()
current_month = today.month
current_month_name = calendar.month_name[current_month]
print(current_month_name)

# 今日の日付がその月の何週目かを数値にて出力
week_of_month = get_week_of_month(today.year, today.month, today.day)
print(f'{week_of_month}週目')