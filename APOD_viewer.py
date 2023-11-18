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
    date = today
    if request.method == "POST":
        date = request.form["date"]
        url += f"&start_date={date}"

    content = requests.get(url).content
    data = json.loads(content)[0]

    return render_template("base.jinja", data=data, today=today)

if __name__ == "__main__":
    app.run(debug=True)