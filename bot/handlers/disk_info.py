from telegram import Update
from telegram.ext import ContextTypes
from .base_info import BaseInfo

class DiskHandler(BaseInfo):
    async def disk_Handler(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        content = self.disk()
        msg = "<b>DISK INFO:</b>\n" + "\n".join(content)
        await self.send_long_message(msg, update, parse_mode="HTML")