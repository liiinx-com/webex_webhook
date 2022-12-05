from flask import Flask

app = Flask(__name__)

print("------------------------")

@app.route("/")
def hello_world():
    print("here")
    return "<p>Hello, World!!!</p>"


@app.post("/webook")
def webex_webhook():
    print("here")
    return "<p>Hello, World!!!</p>"