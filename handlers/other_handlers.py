from aiogram import Router
from aiogram.types import Message

from lexicon.lexicon_ru import LEXICON_RU
from keyboards import keyboards


# Инициализируем роутер уровня модуля
router: Router = Router()


# Этот хэндлер срабатывает всегда
@router.message()
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_RU['other'])