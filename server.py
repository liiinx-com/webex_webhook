from flask import Flask, request

app = Flask(__name__)

print("------------------------")

@app.route("/")
def hello_world():
    print("here")
    return "<p>Hello, World!</p>"


@app.post('/webhook')
def webex_webhook():
    print("here")
    print(request.get_json())
    return "<p>Hello, World!</p>"
    


#export PATH="/project/home/liiinx-com/.local/bin:$PATH"
#flask --app server --debug run