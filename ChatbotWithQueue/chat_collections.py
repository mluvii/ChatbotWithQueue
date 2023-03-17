from collections import defaultdict

d = defaultdict(list)


def get_session_messages(session_id):
    result = d[session_id]
    print(f'messages array: {result} sesId: {session_id}')
    if result is None:
        return []
    else:
        return result


def append_session_message(session_id, message):
    print(f'ses_id: {session_id} message {message} dict {d[session_id]}')
    d[session_id].append(message)
