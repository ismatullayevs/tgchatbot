from .models.message import Message


async def get_history(message, chat_id: int):
    history = []

    while message:
        msg = {'role': message.role, 'content': message.text}
        history.insert(0, msg)
        message = await Message.filter(id=message.replied_to_id, chat_id=chat_id).first()
    
    return history
