from aiogram import types, Router, F
from aiogram.enums import ParseMode
from app.models.user import User
from app.models.message import Message
from app.bot.utils import get_history, escape_characters
from config.settings import settings
from app.openai import client


message_handler = Router()


@message_handler.message(F.text)
async def prompt(message: types.Message):
    assert message.from_user is not None
    user = await User.get(id=message.from_user.id).select_related('last_message')

    reply_id = message.reply_to_message.message_id if message.reply_to_message else user.last_message.message_id if user.last_message else None
    reply = await Message.get_or_none(message_id=reply_id, chat_id=message.chat.id)
    history = await get_history(reply, message.chat.id) if reply else []

    MX = settings.MAX_HISTORY
    if MX and len(history) >= MX:
        return await message.answer(f"Sorry, your conversation history is too long ({MX} messages). Please start a /newchat.")

    history.append({"role": "user", "content": message.text})
    if settings.SYSTEM_MESSAGE:
        history.insert(
            0, {"role": "system", "content": settings.SYSTEM_MESSAGE})

    response = client.chat.completions.create(
        messages=history,
        model='gpt-3.5-turbo',
    )
    response_text = response.choices[0].message.content
    if not response_text:
        return

    response_msg = await message.answer(escape_characters(response_text), parse_mode=ParseMode.MARKDOWN_V2)

    msg = await Message.create(message_id=message.message_id, chat_id=message.chat.id,
                               text=message.text, role='user', replied_to=reply)

    resp = await Message.create(message_id=response_msg.message_id, chat_id=message.chat.id,
                                text=response_text, role='assistant', replied_to=msg)

    user.last_message = resp
    await user.save()
