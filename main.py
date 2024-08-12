import requests
import pprint
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
import asyncio
import os
from dotenv import load_dotenv

load_dotenv()

"""
resp = requests.get("https://stepik.org/api/courses/210064")
resp = resp.json()
pprint.pprint(resp['courses'][0]["learners_count"])
"""

bot = Bot(token=os.getenv("SECRET_KEY"))
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text="Статка"),
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True
    )
    await message.answer("Привет!", reply_markup=keyboard)


@dp.message(F.text == "Статка")
async def with_puree(message: types.Message):
    resp = requests.get("https://stepik.org/api/courses/210064")
    resp = resp.json()
    resp = (resp['courses'][0]["learners_count"])
    await message.answer(f"На курсе {resp} участников")

async def main():
    await dp.start_polling(bot)



if __name__ == "__main__":
    asyncio.run(main(), debug=True)