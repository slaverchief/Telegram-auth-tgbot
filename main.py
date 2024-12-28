import logging
import asyncio

from aiogram import Dispatcher, Bot
import os
from handlers import basic_router


async def main():
    bot = Bot(token=os.environ.get("TOKEN"))
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s")
    dp = Dispatcher()
    dp.include_router(basic_router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
    