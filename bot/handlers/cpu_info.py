from telegram import Update
from telegram.ext import ContextTypes

from bot.handlers.base_info import BaseInfo

class CpuHandler(BaseInfo):
    async def cpu_Handler(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        content = self.system()
        msg = "<b>CPU INFO:</b>\n" + "\n".join(content)
        await update.message.reply_text(msg, parse_mode="HTML")