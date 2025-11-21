from telegram import Update
from telegram.ext import ContextTypes
from bot.handlers.base_info import BaseInfo

class NetworkHandler(BaseInfo):
    async def network_Handler(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        content = self.network()
        msg = "<b>NETWORK INFO:</b>\n" + "\n".join(content)
        await update.message.reply_text(msg, parse_mode="HTML")