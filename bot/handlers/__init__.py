from telegram.ext import CommandHandler, ConversationHandler, MessageHandler, filters

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
    app.add_handler(CommandHandler("help", help_command))
    """
    app.add_handler(CommandHandler("setuser", set_user))
    app.add_handler(CommandHandler("sendpdf", send_pdf))
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("savedeck", start_savedeck)],
        states={
            ASK_DECK_NAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, receive_deck_name)],
            ASK_DECKLIST: [MessageHandler(filters.TEXT & ~filters.COMMAND, receive_decklist)],
        },
        fallbacks=[CommandHandler("cancel", cancel)],
    )
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("list", start_list)],
        states={
            LOCATION: [MessageHandler(filters.TEXT & ~filters.COMMAND, return_decklist)],
            },
        fallbacks=[CommandHandler("cancel", cancel)],
    )
    app.add_handler(conv_handler)
    """
