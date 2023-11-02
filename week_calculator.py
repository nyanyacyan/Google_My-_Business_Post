from logging import getLogger
import pretty_errors
from tqdm import tqdm
from rich import print
import datetime
import calendar

pretty_errors.activate

logger = getLogger(__name__)

def log_message():
    logger.debug("debug message from week_calculator.py")
    logger.info("info message from week_calculator.py")
    logger.warning("warning message from week_calculator.py")


def get_week_of_month(year, month, day):
    '''
    現在の月が何週あるかを出力する関数
    calendarモジュールを使うと日曜日始まり。
    カレンダーでweekリストを作成
    index（０からスタート）に１をプラスすることで週数を割り出す。
    '''
    month_calendar = calendar.monthcalendar(year, month)
    for index, week in enumerate(month_calendar):
        if day in week:
            return index + 1

today = datetime.date.today()

# 今日の日付がその月の何週目かを数値にて出力
week_of_month = get_week_of_month(today.year, today.month, today.day)