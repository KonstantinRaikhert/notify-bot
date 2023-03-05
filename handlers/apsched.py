from aiogram import Bot


async def send_notify(chat_id: str, text: str, bot: Bot):
    await bot.send_message(chat_id=chat_id, text=text)
