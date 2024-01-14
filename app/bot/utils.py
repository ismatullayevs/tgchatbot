from ..models.message import Message


async def get_history(message, chat_id: int):
    history = []

    while message:
        msg = {'role': message.role, 'content': message.text}
        history.insert(0, msg)
        message = await Message.filter(id=message.replied_to_id, chat_id=chat_id).first()
    
    return history


def escape_characters(text: str):
    special_characters = ['_', '*', '[', ']', '(', ')', '~', '`', '>', '#', '+', '-', '=', '|', '{', '}', '.', '!']
    
    escaped_text = ''
    for char in text:
        if char in special_characters:
            escaped_text += '\\' + char
        else:
            escaped_text += char
    
    return escaped_text

