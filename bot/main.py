import logging
from telegram.ext import ApplicationBuilder
from config import BOT_TOKEN
from handlers import setup_handlers

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

def main() -> None:
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    setup_handlers(app)
    app.run_polling()

def tests():
    return "hola"

if __name__ == "__main__":
    main()