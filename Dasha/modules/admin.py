from Dasha import ubot, tbot
from Dasha.events import dasha
from . import get_user

@dasha(pattern="^/kick ?(.*)")
async def kick(event):
 if event.is_private:
   return await event.edit("Please use this in groups.")
 try:
  user, extra = await get_user(event)
 except TypeError:
  pass
 if not user:
  await event.edit("Failed to fetch user.")
 if not event.chat.admin_rights.ban_users:
   return await event.edit("Failed to Kick, No CanBanUsers Right.")
 try:
  await ubot.kick_participant(event.chat_id, user.id)
  await event.edit(f"Kicked **{user.first_name}** from {event.chat.title}!")
 except:
  await event.edit("Can't kick admins.")
