from telegram import Update
from telegram.ext import ContextTypes

from .base_info import BaseInfo

class CpuHandler(BaseInfo):
    async def cpu_Handler(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        content = self.cpu()
        msg = "<b>CPU INFO:</b>\n" + "\n".join(content)
        await self.send_long_message(msg, update, parse_mode="HTML")