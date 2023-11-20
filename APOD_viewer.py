from flask import Flask, render_template, request
import requests
import json
import datetime

app = Flask(__name__)

@app.route("/", methods = ["POST", "GET"])
def index():
    API_KEY = "CtpP4rkxqLb297YpfL9T9m1X6UPNgqzpA6BiaW2y"
    url = f"https://api.nasa.gov/planetary/apod?api_key={API_KEY}"

    today = datetime.datetime.now().date()
    start_date = today
    end_date = None

    if request.method == "POST":
        start_date = request.form["start_date"]
        end_date = request.form["end_date"]

    url += f"&start_date={start_date}"
    if end_date:
        url += f"&end_date={end_date}"

    content = requests.get(url).content
    images = json.loads(content)

    return render_template("base.jinja", images=images, today=today, start_date=start_date, end_date=end_date)

if __name__ == "__main__":
    app.run(debug=True)