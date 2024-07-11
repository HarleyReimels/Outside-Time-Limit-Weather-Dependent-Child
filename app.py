from flask import Flask, render_template, url_for
from dotenv import load_dotenv
import os
import requests
import json

load_dotenv()
api_key = os.getenv('apikey')
app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

if __name__ == "__main__":
    res= requests.get(f"https://api.tomorrow.io/v4/weather/forecast?location=34.00,-81.77&timesteps=1h&units=imperial&apikey={api_key}")
    response = json.loads(res.text)
    json_formatted = json.dumps(response, indent=4)
    with open('test.txt', 'w') as p:
        p.write(json_formatted)
    app.run(debug=True)