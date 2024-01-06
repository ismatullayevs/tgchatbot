from aiogram import types, Router
from aiogram.filters import CommandStart, Command
from app.models.user import User
from app.models.message import Chat

command_handler = Router()


@command_handler.message(CommandStart())
async def start(message: types.Message):
    assert message.from_user is not None

    user, user_created = await User.update_or_create(id=message.from_user.id, defaults={
        "first_name": message.from_user.first_name or '',
        "last_name": message.from_user.last_name or '',
        "is_premium": message.from_user.is_premium or False,
        "last_message": None
    })
    chat, chat_created = await Chat.get_or_create(id=message.chat.id)
    await message.answer("Hi! How can I help you?")


@command_handler.message(Command("newchat"))
async def new_chat(message: types.Message):
    assert message.from_user is not None
    user = await User.get(id=message.from_user.id)
    user.last_message = None
    await user.save()
    await message.answer("Hi! How can I help you?")
