import logging
import threading
import queue
from mluvii_api import send_request
from response_creator import process_data

requestQueue = queue.Queue()


def worker():
    while True:
        item = requestQueue.get()
        logging.info(f'Working on {item}')
        logging.info(f'Server on {item.server}')
        logging.info(f'Chatbot ID on {item.bot}')
        logging.info(f'JSON data on {item.data}')
        process_message(item.server, item.bot, item.data)
        logging.info(f'Finished {item}')
        requestQueue.task_done()


# Turn-on the worker thread.
threading.Thread(target=worker, daemon=True).start()


def process_message(server, bot, data):
    if 'Activity' in data and 'Ping' in data['Activity']:
        return
    else:
        response_message = process_data(data)
        if response_message is None:
            return
        else:
            send_request(server, bot, response_message)
