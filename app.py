from flask import Flask
from attendance_bot import run_attendance
import os
import requests

app = Flask(__name__)

@app.route("/run", methods=["GET"])
def trigger():
    run_attendance()
    return "Attendance triggered", 200

@app.route("/test", methods=["GET"])
def test_telegram():
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")
    message = "سلام علیرضا! این یه پیام تستی از render هست."

    url = f"https://api.telegram.org/bot{token}/sendMessage"
    response = requests.post(url, data={"chat_id": chat_id, "text": message})
    
    if response.status_code == 200:
        return "Test message sent!", 200
    else:
        return f"Error: {response.text}", 500

if __name__ == "__main__":
    app.run()
