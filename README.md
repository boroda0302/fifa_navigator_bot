
# FIFA Карьерный Навигатор 🤖⚽

Телеграм-бот, который генерирует карьерные сценарии для игроков и менеджеров в стиле EA FC 25.

## 📦 Функции
- 🎮 Карьера игрока и менеджера
- 🎲 Случайный старт
- 🔥 Челлендж дня
- 🧠 AI-навигатор (в разработке)
- 💾 Сохранение прогресса

## 🚀 Запуск

1. Установи зависимости:
```bash
pip install -r requirements.txt
```

2. Добавь переменную окружения:
```bash
export BOT_TOKEN=your_bot_token
```

3. Запусти:
```bash
python main.py
```

## 🌐 Деплой на Render

1. Создай репозиторий на GitHub и запушь туда проект.
2. На [render.com](https://render.com):
   - New → Web Service
   - Подключи репозиторий
   - Укажи:
     - Build Command: `pip install -r requirements.txt`
     - Start Command: `python main.py`
   - В Environment добавь `BOT_TOKEN` (твой Telegram-токен)

---

🧠 Разработано для фанатов карьеры в EA FC. Хочешь внести вклад — открывай PR!
