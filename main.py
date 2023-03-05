import asyncio
import logging
from datetime import datetime

from aiogram import Bot, Dispatcher
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from handlers.apsched import send_notify
from settings import ALARM_TEXT, BOT_TOKEN, CHAT_ID, INFO_TEXT, NOTIFY_TEXT

logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN, parse_mode="HTML")

dp = Dispatcher()


async def main():
    scheduler = AsyncIOScheduler(timezone="Europe/Moscow")
    scheduler.add_job(
        send_notify,
        trigger="cron",
        start_date=datetime(year=2023, month=1, day=1),
        day=15,
        hour=10,
        kwargs={"chat_id": CHAT_ID, "text": ALARM_TEXT, "bot": bot},
    )
    scheduler.add_job(
        send_notify,
        trigger="cron",
        start_date=datetime(year=2023, month=1, day=1),
        hour=9,
        kwargs={"chat_id": CHAT_ID, "text": INFO_TEXT, "bot": bot},
    )
    scheduler.add_job(
        send_notify,
        trigger="cron",
        start_date=datetime(year=2023, month=3, day=1),
        end_date=datetime(year=2024, month=1, day=1),
        month=12,
        kwargs={"chat_id": CHAT_ID, "text": NOTIFY_TEXT, "bot": bot},
    )
    scheduler.start()
    print(scheduler.print_jobs())
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
