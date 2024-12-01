import os
import aiohttp
import logging


async def delete_message(chat_id, message_id) -> bool:
    url = f"https://api.telegram.org/bot{os.getenv('TELEGRAM_BOT_TOKEN')}/deleteMessage?chat_id={chat_id}&message_id={message_id}"

    try:
        async with aiohttp.ClientSession() as session:
            await session.post(url)

        return True
    except Exception as e:
        logging.log(logging.ERROR, e)
        return False