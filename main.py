import os
import asyncio
import logging

from dotenv import load_dotenv, find_dotenv

from aiogram import Bot, Dispatcher

from app.routes.start import start_router
from app.routes.message import message_router


async def main():
    try:
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )

        logging.info("Loading environment variables")
        load_dotenv(find_dotenv())

        logging.info("Starting bot")
        bot = Bot(token=os.getenv("TELEGRAM_BOT_TOKEN"))
        dp = Dispatcher()

        logging.info("Starting polling")
        await bot.delete_webhook(drop_pending_updates=True)

        dp.include_routers(
            start_router,
            message_router
        )

        await dp.start_polling(bot)
    except Exception as e:
        logging.log(logging.ERROR, e)
        exit(1)


if __name__ == "__main__":
    asyncio.run(main())