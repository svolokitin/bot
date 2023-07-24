import os
import asyncio
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types
from aiogram.types.web_app_info import WebAppInfo
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup



load_dotenv()
BOT_TOKEN = os.environ.get("BOT_TOKEN")

bot = Bot(BOT_TOKEN)
dispatcher = Dispatcher(bot)


@dispatcher.message_handler(commands=["start"])
async def start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(types.KeyboardButton('Assoleworms Quiz', web_app=WebAppInfo(url='https://svolokitin.github.io/bot-assoleworms/')))

    await message.answer(f"Привет, {message.from_user.full_name}!", reply_markup=keyboard)


async def main():
    await dispatcher.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
