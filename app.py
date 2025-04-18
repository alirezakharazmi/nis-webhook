from flask import Flask
from attendance_bot import run_attendance

app = Flask(__name__)

@app.route("/run", methods=["GET"])
def trigger():
    run_attendance()
    return "Attendance triggered", 200

if __name__ == "__main__":
    app.run()
