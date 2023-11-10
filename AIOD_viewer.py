from flask import Flask
import requests

app = Flask(__name__)

@app.route("/")
def index():
    r = requests.get("https://api.nasa.gov/planetary/apod?date=2017-08-18&api_key=DEMO_KEY").content
    return r

if __name__ == "__main__":
    app.run(debug=True)