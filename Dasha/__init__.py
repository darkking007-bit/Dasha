from telethon import TelegramClient
from telethon.sessions import StringSession
import time
import os, logging
from logging import basicConfig, getLogger, INFO
"""Dasha"""
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
LOGGER = logging.getLogger(__name__)

StartTime = time.time()

STRING_SESSION = os.environ.get("STRING_SESSION")
D_SESSION = os.environ.get("D_SESSION")
X_SESSION = os.environ.get("X_SESSION")
TOKEN = os.environ.get("TOKEN")
OWNER_ID = os.environ.get("OWNER_ID")
API_KEY = os.environ.get("API_KEY")
API_HASH = os.environ.get("API_HASH")

ubot = TelegramClient(StringSession(STRING_SESSION), API_KEY, API_HASH)
tbot = TelegramClient(None, API_KEY, API_HASH)
dbot = TelegramClient(StringSession(D_SESSION), API_KEY, API_HASH)
xbot = TelegramClient(StringSession(X_SESSION), API_KEY, API_HASH)
