from telegram import Update
from telegram.ext import ContextTypes
from bot.handlers.base_info import BaseInfo

class DiskInfo(BaseInfo):
    async def disk_info(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        content = self.cpuinfo()
        msg = "<b>DISK INFO:</b>\n" + "\n".join(content)
        await update.message.reply_text(msg, parse_mode="HTML")