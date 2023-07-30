from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from lexicon.lexicon_ru import BUTTONS


def create_inline_kb(width: int,
                     *args: str,
                     **kwargs: str) -> InlineKeyboardMarkup:

    kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()

    buttons: list[InlineKeyboardButton] = []

    for button in args:
        buttons.append(InlineKeyboardButton(
            text=BUTTONS[button] if button in BUTTONS else button,
            callback_data=button))

    for button, text in kwargs.items():
        buttons.append(InlineKeyboardButton(
            text=text,
            callback_data=button))

    kb_builder.row(*buttons, width=width)

    return kb_builder.as_markup()