from datetime import datetime, timezone
from dataclasses import dataclass


class WorkerData:
    def __init__(self, server, bot, data):
        self.bot = bot
        self.data = data
        self.server = server


@dataclass
class Bot:
    chatbot_id:str
    client_id:str
    client_secret:str


def datetime_now_iso():
    return datetime.now(timezone.utc).astimezone().isoformat()
