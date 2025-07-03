import os
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils import executor

# 🔐 Безопасно получаем токен из окружения
BOT_TOKEN = os.getenv("8087703446:AAEyCvWvjRAkwUhEgAB2YmqDaeajS3KAKBg)

OWNER_ID = 693452733 https://t.me/kny4zhestvo

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

# 🧭 Клавиатура
kb = ReplyKeyboardMarkup(resize_keyboard=True)
kb.add(KeyboardButton("⚽ Начать карьеру"))

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    if message.from_user.id != OWNER_ID:
        await message.answer("❌ У тебя нет доступа к этому боту.")
        return

    await message.answer("Привет, хозяин! Выбери действие:", reply_markup=kb)

@dp.message_handler(lambda msg: msg.text == "⚽ Начать карьеру")
async def generate_career(message: types.Message):
    await message.answer("🎮 Ты начинаешь карьеру в клубе Arsenal с рейтингом 72.")

if __name__ == "__main__":
    print("✅ Бот запущен.")
    executor.start_polling(dp, skip_updates=True)
