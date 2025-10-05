import smtplib
import json
import os
import requests

def send_slack(webhook, text):
    if not webhook:
        return False
    try:
        resp = requests.post(webhook, json={'text': text}, timeout=5)
        return resp.status_code == 200
    except Exception:
        return False

def send_email(smtp_server, port, username, password, to_addr, subject, body):
    try:
        import smtplib
        from email.mime.text import MIMEText
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = username
        msg['To'] = to_addr
        s = smtplib.SMTP(smtp_server, port, timeout=10)
        s.starttls()
        s.login(username, password)
        s.sendmail(username, [to_addr], msg.as_string())
        s.quit()
        return True
    except Exception as e:
        print('Email failed:', e)
        return False
