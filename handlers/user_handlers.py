from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

from lexicon import lexicon_commands
from keyboards import keyboards


# Инициализируем роутер уровня модуля
router: Router = Router()

# Этот хэндлер срабатывает на команду /start
@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text=lexicon_commands['ru']['/start'], reply_markup=keyboards.keyboard_start)


# Этот хэндлер срабатывает на команду /help
@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(text=lexicon_commands['ru']['/help'])