from telegram.ext import CommandHandler, ConversationHandler, MessageHandler, filters

from .all_info import all_info
from .docker_info import docker_info
from .network_info import network_info
from .sensors_info import sensors_info
from .system_info import system_info
from .start import start
from .cpu_info import cpu_info
from .memory_info import memory_info
from .disk_info import disk_info
from .help import help_command

def setup_handlers(app):
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("system", system_info))
    app.add_handler(CommandHandler("cpu", cpu_info))
    app.add_handler(CommandHandler("memory", memory_info))
    app.add_handler(CommandHandler("disk", disk_info))
    app.add_handler(CommandHandler("network", network_info))
    app.add_handler(CommandHandler("docker", docker_info))
    app.add_handler(CommandHandler("sensors", sensors_info))
    app.add_handler(CommandHandler("all", all_info))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, help_command))
