from telegram import Update
from telegram.ext import ContextTypes

from .base_info import BaseInfo

class CpuHandler(BaseInfo):
    async def cpu_Handler(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        msg = self.cpu()
        await self.send_long_message(msg, update, parse_mode="HTML")