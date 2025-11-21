from telegram import Update
from telegram.ext import ContextTypes
from bot.handlers.base_info import BaseInfo

class SystemInfo(BaseInfo):
    async def system_info(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        content = self.systeminfo()
        msg = "<b>SYSTEM INFO:</b>\n" + "\n".join(content)
        await update.message.reply_text(msg, parse_mode="HTML")