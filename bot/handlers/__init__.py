from telegram.ext import CommandHandler, MessageHandler, filters

from .capture import CaptureHandler
from .all_info import AllHandler
from .docker_info import DockerHandler
from .network_info import NetworkHandler
from .sensors_info import SensorsHandler
from .system_info import SystemHandler
from .start import start
from .cpu_info import CpuHandler
from .memory_info import MemoryHandler
from .disk_info import DiskHandler
from .help import help_command


def setup_handlers(app):
    all_Handler = AllHandler()
    docker_Handler = DockerHandler()
    network_Handler = NetworkHandler()
    sensors_Handler = SensorsHandler()
    system_Handler = SystemHandler()
    cpu_Handler = CpuHandler()
    memory_Handler = MemoryHandler()
    disk_Handler = DiskHandler()
    capture_Handler = CaptureHandler()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("system", system_Handler.system_Handler))
    app.add_handler(CommandHandler("cpu", cpu_Handler.cpu_Handler))
    app.add_handler(CommandHandler("memory", memory_Handler.memory_Handler))
    app.add_handler(CommandHandler("disk", disk_Handler.disk_Handler))
    app.add_handler(CommandHandler("network", network_Handler.network_Handler))
    app.add_handler(CommandHandler("docker", docker_Handler.docker_Handler))
    app.add_handler(CommandHandler("sensors", sensors_Handler.sensors_Handler))
    app.add_handler(CommandHandler("all", all_Handler.all_Handler))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("capture", capture_Handler.capture_Handler))
    app.add_handler(MessageHandler(
        filters.TEXT & ~filters.COMMAND, help_command))
