import logging
from threading import Thread
from queue import Queue
from mluvii_api import send_request
from response_creator import process_data, process_data_for_chat_gpt, create_typing_message, create_not_typing_message
from helpers import get_gpt_key

requestQueue = Queue()


def worker() -> None:
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
Thread(target=worker, daemon=True).start()


def process_message(server, bot, data):
    if 'Activity' in data and 'Ping' in data['Activity']:
        return
    else:
        gpt_key = get_gpt_key()
        if gpt_key is not None:
            typing = create_typing_message(data)
            send_request(server, bot, typing)
            response_message = process_data_for_chat_gpt(data)
            if response_message is None:
                not_typing = create_not_typing_message(data)
                send_request(server, bot, not_typing)
                return
            else:
                not_typing = create_not_typing_message(data)
                send_request(server, bot, not_typing)
                send_request(server, bot, response_message)
        else:
            response_message = process_data(data)
            if response_message is None:
                return
            else:
                send_request(server, bot, response_message)



