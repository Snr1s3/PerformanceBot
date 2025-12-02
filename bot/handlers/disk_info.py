from telegram import Update
from telegram.ext import ContextTypes
from .base_info import BaseInfo


class DiskHandler(BaseInfo):
    async def disk_Handler(
        self, update: Update, context: ContextTypes.DEFAULT_TYPE
    ) -> None:
        msg = self.disk()
        await self.send_long_message(msg, update, parse_mode="HTML")
