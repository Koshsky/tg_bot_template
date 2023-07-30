from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from lexicon.lexicon_ru import BUTTONS


kb_builder = ReplyKeyboardBuilder()

btn1 = KeyboardButton(text=BUTTONS['button_1'])
btn2 = KeyboardButton(text=BUTTONS['button_2'])

kb_builder.row(btn1, btn2, width=1)

keyboard_start: ReplyKeyboardMarkup = kb_builder.as_markup(
    resize_keyboard=True,
    one_time_keyboard=True
)