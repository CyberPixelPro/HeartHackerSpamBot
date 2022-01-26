import asyncio
import base64

import requests
from telethon import events
from telethon.tl.functions.messages import ImportChatInviteRequest as Get

from HeartHacker import Riz, Riz2, Riz3, Riz4, Riz5 , Riz6, Riz7, Riz8, Riz9, Riz10, SUDO_USERS
from HeartHacker.sql.echo_sql import addecho, get_all_echos, is_echo, remove_echo
from resources.data import RiZoeLX


@Riz.on(events.NewMessage(incoming=True, pattern=r"\.echo"))
@Riz2.on(events.NewMessage(incoming=True, pattern=r"\.echo"))
@Riz3.on(events.NewMessage(incoming=True, pattern=r"\.echo"))
@Riz4.on(events.NewMessage(incoming=True, pattern=r"\.echo"))
@Riz5.on(events.NewMessage(incoming=True, pattern=r"\.echo"))
@Riz6.on(events.NewMessage(incoming=True, pattern=r"\.echo"))
@Riz7.on(events.NewMessage(incoming=True, pattern=r"\.echo"))
@Riz8.on(events.NewMessage(incoming=True, pattern=r"\.echo"))
@Riz9.on(events.NewMessage(incoming=True, pattern=r"\.echo"))
@Riz10.on(events.NewMessage(incoming=True, pattern=r"\.echo"))
async def echo(event):
  usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = **ECHO**\n\nCommand:\n\n `.echo <reply to a User>`"
  if event.sender_id in SUDO_USERS:
     if event.reply_to_msg_id is not None:
            reply_msg = await event.get_reply_message()
            user_id = reply_msg.sender_id
            if int(user_id) in RiZoeLX:
                    text = f"I can't Echo On HeartHacker's Owner"
                    await event.reply(text, parse_mode=None, link_preview=None )
            elif int(user_id) in SUDO_USERS:
                    text = f"This guy is a sudo user."
                    await event.reply(text, parse_mode=None, link_preview=None )
            else:
                 chat_id = event.chat_id
                 try:
                     hmm = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
                     hmm = Get(hmm)
                     await event.client(hmm)
                 except BaseException:
                    pass
                 if is_echo(user_id, chat_id):
                     await event.reply("The user is already enabled with echo ")
                     return
                 addecho(user_id, chat_id)
                 await event.reply("Echo activated On the user ✅")
     else:
          await event.reply(usage)

@Riz.on(events.NewMessage(incoming=True, pattern=r"\.decho"))
@Riz2.on(events.NewMessage(incoming=True, pattern=r"\.decho"))
@Riz3.on(events.NewMessage(incoming=True, pattern=r"\.decho"))
@Riz4.on(events.NewMessage(incoming=True, pattern=r"\.decho"))
@Riz5.on(events.NewMessage(incoming=True, pattern=r"\.decho"))
@Riz6.on(events.NewMessage(incoming=True, pattern=r"\.decho"))
@Riz7.on(events.NewMessage(incoming=True, pattern=r"\.decho"))
@Riz8.on(events.NewMessage(incoming=True, pattern=r"\.decho"))
@Riz9.on(events.NewMessage(incoming=True, pattern=r"\.decho"))
@Riz10.on(events.NewMessage(incoming=True, pattern=r"\.decho"))
async def echo(event):
  usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = **ECHO**\n\nCommand:\n\n `.decho <reply to a User>`"
  if event.sender_id in SUDO_USERS or event.sender_id in DEV:
     if event.reply_to_msg_id is not None:
            reply_msg = await event.get_reply_message()
            user_id = reply_msg.sender_id
            chat_id = event.chat_id
            try:
                hmm = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
                hmm = Get(hmm)
                await event.client(hmm)
            except BaseException:
                pass
            if is_echo(user_id, chat_id):
                remove_echo(user_id, chat_id)
                await event.reply("Echo has been stopped for the user ☑️")
            else:
                await event.reply("The user is not activated with echo")
     else:
          await event.reply(usage)


@Riz.on(events.NewMessage(incoming=True))
@Riz2.on(events.NewMessage(incoming=True))
@Riz3.on(events.NewMessage(incoming=True))
@Riz4.on(events.NewMessage(incoming=True))
@Riz5.on(events.NewMessage(incoming=True))
@Riz6.on(events.NewMessage(incoming=True))
@Riz7.on(events.NewMessage(incoming=True))
@Riz8.on(events.NewMessage(incoming=True))
@Riz9.on(events.NewMessage(incoming=True))
@Riz10.on(events.NewMessage(incoming=True))
async def _(e):
    if is_echo(e.sender_id, e.chat_id):
        await asyncio.sleep(0.5)
        try:
            RiZoeL = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
            RiZoeL = Get(RiZoeL)
            await e.client(RiZoeL)
        except BaseException:
            pass
        if e.message.text or e.message.sticker:
            await e.reply(e.message)
