from .lexicon_en import LEXICON_BUTTONS_EN, LEXICON_COMMANDS_EN, LEXICON_EN
from .lexicon_ru import LEXICON_BUTTONS_RU, LEXICON_COMMANDS_RU, LEXICON_RU


if set(LEXICON_BUTTONS_EN) != set(LEXICON_BUTTONS_RU):
    raise ValueError('LEXICON_BUTTONS_EN НЕ ПОДОБЕН LEXICON_BUTTONS_RU')

if set(LEXICON_COMMANDS_RU) != set(LEXICON_COMMANDS_EN):
    raise ValueError('LEXICON_COMMANDS_RU НЕ ПОДОБЕН LEXICON_COMMANDS_EN')

if set(LEXICON_EN) != set(LEXICON_RU):
    raise ValueError('LEXICON_EN НЕ ПОДОБЕН LEXICON_RU')


lexicon_buttons = {
    'ru': LEXICON_BUTTONS_RU,
    'en': LEXICON_BUTTONS_EN
}

lexicon_commands = {
    'ru': LEXICON_COMMANDS_RU,
    'en': LEXICON_COMMANDS_EN
}

lexicon = {
    'ru': LEXICON_RU,
    'en': LEXICON_EN
}