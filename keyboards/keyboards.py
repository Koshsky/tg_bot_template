from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from lexicon import lexicon_buttons


# Инициализируем билдер
kb_builder = ReplyKeyboardBuilder()

# Создаем кнопки
btn1 = KeyboardButton(text=lexicon_buttons['ru']['button_1'])
btn2 = KeyboardButton(text=lexicon_buttons['ru']['button_2'])

# Добавляем кнопки в билдер
kb_builder.row(btn1, btn2, width=1)

# Создаем объект клавиатуры
keyboard_start: ReplyKeyboardMarkup = kb_builder.as_markup(
    resize_keyboard=True,
    one_time_keyboard=True
)