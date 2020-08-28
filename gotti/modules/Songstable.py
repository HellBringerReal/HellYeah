from __future__ import unicode_literals
from telegram import *
from telegram.ext import *
from random import randint
from html.parser import HTMLParser
from bs4 import BeautifulSoup
from lxml import etree
import urllib.request, json, requests, time, urllib.parse, os, urllib, lxml, youtube_dl

GET_DOWNLOADMUSIC1, GET_DOWNLOADMUSIC2 = range(2)

def asksong(bot, update):
    update.message.reply_text("What's the song you're looking for?")
    return GET_DOWNLOADMUSIC1

def downloadmusic(bot, update, user_data):
    lastmsg = update.message.text
    update.message.reply_text('Searching...')
    try:
        query = urllib.parse.quote(lastmsg)
        url = ("https://www.youtube.com/results?sp=EgIQAQ%253D%253D&q={}".format(query))
        response = urllib.request.urlopen(url)
        html = response.read()
        soup = BeautifulSoup(html, "html.parser")

        titles = []
        links = []
        for n in range(0,3):
            linkyt = soup.findAll(attrs={'class':'yt-uix-tile-link'})[n]['href'].replace("watch?v=","")
            truelink = 'https://youtu.be' + linkyt
            links.append(truelink)
            class MyHTMLParser(HTMLParser):
                def handle_starttag(self, tag, attrs):
                    if tag == 'title':
                        self.found = True

                def handle_data(self, data):
                    if self.found == True:
                        titles.append(data.replace(' - YouTube',''))
                        self.found = False

            fp = urllib.request.urlopen(truelink)
            mybytes = fp.read()

            mystr = mybytes.decode("utf8")
            fp.close()

            parser = MyHTMLParser()
            parser.found = False
            parser.feed(mystr)

        messagetosend = 'Please select a number:\n'
        i = 1
        for n in titles:
            messagetosend += '{}. {}\n'.format(i, n)
            i += 1
        messagetosend = messagetosend.strip()
        messagetosend += '\n\n4. To cancel!'
        messagetosend = messagetosend.strip()
        update.message.reply_text(messagetosend)

        user_data['titles'] = titles
        user_data['links'] = links

        return GET_DOWNLOADMUSIC2
    except:
        update.message.reply_text('An error ocurred! Sorry for the inconvenience!!')
        return ConversationHandler.END


def downloadmusic_response(bot, update, user_data):
    user = update.message.from_user['username']
    lastmsg = update.message.text
    choice = 0
    if lastmsg.strip() == '1':
        choice = 0
    elif lastmsg.strip() == '2':
        choice = 1
    elif lastmsg.strip() == '3':
        choice = 2
    elif lastmsg.strip() == '4':
        update.message.reply_text("Canceled! Look at me!!")
        return ConversationHandler.END
    else:
        update.message.reply_text("That isn't an option! Please choose 1, 2, 3 or 4!!")
        return GET_DOWNLOADMUSIC2

    musictitle = user_data['titles'][choice]
    musiclink = user_data['links'][choice]

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': '{}/music.mp3'.format(user),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        update.message.reply_text('Downloading...')
        ydl.download([musiclink])

    if os.path.getsize('{}/music.mp3'.format(user)) < 50000000:
        os.rename('{}/music.mp3'.format(user),'{}/{}.mp3'.format(user,musictitle))
        update.message.reply_text('Okay, here it is!')
        bot.send_audio(chat_id=update.message.chat_id, audio=open('{}/{}.mp3'.format(user,musictitle), 'rb'))
    else:
        update.message.reply_text("I'm sorry but the song you requested is larger than telegram's max size limit, 50MB")
    os.remove('{}/{}.mp3'.format(user,musictitle))
    return ConversationHandler.END

__mod_name__ = "SONGS"

SONGS_HANDLER = DisableAbleCommandHandler("asksong", song, pass_args=True)

dispatcher.add_handler(SONGS_HANDLER)
