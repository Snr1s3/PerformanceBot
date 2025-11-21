import os

BOT_TOKEN2 = os.getenv("BOT_TOKEN2", "")
if not BOT_TOKEN2:
    raise RuntimeError("BOT_TOKEN2 not set in environment.")
API_URL = "https://api.telegram.org/bot" + BOT_TOKEN2 + "/"
"""
DB_PSSWD = os.getenv("DB_PSSWD","")
DB_USER = os.getenv("DB_USER","")
DB_URL = os.getenv("DB_URL","")
"""