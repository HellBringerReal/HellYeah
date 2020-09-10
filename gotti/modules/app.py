
from random import randint
from gtts import gTTS
import os
import re
import urllib
import urllib.request
from urllib.error import URLError, HTTPError
from bs4 import BeautifulSoup
import requests
from typing import List
from telegram import ParseMode, InputMediaPhoto, Update, Bot, TelegramError, ChatAction
from telegram.ext import CommandHandler, run_async
from gotti.modules.disable import DisableAbleCommandHandler


@run_async
def app(_bot: Bot, update: Update):
    message = update.effective_message
    try:
        progress_message = update.effective_message.reply_text(
            "Searching.... ")
        app_name = message.text[len('/app '):]
        remove_space = app_name.split(' ')
        final_name = '+'.join(remove_space)
        page = requests.get(
            f"https://play.google.com/store/search?q={final_name}&c=apps")
        soup = BeautifulSoup(page.content, 'lxml', from_encoding='utf-8')
        results = soup.findAll("div", "ZmHEEd")
        app_name = results[0].findNext(
            'div', 'Vpfmgd').findNext(
            'div', 'WsMG1c nnK0zc').text
        app_dev = results[0].findNext(
            'div', 'Vpfmgd').findNext(
            'div', 'KoLSrc').text
        app_dev_link = "https://play.google.com" + results[0].findNext(
            'div', 'Vpfmgd').findNext('a', 'mnKHRc')['href']
        app_rating = results[0].findNext('div', 'Vpfmgd').findNext(
            'div', 'pf5lIe').find('div')['aria-label']
        app_link = "https://play.google.com" + results[0].findNext(
            'div', 'Vpfmgd').findNext('div', 'vU6FJ p63iDd').a['href']
        app_icon = results[0].findNext(
            'div', 'Vpfmgd').findNext(
            'div', 'uzcko').img['data-src']
        app_details = "<a href='" + app_icon + "'>📲&#8203;</a>"
        app_details += " <b>" + app_name + "</b>"
        app_details += "\n\n<code>Developer :</code> <a href='" + app_dev_link + "'>"
        app_details += app_dev + "</a>"
        app_details += "\n<code>Rating :</code> " + app_rating.replace(
            "Rated ", "⭐️ ").replace(" out of ", "/").replace(
                " stars", "", 1).replace(" stars", "⭐️").replace("five", "5")
        app_details += "\n<code>Features :</code> <a href='" + \
            app_link + "'>View in Play Store</a>"
        message.reply_text(
            app_details,
            disable_web_page_preview=False,
            parse_mode='html')
    except IndexError:
        message.reply_text(
            "No result found in search. Please enter **Valid app name**")
    except Exception as err:
        message.reply_text(err)
    progress_message.delete()

APP_HANDLER = DisableAbleCommandHandler("app", app)

dispatcher.add_handler(APP_HANDLER)
