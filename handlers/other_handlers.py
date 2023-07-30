from aiogram import Router
from aiogram.types import Message

from lexicon.lexicon_ru import BOT_ANSWER
from keyboards import keyboards


router: Router = Router()


@router.message()
async def process_help_command(message: Message):
    await message.answer(text=BOT_ANSWER['other'])