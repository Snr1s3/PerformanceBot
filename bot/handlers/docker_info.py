import html
from telegram import Update
from telegram.ext import ContextTypes
from .base_info import BaseInfo

class DockerHandler(BaseInfo):
    async def docker_Handler(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        msg = self.docker()
        await self.send_long_message(msg, update, parse_mode="HTML")