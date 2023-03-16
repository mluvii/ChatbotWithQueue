from datetime import datetime, timezone


class WorkerData:
    def __init__(self, server, bot, data):
        self.bot = bot
        self.data = data
        self.server = server


class Bot:
    def __init__(self, chatbot_id, client_id, client_secret):
        self.chatbot_id = chatbot_id
        self.client_id = client_id
        self.client_secret = client_secret


def datetime_now_iso():
    return datetime.now(timezone.utc).astimezone().isoformat()
