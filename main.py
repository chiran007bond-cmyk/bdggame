from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route("/bdg", methods=["GET"])
def bdg():
    url = "https://draw.ar-lottery01.com/WinGo/WinGo_1M/GetHistoryIssuePage.json?pageNo=1&pageSize=1"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/123.0 Safari/537.36"
    }
    res = requests.get(url, headers=headers)
    return jsonify(res.json())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
