from flask import Flask
from attendance_bot import run_attendance_bot

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running!"

@app.route('/run')
def run_bot():
    try:
        run_attendance_bot()
        return "Attendance triggered"
    except Exception as e:
        return f"Error: {str(e)}", 500
