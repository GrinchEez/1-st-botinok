import asyncio
from aiogram import Bot, Dispatcher
from handlers import questions, group_games, usernames


# Запуск бота
async def main():
    bot = Bot(token="8166147397:AAEKC3zSEBciLPl_Fat8G-jDjJtn27SLRoM")
    dp = Dispatcher()

    dp.include_routers(questions.router)
    dp.include_router(group_games.router)
    dp.include_router(usernames.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())