from helpers import datetime_now_iso


def message_payload(message, session_id):
    return {
        "activity": "Text",
        "timestamp": datetime_now_iso(),
        "text": message,
        "sessionId": session_id,
        "language": "cs",
        "source": "Default"
    }


def message_get_available_operators(session_id):
    return {
        "activity": "GetAvailableOperators",
        "sessionId": session_id
    }


def message_get_available_groups(session_id):
    return {
        "activity": "GetAvailableGroups",
        "sessionId": session_id
    }


def message_get_call_params(session_id):
    return {
        "activity": "GetCallParams",
        "sessionId": session_id
    }


def message_set_call_params(session_id, call_params):
    return {
        "activity": "SetCallParams",
        "sessionId": session_id,
        "callParams": call_params
    }


def message_get_guest_identity(session_id):
    return {
        "activity": "GetGuestIdentity",
        "sessionId": session_id
    }


def message_hand_off(session_id):
    return {
        "activity": "HandOff",
        "sessionId": session_id
    }


def message_end_conversation(session_id):
    return {
        "activity": "EndConversation",
        "sessionId": session_id
    }


def message_typing(session_id, show):
    return {
        "activity": "Typing",
        "sessionId": session_id,
        "show": show
    }


def message_disable_guest_input(session_id):
    return {
        "activity": "DisableGuestInput",
        "sessionId": session_id
    }


def message_enable_guest_input(session_id):
    return {
        "activity": "EnableGuestInput",
        "sessionId": session_id
    }


def message_get_hero_cards(session_id):
    return {
        "activity": "GetHeroCards",
        "sessionId": session_id,
    }


def message_send_hero_card(session_id, hero_card_id):
    return {
        "activity": "SendHeroCard",
        "sessionId": session_id,
        "heroCardId": hero_card_id
    }


def message_chatbot_open_file_upload_prompt(session_id):
    return {
        "activity": "ChatbotOpenFileUploadPrompt",
        "sessionId": session_id
    }


def message_enable_guest_upload(session_id):
    return {
        "activity": "EnableGuestUpload",
        "sessionId": session_id
    }


def message_disable_guest_upload(session_id):
    return {
        "activity": "DisableGuestUpload",
        "sessionId": session_id
    }


def message_carousel(session_id):
    return {
        "sessionId": session_id,
        "type": "message",
        "timestamp": datetime_now_iso(),
        "attachmentLayout": "carousel",
        "attachments": [
            {
                "contentType": "application/vnd.microsoft.card.hero",
                "content": {
                    "title": "Street #1",
                    "subtitle": "1. Street Foo 254 Czechia",
                    "images": [
                        {
                            "url": "https://dev.virtualearth.net/REST/V1/Imagery/Map/Road?form=BTCTRL&mapArea=49"
                                   ".7463607788086,13.1083498001099,49.7932815551758,13.1951398849487&mapSize=500,"
                                   "280&pp=49.7616882324219,"
                                   "13.1491804122925;1;1&dpi=1&logo=always&key=ApBn8xoItlENbFx"
                                   "-rr1kzt_JakWdFTH24taCasYxQCgit15NtDeYrztO4chDtrg5"
                        }
                    ],
                    "buttons": [
                        {
                            "type": "imBack",
                            "title": "Street Foo 254",
                            "value": 1
                        }
                    ]
                }
            },
            {
                "contentType": "application/vnd.microsoft.card.hero",
                "content": {
                    "title": "Street #2",
                    "subtitle": "1. Ulice, Plzeň, Czechia",
                    "images": [
                        {
                            "url": "https://dev.virtualearth.net/REST/V1/Imagery/Map/Road?form=BTCTRL&mapArea=49"
                                   ".7463607788086,13.1083498001099,49.7932815551758,13.1951398849487&mapSize=500,"
                                   "280&pp=49.7616882324219,"
                                   "13.1491804122925;1;1&dpi=1&logo=always&key=ApBn8xoItlENbFx"
                                   "-rr1kzt_JakWdFTH24taCasYxQCgit15NtDeYrztO4chDtrg5"
                        }
                    ],
                    "buttons": [
                        {
                            "type": "imBack",
                            "title": "Ulice, Plzeň, Czechia",
                            "value": 1
                        }
                    ]
                }
            },
            {
                "contentType": "application/vnd.microsoft.card.hero",
                "content": {
                    "title": "Street #2 again",
                    "subtitle": "1. Ulice, Plzeň, Czechia",
                    "images": [
                        {
                            "url": "https://dev.virtualearth.net/REST/V1/Imagery/Map/Road?form=BTCTRL&mapArea=49"
                                   ".7463607788086,13.1083498001099,49.7932815551758,13.1951398849487&mapSize=500,"
                                   "280&pp=49.7616882324219,"
                                   "13.1491804122925;1;1&dpi=1&logo=always&key=ApBn8xoItlENbFx"
                                   "-rr1kzt_JakWdFTH24taCasYxQCgit15NtDeYrztO4chDtrg5"
                        }
                    ],
                    "buttons": [
                        {
                            "type": "imBack",
                            "title": "Ulice, Plzeň, Czechia",
                            "value": 1
                        }
                    ]
                }
            }
        ]
    }


def message_buttons(session_id):
    return {
        "type": "message",
        "sessionId": session_id,
        "timestamp": datetime_now_iso(),
        "attachments": [
            {
                "contentType": "application/vnd.microsoft.card.hero",
                "content": {
                    "title": "Test buttons",
                    "buttons": [
                        {
                            "type": "imBack",
                            "title": "Title of the first button",
                            "value": "Value of the first button"
                        },
                        {
                            "type": "imBack",
                            "title": "Title of the second button",
                            "value": "Value of the second button"
                        }
                    ]
                }
            }
        ]
    }


def message_hello(session_id):
    return {
        "sessionId": session_id,
        "activity": "Text",
        "text": "Hello world"
    }


def send_image(session_id):
    return {
        "sessionId": session_id,
        "activity": "Text",
        "text": "https://upload.wikimedia.org/wikipedia/commons/9/9a/Gull_portrait_ca_usa.jpg"
    }


def send_youtube_video(session_id):
    return {
        "sessionId": session_id,
        "activity": "Text",
        "text": "https://www.youtube.com/watch?v=DQFKmzUhQg8&ab_channel=mluvii"
    }


def send_mp4_video(session_id):
    return {
        "sessionId": session_id,
        "activity": "Text",
        "text": "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4"
    }


def get_media_objects(session_id):
    return {
        "sessionId": session_id,
        "activity": "GetMediaObjects",
    }
