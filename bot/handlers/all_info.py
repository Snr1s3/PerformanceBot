from telegram import Update
from telegram.ext import ContextTypes

from bot.handlers.base_info import BaseInfo
from .system_info import SystemInfo
from .cpu_info import CpuInfo
from .memory_info import MemoryInfo
from .disk_info import DiskInfo
from .network_info import NetworkInfo
from .docker_info import DockerInfo
from .sensors_info import SensorsInfo


class AllInfo(BaseInfo):
    async def all_info(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        msg = "<b>All System Info:</b>\n"
        await update.message.reply_text(msg, parse_mode="HTML")

        handlers = [
            SystemInfo(),
            CpuInfo(),
            MemoryInfo(),
            DiskInfo(),
            NetworkInfo(),
            DockerInfo(),
            SensorsInfo()
        ]

        for handler in handlers:
            if hasattr(handler, "get_text"):
                text = await handler.get_text(update, context)
                await update.message.reply_text(text, parse_mode="HTML")
            elif hasattr(handler, "info"):
                text = await handler.info(update, context)
                await update.message.reply_text(text, parse_mode="HTML")