from telegram import Update
from telegram.ext import ContextTypes
from .base_info import BaseInfo

class NetworkHandler(BaseInfo):
    async def network_Handler(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        content = self.network()
        msg = "<b>NETWORK INFO:</b>\n" + "\n".join(content)
        await self.send_long_message(msg, update, parse_mode="HTML")