from telegram import Update
from telegram.ext import ContextTypes
from bot.handlers.base_info import BaseInfo

class DockerHandler(BaseInfo):
    async def docker_Handler(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        content = self.docker()
        msg = "<b>DOCKER INFO:</b>\n" + "\n".join(content)
        await update.message.reply_text(msg, parse_mode="HTML")