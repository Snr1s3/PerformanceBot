from telegram import Update
from telegram.ext import ContextTypes
from .base_info import BaseInfo

class SensorsHandler(BaseInfo):
    async def sensors_Handler(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        content = self.sensors()
        msg = "<b>Sensors INFO:</b>\n" + "\n".join(content)
        await update.message.reply_text(msg, parse_mode="HTML")