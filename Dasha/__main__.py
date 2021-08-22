from sys import argv, exit
from Dasha import kid
from Dasha import BOT_TOKEN

import Dasha.events

try:
    kid.start(bot_token=BOT_TOKEN)
except Exception:
    print("Bot Token Invalid")
    exit(1)

if len(argv) not in (1, 3, 4):
    kid.disconnect()
else:
    kid.run_until_disconnected()
