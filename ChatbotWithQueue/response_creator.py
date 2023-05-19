import logging
import message_types
from chatgpt_api import send_msg_to_chatbot_api


def create_typing_message(data):
    session_id = data['sessionId']
    return message_types.message_typing(session_id, True)


def create_not_typing_message(data):
    session_id = data['sessionId']
    return message_types.message_typing(session_id, False)


def process_data_for_chat_gpt(data):
    if 'text' not in data or 'sessionId' not in data:
        return None
    text_to_process = data['text']
    session_id = data['sessionId']
    resp = send_msg_to_chatbot_api(session_id, text_to_process)
    return message_types.message_payload(resp, session_id)


def process_data(data):
    if 'text' not in data or 'sessionId' not in data:
        return None
    else:
        text_to_process = data['text']
        session_id = data['sessionId']
        logging.info(f'Text to process: {text_to_process}')
        match text_to_process:
            case 'GetAvailableOperators':
                return message_types.message_get_available_operators(session_id)
            case 'GetAvailableGroups':
                return message_types.message_get_available_groups(session_id)
            case 'GetHeroCards':
                return message_types.message_get_hero_cards(session_id)
            case 'GetCallParams':
                return message_types.message_get_call_params(session_id)
            case 'HandOff':
                return message_types.message_hand_off(session_id)
            case 'EndConversation':
                return message_types.message_end_conversation(session_id)
            case 'Typing':
                return message_types.message_typing(session_id, True)
            case 'NotTyping':
                return message_types.message_typing(session_id, False)
            case 'DisableGuestInput':
                return message_types.message_disable_guest_input(session_id)
            case 'EnableGuestInput':
                return message_types.message_enable_guest_input(session_id)
            case 'EnableGuestUpload':
                return message_types.message_enable_guest_upload(session_id)
            case 'DisableGuestUpload':
                return message_types.message_disable_guest_upload(session_id)
            case 'Carousel':
                return message_types.message_carousel(session_id)
            case 'Buttons':
                return message_types.message_buttons(session_id)
            case 'Hello':
                return message_types.message_hello(session_id)
            case 'ChatbotOpenFileUploadPrompt':
                return message_types.message_chatbot_open_file_upload_prompt(session_id)
            case 'SendImage':
                return message_types.send_image(session_id)
            case 'SendYoutubeLink':
                return message_types.send_youtube_video(session_id)
            case 'SendMp4Link':
                return message_types.send_mp4_video(session_id)
            case 'GetMediaObjects':
                return message_types.get_media_objects(session_id)
            case _:
                if 'SendHeroCard' in text_to_process:
                    hc_id = text_to_process.split(' ', 1)[1]
                    return message_types.message_send_hero_card(session_id, hc_id)
                else:
                    return message_types.message_payload(text_to_process, session_id)
