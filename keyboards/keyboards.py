from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder


# Инициализируем билдер
kb_builder = ReplyKeyboardBuilder()

# Создаем кнопки
start_btn = KeyboardButton(text='/start')
help_btn = KeyboardButton(text='/help')

# Добавляем кнопки в билдер
kb_builder.row(start_btn, help_btn, width=1)

# Создаем объект клавиатуры
keyboard_start: ReplyKeyboardMarkup = kb_builder.as_markup(
    resize_keyboard=True,
    one_time_keyboard=True
)