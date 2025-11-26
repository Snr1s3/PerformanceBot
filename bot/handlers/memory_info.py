from telegram import Update
from telegram.ext import ContextTypes
from .base_info import BaseInfo

class MemoryHandler(BaseInfo):
    async def memory_Handler(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        content = self.memory()
        msg = "<b>MEMORY INFO:</b>\n" + "\n".join(content)
        await self.send_long_message(msg, update, parse_mode="HTML")