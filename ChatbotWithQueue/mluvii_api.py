import requests
import json
import logging


def get_access_token(bot, server_url):

    url = f'https://{server_url}/login/connect/token'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    logging.debug("Url is: " + url + " with ci: " + bot.client_id + " and secret " + bot.client_secret)
    payload = {
        'response_type': 'token',
        'grant_type': 'client_credentials',
        'client_id': bot.client_id,
        'client_secret': bot.client_secret
    }
    response = requests.post(url, headers=headers, data=payload, verify=False)

    if response.status_code == 200:
        access_token = response.json()['access_token']
        logging.debug("access token is: " + access_token)
        return access_token
    else:
        raise logging.error("Could not retrieve access token.")


def get_headers(bot, server_url):
    return {
        'Authorization': f'Bearer {get_access_token(bot, server_url)}',
        'Content-Type': 'application/json'
    }


def send_request(server_url, bot, payload):
    logging.info("bot id: " + str(bot.chatbot_id))
    data = json.dumps(payload)
    logging.info(f'payload: {data}')
    response = requests.post(f'https://{server_url}/api/v1/Chatbot/{str(bot.chatbot_id)}/activity',
                             headers=get_headers(bot, server_url), data=data, verify=False)
    if response.status_code != 200 and response.status_code != 201:
        raise NameError('Response not successful')
