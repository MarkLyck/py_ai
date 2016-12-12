from flask import Flask
from flask import request
import json

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Aimi API'


@app.route('/message', methods=['POST'])
def messageReceived():
    if request.method == 'POST':

        message = request.json['message']

        return json.dumps({
            "reply": message
        })
