from aiogram import types, Router
from aiogram.filters import CommandStart
from app.models.user import User

command_handler = Router()


@command_handler.message(CommandStart())
async def cmd_start(message: types.Message):
    if not message.from_user:
        return
    
    user, created = await User.get_or_create(id=message.from_user.id, defaults={
        "first_name": message.from_user.first_name or '',
        "last_name": message.from_user.last_name or '',
        "is_premium": message.from_user.is_premium or False,
    })

    await message.answer(f"Hello, {user.full_name}!")
    await message.answer("Hello! I'm your OpenAI-powered chatbot. Send me a message, and I'll generate a response for you.")
    # reply = "Hello! I'm your OpenAI-powered chatbot. Send me a message, and I'll generate a response for you."
    # await message.answer(reply)
    # history[message.from_user.id].clear()  # type: ignore
    # history[message.from_user.id].extend([  # type: ignore
    #     {"role": "system", "content": "You are a helpful assistant."},
    #     {"role": "assistant", "content": reply},
    # ])


# @dp.message()
# async def echo(message: types.Message):
#     user_input = message.text
#     # if not user_input:
#     #     return
#     # history[message.from_user.id].append(  # type: ignore
#     #     {"role": "user", "content": user_input})
#     # response = await client.chat.completions.create(
#     #     messages=history[message.from_user.id],  # type: ignore
#     #     model="gpt-3.5-turbo",
#     # )

#     # await message.answer(str(response.choices[0].message.content), parse_mode=ParseMode.MARKDOWN)
    
