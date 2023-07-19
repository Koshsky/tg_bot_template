from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

from lexicon import lexicon_commands
from filters.is_admin import IsAdmin


# Инициализируем роутер уровня модуля и вешаем фильтры
router: Router = Router()
router.message.filter(IsAdmin())

# Даллее хэндлеры:
#
# @router.message(CommandStart())
# async def process_start_command(message: Message):
#     await message.answer(text=lexicon_commands['ru']['/start'])