import asyncio

from downloader.url import is_yt_url
from downloader.youtube import yt_to_mp3

async def handle_activated_message(update, context):

    text = update.message.text

    if not is_yt_url(text):
        await update.message.reply_text(
            "Не совсем поняла тебя... Попробуй прислать ссылку на видео :3"
        )
        return

    path = await asyncio.to_thread(yt_to_mp3, text)

    try:
        await update.message.reply_audio(audio=path)
    finally:
        path.unlink()