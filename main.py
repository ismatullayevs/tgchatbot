from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from collections import defaultdict
from dotenv import load_dotenv
from openai import AsyncOpenAI
from config.settings import settings

import asyncio
import sys
import logging

load_dotenv()
logging.basicConfig(level=logging.INFO)

dp = Dispatcher()
client = AsyncOpenAI(api_key=settings.OPENAI_API_KEY)
history = defaultdict(list)


@dp.message(CommandStart())
async def cmd_start(message: types.Message):
    reply = "Hello! I'm your OpenAI-powered chatbot. Send me a message, and I'll generate a response for you."
    await message.answer(reply)
    history[message.from_user.id].clear()  # type: ignore
    history[message.from_user.id].extend([  # type: ignore
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "assistant", "content": reply},
    ])


@dp.message()
async def echo(message: types.Message):
    user_input = message.text
    if not user_input:
        return
    history[message.from_user.id].append(  # type: ignore
        {"role": "user", "content": user_input})
    response = await client.chat.completions.create(
        messages=history[message.from_user.id],  # type: ignore
        model="gpt-3.5-turbo",
    )

    await message.answer(str(response.choices[0].message.content), parse_mode=ParseMode.MARKDOWN)


async def main() -> None:
    bot = Bot(token=settings.BOT_TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
