import html
from telegram import Update
from telegram.ext import ContextTypes
from .base_info import BaseInfo

class DockerHandler(BaseInfo):
    async def docker_Handler(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        content = self.docker()
        safe_content = [html.escape(line) for line in content]
        msg = "<b>DOCKER INFO:</b>\n" + "\n".join(safe_content)
        await self.send_long_message(msg, update, parse_mode="HTML")