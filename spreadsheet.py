from logging import getLogger
import pretty_errors
from rich import print
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import week_calculator

pretty_errors.activate

logger = getLogger(__name__)

def log_message():
    logger.debug("debug message from spreadsheet.py")
    logger.info("info message from spreadsheet.py")
    logger.warning("warning message from spreadsheet.py")


scopes = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
service_account_file = 'gspread-401409-c734de15aef5.json'

credentials = ServiceAccountCredentials.from_json_keyfile_name(service_account_file, scopes)

gs = gspread.authorize(credentials)

spreadsheet_key = '10RWjNIESE8VdK9DbWmix9cV5FmMeVuXuG31eZuQMuP4'
spreadsheet = gs.open_by_key(spreadsheet_key)

# それぞれのワークシートを定義して辞書にする。
worksheets_dict = {
    "January": spreadsheet.worksheet("January"),
    "February": spreadsheet.worksheet("February"),
    "March": spreadsheet.worksheet("March"),
    "April": spreadsheet.worksheet("April"),
    "May": spreadsheet.worksheet("May"),
    "June": spreadsheet.worksheet("June"),
    "July": spreadsheet.worksheet("July"),
    "August": spreadsheet.worksheet("August"),
    "September": spreadsheet.worksheet("September"),
    "October": spreadsheet.worksheet("October"),
    "November": spreadsheet.worksheet("November"),
    "December": spreadsheet.worksheet("December")
}

# 週数からセルの値を指定するための辞書を作成。
cell_addresses = {
    1: 'B2',
    2: 'B3',
    3: 'B4',
    4: 'B5',
    5: 'B6'
}

# モジュールからのものを変数に置換
current_month_name = week_calculator.current_month_name
week_of_month = week_calculator.week_of_month

# 辞書を使用して今月のワークシートを選択します
current_worksheet = worksheets_dict[current_month_name]

# week_of_monthで出された数値をcell_addressesからindexの値を抽出
cell_address = cell_addresses[week_of_month]

# acellでcell_addressで指定されたセルの値を出力
cell_value = current_worksheet.acell(cell_address).value

if cell_value is None:
    print(f'今週分のスプレッドシートが記載されてません。')
else:
    print(cell_value)

