from telegram import Update
from telegram.ext import ContextTypes
from .system_info import system_info
from .cpu_info import cpu_info
from .memory_info import memory_info
from .disk_info import disk_info
from .network_info import network_info
from .docker_info import docker_info
from .sensors_info import sensors_info

async def all_info(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Collect info from each handler as text
    msgs = []
    
    msg = "<b>All System Info:</b>\n"
    await update.message.reply_text(msg, parse_mode="HTML")
    for func in [system_info, cpu_info, memory_info, disk_info, network_info, docker_info, sensors_info]:
        # Each info function should return a string, not send a message directly
        if hasattr(func, "get_text"):
            msgs.append(await func.get_text(update, context))
        else:
            # fallback: call and ignore output
            await func(update, context)