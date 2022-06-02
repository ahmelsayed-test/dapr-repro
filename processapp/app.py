import json
import os
import requests
import logging
import string
import random
import flask
from flask import request, jsonify
from flask_cors import CORS

logging.basicConfig(level=logging.INFO)

dapr_port = os.getenv("DAPR_HTTP_PORT")
target_app = os.getenv("TARGET_APP")
orders_url = "http://localhost:{}/v1.0/invoke/{}/method/orders".format(dapr_port, target_app)

app = flask.Flask(__name__)
CORS(app)


def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))


@app.route('/process', methods=['POST'])
def neworder():
    order = request.json
    headers = {
        "Large-Header1": get_random_string(4000),
        "Large-Header2": get_random_string(4000),
    }

    response = requests.post(orders_url, json=order, timeout=60, headers=headers)
    log_string = "New order submitted, content: {content}".format(content=json.dumps(order))
    app.logger.info(log_string)
    return response.text


app.run(host='0.0.0.0')
