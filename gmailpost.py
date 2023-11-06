from google.oauth2 import service_account
from googleapiclient.discovery import build

# jsonファイルを指定して認証を実施
SERVICE_ACCOUNT_FILE = 'credentials.json'

# Gmail全ての権限付与
SCOPES = ['https://www.googleapis.com/auth/gmail.modify']


# service_account.Credentials.from_service_account_fileメソッドを使用して、サービスアカウントのJSONキーファイルから認証情報を読み込み
credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

service = build('gmail', 'v1', credentials=credentials)
