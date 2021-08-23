from telethon import events, buttons
from Dasha import kid


@kid.on(events.NewMessage(pattern = '[*?/]lol'))
async def lol(event):
    await event.reply('lmao')
