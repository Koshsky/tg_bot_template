from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

from lexicon.lexicon_ru import LEXICON_RU
from filters.is_admin import IsAdmin


# Инициализируем роутер уровня модуля и вешаем фильтры
router: Router = Router()
router.message.filter(IsAdmin())

# Даллее хэндлеры:
#
