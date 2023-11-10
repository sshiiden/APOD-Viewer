from flask import Flask
import requests

app = Flask(__name__)

@app.route("/")
def index():
    API_KEY = "DEMO_KEY"
    date = "2017-08-18"
    url = f"https://api.nasa.gov/planetary/apod?date={date}&api_key={API_KEY}"
    r = requests.get(url).content
    return r

if __name__ == "__main__":
    app.run(debug=True)