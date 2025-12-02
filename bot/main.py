from telegram.ext import ApplicationBuilder
from config import BOT_TOKEN
from handlers import setup_handlers


def main() -> None:
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    setup_handlers(app)
    app.run_polling()


if __name__ == "__main__":
    main()
