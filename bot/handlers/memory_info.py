from telegram import Update
from telegram.ext import ContextTypes
from bot.handlers.base_info import BaseInfo

class MemoryInfo(BaseInfo):
    async def memory_info(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        content = self.memoryinfo()
        msg = "<b>MEMORY INFO:</b>\n" + "\n".join(content)
        await update.message.reply_text(msg, parse_mode="HTML")