from aiogram import Router
from aiogram.types import Message

from lexicon import lexicon
from keyboards import keyboards


# Инициализируем роутер уровня модуля
router: Router = Router()


# Этот хэндлер срабатывает всегда
@router.message()
async def process_help_command(message: Message):
    await message.answer(text=lexicon['ru']['other'])