from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

from lexicon.lexicon_ru import BOT_ANSWER
from keyboards import keyboards


router: Router = Router()

@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text=BOT_ANSWER['/start'], reply_markup=keyboards.keyboard_start)

@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(text=BOT_ANSWER['/help'])