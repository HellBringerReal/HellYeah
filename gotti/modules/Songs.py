from telethon import events
import subprocess
from telethon.errors import MessageEmptyError, MessageTooLongError, MessageNotModifiedError
import io
import asyncio
import time
import glob
import os
import instantmusic,subprocess
os.system("rm -rf *.mp3")
    

@run_async
def song(bot: event, Bot, update: Update, args):
    if event.fwd_from:
        return
    cmd = event.pattern_match.group(1)
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
    bot.client.send_file(
                event.chat_id,
                loa,
                force_document=True,
                allow_cache=False,
                caption=cmd,
                reply_to=reply_to_id
            )
    os.system("rm -rf *.mp3")
    subprocess.check_output("rm -rf *.mp3",shell=True)

__help__ = """
 - /song <name>: search download and return a song in the best format
"""
__mod_name__ = "SONGS"

SONGS_HANDLER = DisableAbleCommandHandler("song", song, pass_args=True)

dispatcher.add_handler(SONGS_HANDLER)
