import asyncio
import os

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart, Command
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message):
    print("Получен /start от:", message.from_user.id)
    await message.answer("Добро пожаловать!")

@dp.message(Command("bagivs"))
async def say_hello(message):
    print("Получен /bagivs от:", message.from_user.id)
    await message.answer("Привет! 👋")

async def main():
    me = await bot.get_me()
    print("Бот запущен:", me.username)

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
