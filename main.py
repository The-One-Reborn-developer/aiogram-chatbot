import os
import asyncio

from dotenv import load_dotenv, find_dotenv

from aiogram import Bot, Dispatcher

from app.routes.start import start_router
from app.routes.message import message_router


async def main():
    load_dotenv(find_dotenv())

    bot = Bot(token=os.getenv("TELEGRAM_BOT_TOKEN"))
    dp = Dispatcher()

    dp.include_routers(
        start_router,
        message_router
    )

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())