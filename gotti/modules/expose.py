from telegram import Bot, Update, ParseMode
from telegram.ext import run_async

import gotti.modules.fun_strings as fun_strings
from gotti import dispatcher
from gotti.modules.disable import DisableAbleCommandHandler

@run_async
def expose(bot: Bot, update: Update):
    msg = update.effective_message
    reply_text = msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    reply_text(fun_strings.EXPOSE)
     
     
__help__ = """
*So You Are Searching For Expose Channel And You Really Want to Expose Someone Then You Are At The Right Place
For This You Must Need Some Proofs As Follows:
1. Forwarded Messages
2. Screenshots
3. Person's Info
4. Just Support Our Teams
5. Have Guts To Raise Your Voice*

- /expose If You Want To Expose Someone
"""

EXPOSE_HANDLER = DisableAbleCommandHandler("expose", expose)
dispatcher.add_handler(EXPOSE_HANDLER)


__mod_name__ = "EXPOSE😎"
__command_list__ = ["expose"]
__handlers__ = [EXPOSE_HANDLER]
