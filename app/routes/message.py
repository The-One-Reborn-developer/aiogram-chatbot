import logging

from aiogram import Router, F

from app.views.message import model_response
from app.views.message import waiting_for_response

from app.scripts.delete_message import delete_message


message_router = Router()


@message_router.message(F.text)
async def message(message):
    waiting_message = await message.answer(waiting_for_response(), parse_mode='HTML')

    response = model_response(message)

    logging.info(f'Deleting waiting message: {waiting_message.message_id}, chat: {message.chat.id}')
    try:
        await delete_message(message.chat.id, waiting_message.message_id)
    except Exception as e:
        logging.log(logging.ERROR, e)

    await message.answer(response, parse_mode='MARKDOWN')