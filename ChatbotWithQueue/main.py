import logging
from flask import Flask, request
import json
from helpers import WorkerData, Bot
from worker import requestQueue


app = Flask(__name__)


@app.route('/testbot', methods=['POST', 'GET'])
def chatbot():
    if request.method == 'GET':
        return 'OK'
    else:
        server_url = request.host.split(":")[0]
        chatbot_id = request.args.get('id')
        client_id = request.args.get('client_id')
        client_secret = request.args.get('client_secret')
        if chatbot_id is None or client_id is None or client_secret is None:
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
