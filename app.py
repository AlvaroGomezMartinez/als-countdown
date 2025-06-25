from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

# Retirement date
RETIREMENT_DATE = datetime(2026, 1, 31)

@app.route("/")
def index():
    today = datetime.now()
    time_remaining = RETIREMENT_DATE - today
    days = time_remaining.days
    hours = time_remaining.seconds // 3600
    minutes = (time_remaining.seconds % 3600) // 60
    seconds = time_remaining.seconds % 60
    return render_template("index.html", today=today)

if __name__ == "__main__":
    app.run(debug=True)