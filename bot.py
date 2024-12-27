import asyncio
from aiogram import Bot, Dispatcher
from handlers import questions, group_games, usernames
import config

async def main():
    bot = Bot(token=config.token)
    dp = Dispatcher()

    dp.include_routers(questions.router)
    dp.include_router(group_games.router)
    dp.include_router(usernames.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())