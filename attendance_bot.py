cat > app.py <<EOF
from flask import Flask
from attendance_bot import run_attendance_bot

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running!"

@app.route('/run')
def run_bot():
    run_attendance_bot()
    return "Attendance triggered"
EOF
