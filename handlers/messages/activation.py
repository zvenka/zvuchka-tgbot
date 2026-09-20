from user_manager import (
    activate_user
)

async def handle_activation(update, context):
    user_id = str(update.message.chat_id)
    key = update.message.text.strip()

    if activate_user(user_id, key):
        await update.message.reply_text(
            "👀 Всё проверила, ключ верный! ✨"
        )

    else:
        await update.message.reply_text(
            "❌ Неверный ключ. Попробуй ещё раз."
        )