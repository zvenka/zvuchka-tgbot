from user_manager import user_exists, is_user_activated

from .activation import handle_activation
from .activated import handle_activated_message


async def handle_message(update, context):
    user_id = str(update.message.chat_id)

    if not user_exists(user_id):
        return

    if is_user_activated(user_id):
        await handle_activated_message(update, context)
    else:
        await handle_activation(update, context)