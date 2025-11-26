from telegram import Update
from telegram.ext import ContextTypes
from .base_info import BaseInfo

class DiskHandler(BaseInfo):
    async def disk_Handler(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        content = self.disk()
        print(content)
        msg = "<b>DISK INFO:</b>\n" + "\n".join(content)
        await update.message.reply_text(msg, parse_mode="HTML")