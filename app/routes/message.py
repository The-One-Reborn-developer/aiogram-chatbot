from aiogram import Router, F


message_router = Router()


@message_router.message(F.text)
async def message(message):
    pass