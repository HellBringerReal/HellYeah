import html
import random
import time
from typing import List

from telegram import Bot, Update, ParseMode
from telegram.ext import run_async

from gotti import dispatcher
from gotti.modules.disable import DisableAbleCommandHandler
from gotti.modules.helper_funcs.chat_status import is_user_admin, user_admin
from gotti.modules.helper_funcs.extraction import extract_user

#sleep how many times after each edit in 'police' 
EDIT_SLEEP = 1
#edit how many times in 'police' 
EDIT_TIMES = 3

police_siren = [
            "🔴🔴🔴⬜️⬜️⬜️🔵🔵🔵\n🔴🔴🔴⬜️⬜️⬜️🔵🔵🔵\n🔴🔴🔴⬜️⬜️⬜️🔵🔵🔵",
            "🔵🔵🔵⬜️⬜️⬜️🔴🔴🔴\n🔵🔵🔵⬜️⬜️⬜️🔴🔴🔴\n🔵🔵🔵⬜️⬜️⬜️🔴🔴🔴"
]



@user_admin
@run_async
def police(bot: Bot, update: Update):
    msg = update.effective_message.reply_text('Police is coming!') 
    for x in range(EDIT_TIMES):
        msg.edit_text(police_siren[x%2])
        time.sleep(EDIT_SLEEP)
    msg.edit_text('Police is here!')


__help__ = """
 - /cash : currency converter
 example syntax: /cash 1 USD INR

 - /define <word>: returns the definition of the word.
 - /time <query> : Gives information about a timezone. Country Code/Country Name/Timezone Name
*Dogbin*
 - /paste: Create a paste or a shortened url using [dogbin](https://del.dog)
 - /getpaste: Get the content of a paste or shortened url from [dogbin](https://del.dog)
 - /pastestats: Get stats of a paste or shortened url from [dogbin](https://del.dog)
"""

POLICE_HANDLER = DisableAbleCommandHandler("police", police)


dispatcher.add_handler(POLICE_HANDLER)

__mod_name__ = "EXTRAS"
__command_list__ = ["police"]
__handlers__ = [POLICE_HANDLER]
