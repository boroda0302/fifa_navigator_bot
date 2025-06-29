
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils import executor
import asyncio
import json
import random

API_TOKEN = "YOUR_BOT_TOKEN_HERE"

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Загрузка клубов и челленджей
with open("data/fifa_clubs.json", "r", encoding="utf-8") as f:
    clubs = json.load(f)

with open("data/challenges.json", "r", encoding="utf-8") as f:
    challenges = json.load(f)

# Главное меню
main_kb = ReplyKeyboardMarkup(resize_keyboard=True)
main_kb.add(KeyboardButton("🎮 Начать карьеру"))
main_kb.add(KeyboardButton("🎲 Случайный старт"), KeyboardButton("🔥 Челлендж дня"))
main_kb.add(KeyboardButton("📜 История успеха"), KeyboardButton("🧠 AI Навигатор (в разработке)"))

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer("Привет! Я — FIFA Карьерный Навигатор ⚽
Выбери опцию ниже:", reply_markup=main_kb)

@dp.message_handler(lambda msg: msg.text == "🎲 Случайный старт")
async def random_start(message: types.Message):
    club = random.choice(clubs)
    response = (
        f"🎲 **Твоя судьба:**
"
        f"🏟️ Клуб: {club['name']} ({club['league']})
"
        f"💰 Бюджет: {club['budget']}$
"
        f"🎯 Стиль игры: {club['style']}
"
        f"📌 Нужны игроки: {', '.join(club['needs'])}"
    )
    await message.answer(response, parse_mode="Markdown")

@dp.message_handler(lambda msg: msg.text == "🔥 Челлендж дня")
async def challenge(message: types.Message):
    challenge = random.choice(challenges)
    if challenge["type"] == "player":
        msg = (
            f"🔥 Челлендж игрока:
"
            f"🏟️ Клуб: {challenge['club']}
"
            f"📊 Старт рейтинг: {challenge['start_rating']}
"
            f"🎯 Цель: {challenge['goal']}"
        )
    else:
        msg = (
            f"🔥 Челлендж менеджера:
"
            f"🏟️ Клуб: {challenge['club']}
"
            f"💼 Задача: {challenge['goal']}
"
            f"🎚️ Сложность: {challenge['difficulty']}"
        )
    await message.answer(msg)

@dp.message_handler(lambda msg: msg.text == "📜 История успеха")
async def story(message: types.Message):
    await message.answer("📖 История: Игрок начинал в Ligue 2, стал звездой Реала. (Это демо, будет на базе сейвов)")

@dp.message_handler(lambda msg: msg.text == "🎮 Начать карьеру")
async def start_career(message: types.Message):
    await message.answer("⚙️ Выбери режим карьеры:
(в следующей версии будет выбор позиции/клуба)")

@dp.message_handler(lambda msg: msg.text == "🧠 AI Навигатор (в разработке)")
async def ai_nav(message: types.Message):
    await message.answer("🧠 В будущем ты сможешь просто написать: 'Хочу карьеру как у Холланда', и я всё сделаю сам!")

if __name__ == "__main__":
    print("Бот запущен...")
    executor.start_polling(dp, skip_updates=True)
