from user_manager import (
    user_exists,
    create_user,
    is_user_activated
)


async def start(update, context):
    user_id = str(update.message.chat_id)

    if not user_exists(user_id):

        create_user(user_id)

        await update.message.reply_text(
            "🎧 Привет! Я Звучка — твой персональный медиа-ассистент.\n\n"
            "Умею скачивать музыку с Ютуба, конвертировать файлы и ещё много чего интересного ✨\n\n"
            "Но сначала нужно кое-что проверить 👀\n"
            "Попроси Давида дать тебе код активации и пришли его сюда — и тогда я буду к твоим услугам!"
        )

    elif not is_user_activated(user_id):

        await update.message.reply_text(
            "🔒 Ты ещё не активирован!\n\n"
            "Попроси Давида дать тебе код активации и пришли его сюда."
        )

    else:

        await update.message.reply_text(
            "С возвращением! Я готова к работе ✨"
        )