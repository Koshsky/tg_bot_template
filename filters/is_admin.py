from aiogram.filters import BaseFilter
from aiogram.types import Message

from config_data.config import load_config


class IsAdmin(BaseFilter):
    async def __call__(self, message: Message):
        return message.from_user.id in load_config().tg_bot.admin_ids
