#Lol 
import logging
import os
import sys
import time
import os
import urllib.parse as urlparse
import json
from logging import basicConfig
from logging import DEBUG
from logging import getLogger
from logging import INFO


from telethon import TelegramClient
StartTime = time.time()

#aah lol
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)
LOGGER = logging.getLogger(__name__)
ENV = bool(os.environ.get("ENV", True))

if ENV:
    BOT_TOKEN = os.environ.get("BOT_TOKEN", None)
    API_ID = os.environ.get("API_ID", None)
    API_HASH = os.environ.get("API_HASH", None)

kid = TelegramClient('kid', API_ID, API_HASH).start(bot_token=BOT_TOKEN)
