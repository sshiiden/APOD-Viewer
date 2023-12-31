from flask import Flask, render_template, request
import requests
import datetime

def getData():
    API_KEY = "CtpP4rkxqLb297YpfL9T9m1X6UPNgqzpA6BiaW2y"
    url = f"https://api.nasa.gov/planetary/apod?api_key={API_KEY}"

    today = datetime.datetime.now().date()
    data = {"filter_type": "single",
            "start_date": today,
            "end_date": today,
            "n_images": 1,
            "today": today}
    
    if request.method == "POST":
        match request.form["filter_type"]:
            case "single":
                url += f"&start_date={request.form['start_date']}"
                url += f"&end_date={request.form['start_date']}"
            case "range":
                url += f"&start_date={request.form['start_date']}"
                url += f"&end_date={request.form['end_date']}"
            case "random":
                url += f"&count={request.form['n_images']}"
        data["filter_type"] = request.form["filter_type"]
        data["start_date"] = request.form["start_date"]
        data["end_date"] = request.form["end_date"]
        data["n_images"] = request.form["n_images"]
    elif request.method == "GET":
        url += f"&start_date={today}"

    images = requests.get(url).json()

    return (images, data)

app = Flask(__name__)
@app.route("/", methods = ["POST", "GET"])
def index():
    images, data = getData()
    return render_template("viewer/base.jinja", images=images, data=data)

if __name__ == "__main__":
    host = "127.0.0.1"
    port = 5000
    debug = True
    app.run(host, port, debug)