from gmailsendsys import send_email

# 処理が成功した際にメールを送る機能
def success_send():
    # 送信するメールの情報を設定
    # 送信元
    from_email = '*****@gmail.com'

    # メールを送る相手のアドレス
    to_email = '*****@gmail.com'

    # 件名
    subject = 'テストメール'

    # 本文
    message = '今日も最高でした。'

    # アプリパスワードを設定
    # やり方 Googleのアカウント→セキュリティ→2段階認証→アプリパスワード
    smtp_password = 'eaqa kyvh pmso xzmr'

    # メール送信関数を呼び出す
    send_email(from_email, to_email, subject, message, smtp_password)
