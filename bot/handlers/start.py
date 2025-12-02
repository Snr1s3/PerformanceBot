from telegram import Update
from telegram.ext import ContextTypes


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    welcome_message = f"Hi, I'm your personal virtual assistant!\nHow can I assist you today?"
    await update.message.reply_text(welcome_message)
