import json
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, world!"

@app.route("/data")
def get_data():
    data = {"message": "this is my message"}
    return json.dumps(data, ensure_ascii=False, indent=3)

if __name__ == "__main__":
    app.run(port=8000)