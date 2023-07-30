import asyncio
import logging

from aiogram import Bot, Dispatcher, F
from aiogram.fsm.storage.redis import RedisStorage, Redis

from config_data.config import Config, load_config
from handlers import admin_handlers, user_handlers, other_handlers, user_actions
from keyboards.set_menu import set_main_menu
from middlewares.trottling import ThrottlingMiddleware


logger = logging.getLogger(__name__)

async def main() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
               '[%(asctime)s] - %(name)s - %(message)s')

    logger.info('Starting bot')


    config: Config = load_config()

    bot: Bot = Bot(token=config.tg_bot.token,
                   parse_mode='HTML')
    redis: Redis = Redis(host=config.redis.host)
    storage: RedisStorage = RedisStorage(redis=redis)

    dp: Dispatcher = Dispatcher(storage=storage)

    dp.middleware.setup(ThrottlingMiddleware())

    dp.include_router(user_actions.router)
    dp.include_router(admin_handlers.router)
    dp.include_router(user_handlers.router)
    dp.include_router(other_handlers.router)

    await set_main_menu(bot)

    await bot.delete_webhook(drop_pending_updates=True)  # УБРАТЬ, если бот работает с платежами
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())