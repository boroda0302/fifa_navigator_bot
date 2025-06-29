
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils import executor
import asyncio
import json
import random

API_TOKEN = "8087703446:AAEyCvWvjRAkwUhEgAB2YmqDaeajS3KAKBg"

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Загрузка клубов и челленджей
with open("data/fifa_clubs.json", "r", encoding="utf-8") as f:
    clubs = json.load(f)

with open("data/challenges.json", "r", encoding="utf-8") as f:
    challenges = json.load(f)

# Главное меню
main_kb = ReplyKeyboardMarkup(resize_keyboard=True)
KeyboardButton("🌐 Mini App", web_app=WebAppInfo(url="https://your-hosted-mini-app.com"))
main_kb.add(KeyboardButton("🎲 Случайный старт"), KeyboardButton("🔥 Челлендж дня"))
main_kb.add(KeyboardButton("📜 История успеха"), KeyboardButton("🧠 AI Навигатор (в разработке)"))

@dp.message_handler(content_types=["web_app_data"])
async def handle_web_app(message: types.Message):
    data = json.loads(message.web_app_data.data)
    position = data["position"]
    style = data["style"]
    level = data["level"]
    clubs = recommend_clubs(player_position=position, style=style, level=level)
    if not clubs:
        await message.answer("❌ Не удалось найти клуб. Попробуй снова.")
        return
    club = random.choice(clubs)
    response = (
        f"🎯 Карьера по твоим параметрам:\n"
        f"🏟️ {club['name']} ({club['league']})\n"
        f"🧠 Стиль: {club['style']}\n"
        f"💰 Бюджет: {club['budget']}$"
    )
    await message.answer(response)

def recommend_clubs(player_position=None, style=None, level=None):
    from data import fifa_clubs  # если у тебя клубы в отдельном модуле
    # или просто: clubs = загрузка из data/fifa_clubs.json

    with open("data/fifa_clubs.json", "r", encoding="utf-8") as f:
        clubs = json.load(f)

    result = []
    for club in clubs:
        if style and club["style"] != style:
            continue
        if player_position and player_position not in club.get("needs", []):
            continue
        if level:
            if level == "high" and club["budget"] < 50000000:
                continue
            if level == "mid" and not (10000000 <= club["budget"] <= 50000000):
                continue
            if level == "low" and club["budget"] > 10000000:
                continue
        result.append(club)
    return result

{
  "name": "Arsenal",
  "league": "Premier League",
  "budget": 75000000,
  "style": "possession",
  "needs": ["ST", "CB"]
}


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
