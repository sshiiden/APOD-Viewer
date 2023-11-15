from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

@app.route("/", methods = ["POST", "GET"])
def index():
    API_KEY = "CtpP4rkxqLb297YpfL9T9m1X6UPNgqzpA6BiaW2y"
    url = f"https://api.nasa.gov/planetary/apod?api_key={API_KEY}"

    date = ""
    if request.method == "POST":
        date = request.form["date"]
    if date:
        url += f"&date={date}"

    r = requests.get(url).content
    y = json.loads(r)

    return render_template("base.jinja", image=y["url"])

if __name__ == "__main__":
    app.run(debug=True)