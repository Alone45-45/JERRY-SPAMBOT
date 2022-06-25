import asyncio
import os
from telethon.tl.functions.users import GetFullUserRequest
from telethon import events, Button
from telethon.tl.custom import button
from .. import Jerry, Jerry2, Jerry3, Jerry4, Jerry5, Jerry6, Jerry7, Jerry8, Jerry9, Jerry10, ALIVE_PIC, OWNER_ID
from JerrySpam.plugins.help import *


RIZ_IMG = ALIVE_PIC if ALIVE_PIC else "https://te.legra.ph/file/3dcb99ff2621a74ceed37.jpg"

Riz_Button = [
        [
        Button.url("• sᴜᴘᴘᴏʀᴛ •", "https://t.me/chatty_familia")
        ],
        [
        Button.inline("• ᴄᴍᴅs •", data="help_back")
        ]
        ]
               
RizX_Button = [
        [
        Button.url("ᴄʜᴀɴɴᴇʟ", "https://t.me/TASTRON"),
        Button.url("sᴜᴘᴘᴏʀᴛ", "https://t.me/chatty_familia")
        ],
        [
        Button.url("• ʀᴇᴘᴏ •", "https://t.me/TASTRON")
        ]
        ]
        
        
#USERS 


@Jerry.on(events.NewMessage(pattern="/start"))
@Jerry2.on(events.NewMessage(pattern="/start"))
@Jerry3.on(events.NewMessage(pattern="/start"))
@Jerry4.on(events.NewMessage(pattern="/start"))
@Jerry5.on(events.NewMessage(pattern="/start"))
@Jerry6.on(events.NewMessage(pattern="/start"))
@Jerry7.on(events.NewMessage(pattern="/start"))
@Jerry7.on(events.NewMessage(pattern="/start"))
@Jerry8.on(events.NewMessage(pattern="/start"))
@Jerry9.on(events.NewMessage(pattern="/start"))
@Jerry10.on(events.NewMessage(pattern="/start"))
async def start(event):              
    if event.is_private:
       JerryT = await event.client.get_me()
       bot_id = JerryT.first_name
       bot_username = JerryT.username
       replied_user = await event.client(GetFullUserRequest(event.sender_id))
       JerryT = event.chat_id
       firstname = replied_user.user.first_name
       ownermsg = f"**Hi Master, Its me {bot_id}, Your Spam Bot !! \n\n Click Below Buttons For help**"
       usermsg = f"**Hello, {firstname} ! Nice To Meet You, Well I Am {bot_id}, An Powerfull Spam Bot.** \n\n**If You Want Your Own Spam Bots You Can Deploy From Button Below.** \n\n**𝐏𝐎𝐖𝐄𝐑𝐄𝐃 𝐁𝐘 [JERRY](https://t.me/TASTRON)**"
       if event.sender_id == OWNER_ID:
            await event.client.send_file(JerryT,
                  RIZ_IMG,
                  caption=ownermsg, 
                  buttons=Riz_Button)
       else:
            await event.client.send_file(JerryT,
                  RIZ_IMG,
                  caption=usermsg, 
                  buttons=RizX_Button)
                

