import os
import aiohttp


async def delete_message(chat_id, message_id):
    url = f"https://api.telegram.org/bot{os.getenv('TELEGRAM_BOT_TOKEN')}/deleteMessage?chat_id={chat_id}&message_id={message_id}"

    await aiohttp.ClientSession().post(url)