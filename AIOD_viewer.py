from flask import Flask, render_template
import requests
import json

app = Flask(__name__)

@app.route("/")
def index():
    API_KEY = "CtpP4rkxqLb297YpfL9T9m1X6UPNgqzpA6BiaW2y"
    #date = "2017-08-18"
    #url = f"https://api.nasa.gov/planetary/apod?date={date}&api_key={API_KEY}"
    url = f"https://api.nasa.gov/planetary/apod?api_key={API_KEY}"

    r = requests.get(url).content
    y = json.loads(r)

    return render_template("base.jinja", image=y["url"])

if __name__ == "__main__":
    app.run(debug=True)