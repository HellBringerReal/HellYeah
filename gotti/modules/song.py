from telethon import events
import subprocess
from telethon.errors import MessageEmptyError, MessageTooLongError, MessageNotModifiedError
from telegram import Message, Chat, Update, Bot
import io
import asyncio
import time
import glob
import os
import instantmusic,subprocess
os.system("rm -rf *.mp3")


@run_async
def song(bot: Bot, update: Update, args):
    chat_id = update.effective_chat.id
    msg = update.effective_message
    msg_id = update.effective_message.message_id
    if not cmd:
        msg.reply_text("Please enter a query!")
        return
    else:
        caption = cmd
    reply_to_id = event.message.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id   
    msg.reply_text("ok finding the song")  
    os.system("instantmusic -q -s "+cmd)
    bro = 'for f in *.webm; do      mv -- "$f" "${f%.webm}.mp3"; done'
    os.system(bro)
    l = glob.glob("*.mp3")
    loa = l[0]
    
    msg.reply_text("sending the song")
    bot.send_file(
                chat_id, loa,
                force_document=True,
                allow_cache=False,
                caption=cmd,
                reply_to_message_id=msg_id,
               )
    os.system("rm -rf *.mp3")
    subprocess.check_output("rm -rf *.mp3",shell=True)

    
     
__help__ = """
 - /song <song name> to get songs
"""

__mod_name__ = "SONGS"

SONGS_HANDLEE = DisableAbleCommandHandler("song", song, pass_args=True)

dispatcher.add_handler(SONGS_HANDLER)
        