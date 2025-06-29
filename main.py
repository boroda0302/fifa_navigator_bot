import os
import json
import random
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo
from aiogram.utils import executor

BOT_TOKEN = os.getenv("BOT_TOKEN")  # Секретный токен из Render Environment

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

# Мини-клавиатура с кнопками
kb = ReplyKeyboardMarkup(resize_keyboard=True)
kb.add(KeyboardButton("🎮 Карьера игрока"))
kb.add(KeyboardButton("🌐 Mini App", web_app=WebAppInfo(url="https://fifa-navigator-bot.onrender.com")))

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer("Привет! Выбери действие ниже 👇", reply_markup=kb)

@dp.message_handler(lambda msg: msg.text == "🎮 Карьера игрока")
async def player(message: types.Message):
    positions = ["ST", "CM", "CB", "GK"]
    clubs = ["Arsenal", "Barcelona", "Juventus", "Ajax"]
    rating = random.randint(60, 80)
    await message.answer(f"🧍 Позиция: {random.choice(positions)}\n🏟️ Клуб: {random.choice(clubs)}\n🔢 Рейтинг: {rating}")

@dp.message_handler(content_types=["web_app_data"])
async def handle_web_app(message: types.Message):
    data = json.loads(message.web_app_data.data)
    await message.answer(f"✅ Mini App данные:\nПозиция: {data['position']}\nСтиль: {data['style']}\nУровень: {data['level']}")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
