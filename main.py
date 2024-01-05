from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from config.settings import settings
from app.bot.handlers.commands import command_handler
from tortoise import Tortoise
import asyncio
import sys
import logging


logging.basicConfig(level=logging.INFO)

dp = Dispatcher()
dp.include_router(command_handler)


@dp.startup()
async def on_startup(*args, **kwargs):
    await Tortoise.init(config=settings.DB_CONFIG)
    await Tortoise.generate_schemas()


@dp.shutdown()
async def on_shutdown(*args, **kwargs):
    await Tortoise.close_connections()


async def main() -> None:
    bot = Bot(token=settings.BOT_TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
