import os

BOT_TOKEN = os.getenv("BOT_TOKEN2", "")
if not BOT_TOKEN:
    raise RuntimeError("BOT_TOKEN not set in environment.")
API_URL = "https://api.telegram.org/bot" + BOT_TOKEN + "/"