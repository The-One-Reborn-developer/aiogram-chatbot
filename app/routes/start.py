from aiogram import Router
from aiogram.filters import CommandStart

from app.views.start import start_command


start_router = Router()


@start_router.message(CommandStart())
async def start(message):
    content = start_command(message)

    await message.answer(content, parse_mode='HTML')