from telegram import Update
from telegram.ext import ContextTypes

from bot.socket.socket_con import SocketCon


async def cpu_info(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    sock = SocketCon()
    sock.connect()
    content = sock.systeminfo()
    msg = "<b>CPU INFO:</b>\n" + "\n".join(content)
    await update.message.reply_text(msg, parse_mode="HTML")