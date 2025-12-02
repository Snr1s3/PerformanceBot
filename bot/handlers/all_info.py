from telegram import Update
from telegram.ext import ContextTypes

from .base_info import BaseInfo
from handlers.cpu_info import CpuHandler
from handlers.disk_info import DiskHandler
from handlers.docker_info import DockerHandler
from handlers.memory_info import MemoryHandler
from handlers.network_info import NetworkHandler
from handlers.sensors_info import SensorsHandler
from handlers.system_info import SystemHandler


class AllHandler(BaseInfo):
    async def all_Handler(
        self,
        update: Update,
        context: ContextTypes.DEFAULT_TYPE
    ) -> None:
        msg = "<b>All System Info:</b>\n"
        await self.send_long_message(msg, update, parse_mode="HTML")

        handlers_methods = [
            (SystemHandler(), "system_Handler"),
            (CpuHandler(), "cpu_Handler"),
            (MemoryHandler(), "memory_Handler"),
            (DiskHandler(), "disk_Handler"),
            (NetworkHandler(), "network_Handler"),
            (DockerHandler(), "docker_Handler"),
            (SensorsHandler(), "sensors_Handler"),
        ]

        for handler, method_name in handlers_methods:
            method = getattr(handler, method_name, None)
            if method:
                msg = await method(update, context)
                if msg:
                    await self.send_long_message(
                        msg, update, parse_mode="HTML"
                    )

        await update.message.reply_text(
            "<b>ALL INFO:</b>\n"
            + "\n".join(self.system)
            + "\n"
            + "\n".join(self.cpu)
            + "\n"
            + "\n".join(self.memory)
            + "\n"
            + "\n".join(self.disk)
            + "\n"
            + "\n".join(self.network)
            + "\n"
            + "\n".join(self.sensors),
            parse_mode="HTML"
        )

        await update.message.reply_text(
            "\n".join(self.docker),
            parse_mode="HTML"
        )
