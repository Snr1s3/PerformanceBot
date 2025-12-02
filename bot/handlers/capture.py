from telegram import Update
from telegram.ext import ContextTypes

from .base_info import BaseInfo


class CaptureHandler(BaseInfo):
    async def capture_Handler(
        self, update: Update, context: ContextTypes.DEFAULT_TYPE
    ) -> None:
        msg = "<b>Capturing Server Status</b>"
        filename = self.capture()
        await self.send_long_message(msg, update, parse_mode="HTML")

        with open(filename, 'rb') as f:
            await update.message.reply_document(f, filename=filename)
