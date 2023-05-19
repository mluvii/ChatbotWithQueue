import openai
from helpers import get_gpt_key, get_gpt_model
from chat_collections import get_session_messages, append_session_message
import logging


logging.basicConfig(
    format="%(asctime)s %(levelname)-8s %(message)s", level=logging.INFO
)


def send_msg_to_chatbot_api(session_id: int, message: str) -> str:
    try:
        openai.api_key = get_gpt_key()
        append_session_message(session_id, {"role": "user", "content": message})
        messages = get_session_messages(session_id)
        chat_completion = openai.ChatCompletion.create(
            model=get_gpt_model(), messages=messages
        )
        print(chat_completion)
        append_session_message(session_id, chat_completion.choices[0].message)
        answer = chat_completion.choices[0].message.content
        return answer
    except openai.error.RateLimitError as e:
        logging.error(e)
        return f"Rate limit exceeded: {str(e)}"
