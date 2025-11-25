import logging
from telegram.ext import ApplicationBuilder
from bot.config import BOT_TOKEN
from bot.handlers import setup_handlers

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

def main() -> None:
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    setup_handlers(app)
    app.run_polling()

if __name__ == "__main__":
    main()