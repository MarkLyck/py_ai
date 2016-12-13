from flask import Flask
from flask import request
import json

from NLP.NLP import tasks

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Aimi API'


@app.route('/message', methods=['POST'])
def messageReceived():
    if request.method == 'POST':
        originalMessage = request.json['message']
        msgObj = tasks(originalMessage)

        return json.dumps(msgObj)
