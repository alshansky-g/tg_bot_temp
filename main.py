import asyncio
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
import game_handlers
import command_handlers
from models import init_models
from config import settings


async def main():
    await init_models()
    bot = Bot(token=settings.BOT_TOKEN,
              default=DefaultBotProperties(parse_mode='HTML'))
    dp = Dispatcher()

    dp.include_router(command_handlers.command_router)
    dp.include_router(game_handlers.game_router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


try:
    asyncio.run(main())
except KeyboardInterrupt:
    print('Бот остановлен')
