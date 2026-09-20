import random

CHECK_RESPONSES = [
    ("Да-да?! Что-то качаем? ✨", 15),
    ("Всё под контролем, шеф! 👍✨", 12),
    ("Я тут! Заряжена на полную мощность 🔋✨", 15),
    ("Всё ещё здесь, к твоим услугам :3", 12),
    ("Хе-хе, проверка связи прошла успешно! 📶", 7),
    ("Тут я, тут... Просто трек выбирала 🎶", 7),
    ("А..? Что? Я не сплю! 👀", 5),
    ("М-м? Ну чего ты тыкаешь, работаю я! 🥱", 3),
    ("Тут я. И вовсе я не ленивая, я энергосберегающая! 🥱", 3),
    ("М-м? Запуталась в проводах... 🎧🕸️", 3)
]

async def check(update, context):

    responses = [text for text, weight in CHECK_RESPONSES]
    weights = [weight for text, weight in CHECK_RESPONSES]

    response = random.choices(responses, weights=weights, k=1)[0]

    await update.message.reply_text(response)