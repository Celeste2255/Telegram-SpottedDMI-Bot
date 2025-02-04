"""/help command"""
from telegram import Update, ParseMode
from telegram.ext import CallbackContext
from modules.data import Config, read_md
from modules.utils import EventInfo


def help_cmd(update: Update, context: CallbackContext):
    """Handles the /help command.
    Sends an help message

    Args:
        update: update event
        context: context passed by the handler
    """
    info = EventInfo.from_message(update, context)
    if info.chat_id == Config.meme_get('group_id'):  # if you are in the admin group
        text = read_md("instructions")
    else:  # you are NOT in the admin group
        text = read_md("help")
    info.bot.send_message(chat_id=info.chat_id, text=text, parse_mode=ParseMode.MARKDOWN_V2, disable_web_page_preview=True)
