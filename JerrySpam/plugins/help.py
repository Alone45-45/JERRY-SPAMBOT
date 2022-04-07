from JerrySpam import Jerry, Jerry2, Jerry3, Jerry4, Jerry5, Jerry6, Jerry7, Jerry8, Jerry9, Jerry10, SUDO_USERS
from telethon import events, Button
from telethon.tl.custom import button
from time import time
from datetime import datetime
from JerrySpam import CMD_HNDLR as hl
    
HELP_PIC = "https://te.legra.ph/file/d1344663dfba5cadb595d.jpg"

Jerry_Help = "__Click On Below Buttons for help__"


@Jerry.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Jerry2.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Jerry3.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Jerry4.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Jerry5.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Jerry6.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Jerry7.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Jerry8.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Jerry9.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Jerry10.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
async def help(event):
    if event.sender_id in SUDO_USERS:
       await event.client.send_file(event.chat_id,
                                  HELP_PIC,
                                  caption=Jerry_Help,
                                  buttons=[
           [
            Button.inline("• Spam •", data="spam"),
            Button.inline("• Raid •", data="raid"),
           ],
           [
            Button.inline("• Extra •", data="extra"),
           ],
           [    
            Button.url("ᴄʜᴀɴɴᴇʟ", "https://t.me/THEJERRY_NETWORK")
           ],
           ],
           )              

  
  
extra_msg = f"""
**Help Extra Cmds**

**Userbot**: Userbot Cmds
command:
i) {hl}ping 
ii) {hl}alive
iii) {hl}restart
iv) {hl}addsudo <reply to user> : Owner Cmd

**Echo**: To Active Echo On Any User
command:
i) {hl}addecho <reply to user>
ii) {hl}rmecho <reply to user>

**Leave**: To Leave Group/channel
command:
i) {hl}leave <group/chat id>
ii) {hl}leave : Type in the Group bot will auto leave that group

**Packspam**: Sticker Pack Spam
i) {hl}packspam (replying to any sticker)

**© @THEJERRY_NETWORK**
"""

                 
raid_msg = f"""
**Help Raid Cmds**


**raid:** Activates raid on any individual user for given range.
command:
i) {hl}raid <count> <username
ii) {hl}raid <count> <reply to user>

**Delayraid**: Activates raid on any individual user for given range.
Command:
i) {hl}delayraid <delay> <count> <Username of User>
ii) {hl}delayraid <delay> <count> <reply to a User>

**replyraid:** Activates Reply Raid on the user!!
command:
i) {hl}replyraid <replying to user>
ii) {hl}dreplyraid <username>

**dreplyraid:** Deactivates reply raid on the user!!
command:
i) {hl}dreplyraid <replying to user>
ii) {hl}dreplyraid <username>


**© @THEJERRY_NETWORK**
"""

spam_msg = f"""
**Help Spam Cmds**

**spam**: Spams a message for given counter(<= 100).
command:
i) {hl}spam <count> <message to spam> (you can reply any message if you want bot to reply that message and do spamming)
ii) {hl}spam <count> <replying any message>

**bigspam**: Spams a message for given counter.
command:
i) {hl}bigspam <count> <message to spam> (you can reply any message if you want bot to reply that message and do spamming)
ii) {hl}bigspam <count> <replying any message>

**delayspam**: Delay spam a text for given counter after given time.
command:
i) {hl}delayspam <delay> <count> <message to spam> (you can reply any message if you want bot to reply that message and do spamming)
ii) {hl}delayspam <delay> <count> <replying any message>

**pornspam**: Pornography Spam.
command:
i) {hl}pornspam <count>

**hang**: Spams hanging message for given counter.
command:
i) {hl}hang <counter> (you can reply any message if you want bot to reply that message and do spamming)

** © @THEJERRY_NETWORK**
"""                     
           
           
@Jerry.on(events.CallbackQuery(pattern=r"help_back"))
@Jerry2.on(events.CallbackQuery(pattern=r"help_back"))
@Jerry3.on(events.CallbackQuery(pattern=r"help_back"))
@Jerry4.on(events.CallbackQuery(pattern=r"help_back"))
@Jerry5.on(events.CallbackQuery(pattern=r"help_back"))
@Jerry6.on(events.CallbackQuery(pattern=r"help_back"))
@Jerry7.on(events.CallbackQuery(pattern=r"help_back"))
@Jerry8.on(events.CallbackQuery(pattern=r"help_back"))
@Jerry9.on(events.CallbackQuery(pattern=r"help_back"))
@Jerry10.on(events.CallbackQuery(pattern=r"help_back"))
async def helpback(event):
   if event.query.user_id in SUDO_USERS:    
      await event.edit(
            Jerry_Help,
            buttons=[
                [
            Button.inline("Spam", data="spam"),
            Button.inline("Raid", data="raid"),
           ],
           [
            Button.inline("Extra cmds", data="extra"),
           ],
           [    
            Button.url("ᴄʜᴀɴɴᴇʟ", "https://t.me/THEJERRY_NETWORK")
           ],
           ],
        )           
   else:
        Alert = (
                "Noob !! Make Your Own Jerry T Spam Bots !!"
            )
        await event.answer(Alert, cache_time=0, alert=True)
      
           
                      
@Jerry.on(events.CallbackQuery(pattern=r"spam"))
@Jerry2.on(events.CallbackQuery(pattern=r"spam"))
@Jerry3.on(events.CallbackQuery(pattern=r"spam"))
@Jerry4.on(events.CallbackQuery(pattern=r"spam"))
@Jerry5.on(events.CallbackQuery(pattern=r"spam"))
@Jerry6.on(events.CallbackQuery(pattern=r"spam"))
@Jerry7.on(events.CallbackQuery(pattern=r"spam"))
@Jerry8.on(events.CallbackQuery(pattern=r"spam"))
@Jerry9.on(events.CallbackQuery(pattern=r"spam"))
@Jerry10.on(events.CallbackQuery(pattern=r"spam"))
async def help_spam(event):
   if event.query.user_id in SUDO_USERS:    
       await event.edit(
            spam_msg,
            buttons=[
                [
            Button.inline("< Back", data="help_back"),
            ],
            ],
            ) 
   else:
        Alert = (
                "Noob !! Make Your Own Jerry T Spam Bots !!"
            )
        await event.answer(Alert, cache_time=0, alert=True)
                 
                                                       
@Jerry.on(events.CallbackQuery(pattern=r"raid"))
@Jerry2.on(events.CallbackQuery(pattern=r"raid"))
@Jerry3.on(events.CallbackQuery(pattern=r"raid"))
@Jerry4.on(events.CallbackQuery(pattern=r"raid"))
@Jerry5.on(events.CallbackQuery(pattern=r"raid"))
@Jerry6.on(events.CallbackQuery(pattern=r"raid"))
@Jerry7.on(events.CallbackQuery(pattern=r"raid"))
@Jerry8.on(events.CallbackQuery(pattern=r"raid"))
@Jerry9.on(events.CallbackQuery(pattern=r"raid"))
@Jerry10.on(events.CallbackQuery(pattern=r"raid"))
async def help_raid(event):
     if event.query.user_id in SUDO_USERS:
        await event.edit(
            raid_msg,
            buttons=[
            [
            Button.inline("< Back", data="help_back"),
            ],
            ],
            )  
     else:
        Alert = (
                "Noob !! Make Your Own Jerry T Spam Bots !!"
            )
        await event.answer(Alert, cache_time=0, alert=True)
       


@Jerry.on(events.CallbackQuery(pattern=r"extra"))
@Jerry2.on(events.CallbackQuery(pattern=r"extra"))
@Jerry3.on(events.CallbackQuery(pattern=r"extra"))
@Jerry4.on(events.CallbackQuery(pattern=r"extra"))
@Jerry5.on(events.CallbackQuery(pattern=r"extra"))
@Jerry6.on(events.CallbackQuery(pattern=r"extra"))
@Jerry7.on(events.CallbackQuery(pattern=r"extra"))
@Jerry8.on(events.CallbackQuery(pattern=r"extra"))
@Jerry9.on(events.CallbackQuery(pattern=r"extra"))
@Jerry10.on(events.CallbackQuery(pattern=r"extra"))
async def help_extra(event):
   if event.query.user_id in SUDO_USERS:
        await event.edit(
            extra_msg,
            buttons=[
            [
            Button.inline("< Back", data="help_back"),                        
            ],
            ],
            )
   else:
        Alert = (
                "Noob !! Make Your Own Jerry T Spam Bots !!"
            )
        await event.answer(Alert, cache_time=0, alert=True)

