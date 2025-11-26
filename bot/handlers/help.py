from telegram import Update
from telegram.ext import ContextTypes
from .base_info import BaseInfo

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    msg = (
        "<b>Available Commands:</b>\n"
        "/start - Start the bot\n"
        "/system - Show system info\n"
        "/cpu - Show CPU info\n"
        "/memory - Show memory info\n"
        "/disk - Show disk info\n"
        "/network - Show network info\n"
        "/docker - Show docker info\n"
        "/sensors - Show sensors info\n"
        "/all - Show all info\n"
        "/capture - Sends a json with all the data\n"
        "/help - Show this help message"
    )
    await BaseInfo.send_long_message(msg, update, parse_mode="HTML")