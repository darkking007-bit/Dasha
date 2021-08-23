#kek

from Dasha import kid
import requests
from telethon import events

@kid.on(events.NewMessage(outgoing=True, pattern="(?i)^haste$"))
def haste(e):
  if e.is_reply and e.get_reply_message().message:
    text = e.get_reply_message().text
    e.edit("[Haste link to the above](http://hastebin.com/{}) ".format(requests.post("https://hastebin.com/documents", data=text).json()['key']))
