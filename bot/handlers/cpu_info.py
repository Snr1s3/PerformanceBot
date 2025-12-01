from telegram import Update
from telegram.ext import ContextTypes

from .base_info import BaseInfo

class CpuHandler(BaseInfo):
    async def cpu_Handler(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        content = self.cpu()
        chat = update.effective_chat
        info = (
            f"Chat ID: {chat.id}\n"
            f"Type: {chat.type}\n"
            f"Title: {chat.title}\n"
            f"Username: {chat.username}\n"
        )
        print(info)
        msg = "<b>CPU INFO:</b>\n" + "\n".join(content)
        await self.send_long_message(msg, update, parse_mode="HTML")