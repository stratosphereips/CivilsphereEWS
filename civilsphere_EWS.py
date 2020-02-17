#!/usr/bin/python3
# This file is part of the Stratosphere Linux IPS
# See the file 'LICENSE' for copying permission.
# Author: Veronica Valeros, veronica.valeros@aic.fel.cvut.cz

import sys
from twython import Twython
import telegram

# Import the Twitter API key information stored in auth.py
from auth_twitterbot import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

from auth_telegrambot import (
    telegramtoken,
    telegramchannel
)

version = '0.0.2'

# Reading the message as a parameter
try:
    message=sys.argv[1]
except:
    print('Civilsphere Early Warning System: a tool to share information to Telegram and Twitter. \nVersion {} - https://www.civilsphereproject.org'.format(version))
    print('')
    print('Usage:\n\tcivilsphereEWS.py "This is the text to post to Twitter and Telegram"')
    print('')
    sys.exit(-1)


print('Civilsphere Early Warning System: a tool to share information to Telegram and Twitter. \nVersion {} - https://www.civilsphereproject.org'.format(version))

# Connect with the Twitter API using the imported keys
twitterbot = Twython(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

# Instanciating the telegram bot
telegrambot = telegram.Bot(token=telegramtoken)


print(message)
# POST message to Twitter
twitterbot.update_status(status=message)

# POST message to Telegram
telegrambot.send_message(chat_id=telegramchannel, text=message)
print("POSTED")
