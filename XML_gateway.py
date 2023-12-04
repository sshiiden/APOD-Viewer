from flask import Flask, render_template, request
import requests

def getData(args):
    API_KEY = "CtpP4rkxqLb297YpfL9T9m1X6UPNgqzpA6BiaW2y"
    url = f"https://api.nasa.gov/planetary/apod?api_key={API_KEY}"

    if args:
        if args.get("date"):
            url += f"&start_date={args.get('date')}"
            url += f"&end_date={args.get('date')}"
        if args.get("start_date"):
            url += f"&start_date={args.get('start_date')}"
        if args.get("end_date"):
            url += f"&end_date={args.get('end_date')}"
        if args.get("count"):
            url += f"&count={args.get('count')}"
        return requests.get(url).json()
    else:
        return [requests.get(url).json()]

app = Flask(__name__)
@app.route("/", methods = ["GET"])
def index():
    images = getData(request.args)
    return render_template("xml.jinja", images=images)

if __name__ == "__main__":
    app.run(port="5001", debug=True)