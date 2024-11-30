from aiogram import Router, F

from app.views.message import model_response
from app.views.message import waiting_for_response


message_router = Router()


@message_router.message(F.text)
async def message(message):
    response = model_response(message)

    await message.answer(waiting_for_response(), parse_mode='HTML')

    await message.answer(response, parse_mode='HTML')