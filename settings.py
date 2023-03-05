import os
from os.path import dirname, join

from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path)

BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")
ALARM_TEXT = "Пора оплатить VPS!!!"
INFO_TEXT = "VPS функционирует"
NOTIFY_TEXT = "Подписка Лысого закончилась"
