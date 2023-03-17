import openai
from helpers import get_gpt_key
from chat_collections import get_session_messages, append_session_message


def send_msg_to_chatbot_api(session_id: int, message: str) -> str:
    openai.api_key = get_gpt_key()
    append_session_message(session_id, {"role": "user", "content": message})
    messages = get_session_messages(session_id)
    chat_completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    print(chat_completion)
    append_session_message(session_id, chat_completion.choices[0].message)
    answer = chat_completion.choices[0].message.content
    return answer
