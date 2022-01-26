async def gifspam(e, smex):
    try:
        await e.client(
            functions.messages.SaveGifRequest(
                id=types.InputDocument(
                    id=sandy.media.document.id,
                    access_hash=smex.media.document.access_hash,
                    file_reference=smex.media.document.file_reference,
                ),
                unsave=True,
            )
        )
    except Exception:
        pass

import asyncio
import random
import os
from telethon import events
from telethon import functions, types
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from .. import Riz, Riz2, Riz3, Riz4, Riz5 , Riz6, Riz7, Riz8, Riz9, Riz10, SUDO_USERS
from resources.data import GROUP, PORMS


SMEX_USERS = []
for x in SUDO_USERS:
    SMEX_USERS.append(x)



@Riz.on(events.NewMessage(pattern=r"\.spam"))
@Riz2.on(events.NewMessage(pattern=r"\.spam"))
@Riz3.on(events.NewMessage(pattern=r"\.spam"))
@Riz4.on(events.NewMessage(pattern=r"\.spam"))
@Riz5.on(events.NewMessage(pattern=r"\.spam"))
@Riz6.on(events.NewMessage(pattern=r"\.spam"))
@Riz7.on(events.NewMessage(pattern=r"\.spam"))
@Riz8.on(events.NewMessage(pattern=r"\.spam"))
@Riz9.on(events.NewMessage(pattern=r"\.spam"))
@Riz10.on(events.NewMessage(pattern=r"\.spam"))
async def spam(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗦𝗽𝗮𝗺\n\nCommand:\n\n.spam <count> <message to spam>\n\n.spam <count> <reply to a message>\n\nCount must be a integer."
    error = "Spam Module can only be used till 100 count. For bigger spams use BigSpam."
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None)
        Rizoel = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(Rizoel) == 2:
            message = str(Rizoel[1])
            counter = int(Rizoel[0])
            if counter > 100:
                return await e.reply(error, parse_mode=None, link_preview=None)
            await asyncio.wait([e.respond(message) for i in range(counter)])
        elif e.reply_to_msg_id and smex.media:
            counter = int(Rizoel[0])
            if counter > 100:
                return await e.reply(error, parse_mode=None, link_preview=None)
            for _ in range(counter):
                smex = await e.client.send_file(e.chat_id, smex, caption=smex.text)
                await gifspam(e, smex)
        elif e.reply_to_msg_id and smex.text:
            message = smex.text
            counter = int(Rizoel[0])
            if counter > 100:
                return await e.reply(error, parse_mode=None, link_preview=None)
            await asyncio.wait([e.respond(message) for i in range(counter)])
        else:
            await e.reply(usage, parse_mode=None, link_preview=None)

@Riz.on(events.NewMessage(pattern=r"\.pspam"))
@Riz2.on(events.NewMessage(pattern=r"\.pspam"))
@Riz3.on(events.NewMessage(pattern=r"\.pspam"))
@Riz4.on(events.NewMessage(pattern=r"\.pspam"))
@Riz5.on(events.NewMessage(pattern=r"\.pspam"))
@Riz6.on(events.NewMessage(pattern=r"\.pspam"))
@Riz7.on(events.NewMessage(pattern=r"\.pspam"))
@Riz8.on(events.NewMessage(pattern=r"\.pspam"))
@Riz9.on(events.NewMessage(pattern=r"\.pspam"))
@Riz10.on(events.NewMessage(pattern=r"\.pspam"))
async def pspam(e):
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        rizoel = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(rizoel) == 1:
            counter = int(rizoel[0])
            if int(e.chat_id) in GROUP:
                text = f"Sorry !! I can't spam here"
                await e.reply(text, parse_mode=None, link_preview=None )
            else:
                 porrn = random.choice(PORMS)
                 for _ in range(counter):
                     async with e.client.action(e.chat_id, "document"):
                         smex = await e.client.send_file(e.chat_id, porrn)
                         await gifspam(e, smex) 
                     await asyncio.sleep(0.4)
        else:
            usage = f"**MODULE NAME : PORN SPAM** \n\n command: `.pornspam <count>`"
            await e.reply(usage, parse_mode=None, link_preview=None )
