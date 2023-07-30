from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

from lexicon.lexicon_ru import BOT_ANSWER
from filters.is_admin import IsAdmin


router: Router = Router()
router.message.filter(IsAdmin())
