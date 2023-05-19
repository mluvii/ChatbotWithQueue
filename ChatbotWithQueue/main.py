import os
import logging
from flask import Flask, request
import json
from helpers import WorkerData, Bot, get_bot, get_server_url
from worker import requestQueue


app = Flask(__name__)

webhook_url = os.environ.get('WEBHOOK_URL') 

@app.route('/', methods=['GET'])
def index():
    return 'ok', 200


@app.route(f'/{webhook_url}', methods=['GET', 'POST'])
def chatbot():
    if request.method == 'GET':
        return 'OK', 200
    else:
        server_url = request.host.split(":")[0]
        chatbot_id = request.args.get('id')
        client_id = request.args.get('client_id')
        client_secret = request.args.get('client_secret')
        if chatbot_id is None or client_id is None or client_secret is None:
            defined_server_url = get_server_url()
            defined_bot = get_bot()
            logging.info(f'defined server: {server_url}')
            logging.info(f'defined bot: {defined_bot}')
            if defined_server_url is not None and defined_bot is not None:
                try:
                    data = json.loads(request.data)
                except ValueError as e:
                    return f'No valid data {e}', 400
                worker_data = WorkerData(defined_server_url, defined_bot, data)
                requestQueue.put(worker_data)
                logging.info("Returning OK")
                return 'OK'
            else:
                return 'Wrong chatbot or bad parameters', 400
        else:
            try:
                data = json.loads(request.data)
            except ValueError as e:
                return f'No valid data {e}', 400
            bot = Bot(chatbot_id, client_id, client_secret)
            worker_data = WorkerData(server_url, bot, data)
            requestQueue.put(worker_data)
            logging.info("Returning OK")
            return 'OK'
