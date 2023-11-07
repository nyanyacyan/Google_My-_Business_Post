# ライブラリ設定
import smtplib
from email.mime.text import MIMEText


def send_email(from_email, to_email, subject, message, smtp_password, smtp_host='smtp.gmail.com', smtp_port=587):
    msg = MIMEText(message, 'plain')
    msg['Subject'] = subject
    msg['To'] = to_email
    msg['From'] = from_email

    with smtplib.SMTP(smtp_host, smtp_port) as server:
        try:
            server.starttls()
            server.login(from_email, smtp_password)
            server.send_message(msg)
            print(f'メール送信が完了しました。')
        except Exception as e:
            print(f'メール送信に失敗しました:{e}')
