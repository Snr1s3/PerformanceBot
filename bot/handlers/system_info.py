from telegram import Update
from telegram.ext import ContextTypes
from .base_info import BaseInfo

class SystemHandler(BaseInfo):
    async def system_Handler(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        content = self.system()
        msg = "<b>SYSTEM INFO:</b>\n" + "\n".join(content)
        await self.send_long_message(msg, update, parse_mode="HTML")