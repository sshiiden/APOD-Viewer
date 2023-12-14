from flask import Flask, render_template, request
import requests

def checkArgs(args, allowed):
    for key in args:
        if key not in allowed:
            return False
    return True

def getData(args):
    API_KEY = "CtpP4rkxqLb297YpfL9T9m1X6UPNgqzpA6BiaW2y"
    url = f"https://api.nasa.gov/planetary/apod?api_key={API_KEY}"

    if args:
        if checkArgs(args, ("date", "start_date", "end_date", "count")):
            if "date" in args:
                url += f"&start_date={args.get('date')}"
                url += f"&end_date={args.get('date')}"
            if "start_date" in args:
                url += f"&start_date={args.get('start_date')}"
            if "end_date" in args:
                url += f"&end_date={args.get('end_date')}"
            if "count" in args:
                url += f"&count={args.get('count')}"
            return requests.get(url).json()
        else:
            return {"code": 400,
                    "msg": "Bad Request: incorrect field passed."}
    else:
        return [requests.get(url).json()]

app = Flask(__name__)
@app.route("/", methods = ["GET"])
def index():
    data = getData(request.args)
    return render_template("xml/base_XML.jinja", data=data)

if __name__ == "__main__":
    host = "127.0.0.1"
    port = 5001
    debug = True
    app.run(host, port, debug)