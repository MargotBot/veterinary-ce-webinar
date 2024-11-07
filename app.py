from datetime import datetime
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    event_date = datetime(2024, 11, 18, 18, 0)  # 6:00 PM EST, Nov 18, 2024
    return render_template('index.html', event_date=event_date)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
