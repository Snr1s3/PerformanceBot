from telegram.ext import CommandHandler, MessageHandler, filters

from .all_info import AllInfo
from .docker_info import DockerInfo
from .network_info import NetworkInfo
from .sensors_info import SensorsInfo
from .system_info import SystemInfo
from .start import start
from .cpu_info import CpuInfo
from .memory_info import MemoryInfo
from .disk_info import DiskInfo
from .help import help_command

def setup_handlers(app):
    all_info_handler = AllInfo()
    docker_info_handler = DockerInfo()
    network_info_handler = NetworkInfo()
    sensors_info_handler = SensorsInfo()
    system_info_handler = SystemInfo()
    cpu_info_handler = CpuInfo()
    memory_info_handler = MemoryInfo()
    disk_info_handler = DiskInfo()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("system", system_info_handler.system_info))
    app.add_handler(CommandHandler("cpu", cpu_info_handler.cpu_info))
    app.add_handler(CommandHandler("memory", memory_info_handler.memory_info))
    app.add_handler(CommandHandler("disk", disk_info_handler.disk_info))
    app.add_handler(CommandHandler("network", network_info_handler.network_info))
    app.add_handler(CommandHandler("docker", docker_info_handler.docker_info))
    app.add_handler(CommandHandler("sensors", sensors_info_handler.sensors_info))
    app.add_handler(CommandHandler("all", all_info_handler.all_info))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, help_command))