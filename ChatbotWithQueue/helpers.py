from datetime import datetime, timezone
from dataclasses import dataclass


@dataclass(frozen=True)
class Bot:
    chatbot_id: str
    client_id: str
    client_secret: str

@dataclass
class WorkerData:
    server:str
    bot: Bot
    data:object

def datetime_now_iso():
    return datetime.now(timezone.utc).astimezone().isoformat()


server_url: str | None = None
gpt_key: str | None = None
bot: Bot | None = None


def set_bot(b: Bot) -> None:
    global bot
    bot = b


def get_bot() -> Bot | None:
    return bot


def set_server_url(s: str) -> None:
    global server_url
    server_url = s


def get_server_url() -> str | None:
    return server_url


def set_gpt_key(k: str) -> None:
    global gpt_key
    gpt_key = k


def get_gpt_key() -> str | None:
    return gpt_key
