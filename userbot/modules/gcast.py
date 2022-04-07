# Ultroid - UserBot
# Copyright (C) 2020 TeamUltroid
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.
# Copyright by @mrismanaziz
# Recode by @OuraCakep

import asyncio

from requests import get
from telethon.errors.rpcerrorlist import FloodWaitError

from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP, DEVS
from userbot.utils import edit_delete, edit_or_reply, poci_cmd

while 0 < 6:
    _GCAST_BLACKLIST = get(
        "https://raw.githubusercontent.com/Oura-Ubot/darkweeb/master/blacklistgcast.json"
    )
    if _GCAST_BLACKLIST.status_code != 200:
        if 0 != 5:
            continue
        GCAST_BLACKLIST = [-1001267233272, -1001473548283, -1001217578068, -1001704645461]
        break
    GCAST_BLACKLIST = _GCAST_BLACKLIST.json()
    break

del _GCAST_BLACKLIST


@poci_cmd(pattern="gcast(?: |$)(.*)")
async def gcast(event):
    xx = event.pattern_match.group(1)
    if xx:
        msg = xx
    elif event.is_reply:
        msg = await event.get_reply_message()
    else:
        return await edit_delete(event, "**𝘽𝙞𝙨𝙖 𝙉𝙜𝙚𝙩𝙞𝙠 𝙔𝙖𝙣𝙜 𝘽𝙚𝙣𝙚𝙧 𝙂𝙖 𝙉𝙜𝙚𝙣𝙩𝙤𝙩𝙩𝙩...**")
    kk = await edit_or_reply(event, "`𝙔𝙪𝙝𝙪 𝙈𝙚𝙡𝙪𝙣𝙘𝙪𝙧... 𝙎𝙖𝙗𝙖𝙧 𝙔𝙖 𝙉𝙜𝙚𝙣𝙩𝙤𝙩𝙩𝙩 𝙇𝙖𝙜𝙞 𝙂𝙪𝙖 𝙎𝙚𝙗𝙖𝙧 𝘽𝙤𝙠𝙚𝙥𝙣𝙮𝙖, 𝙈𝙤𝙜𝙖 𝙇𝙞𝙢𝙞𝙩 𝙔𝙖 𝘼𝙣𝙟𝙚𝙣𝙜...`")
    er = 0
    done = 0
    async for x in event.client.iter_dialogs():
        if x.is_group:
            chat = x.id
            if chat not in GCAST_BLACKLIST:
                try:
                    await event.client.send_message(chat, msg)
                    await asyncio.sleep(0.1)
                    done += 1
                except FloodWaitError as anj:
                    await asyncio.sleep(int(anj.seconds))
                    await event.client.send_message(chat, msg)
                    done += 1
                except BaseException:
                    er += 1
    await kk.edit(
        f"**𝘼𝙇𝙃𝘼𝙈𝘿𝙐𝙇𝙄𝙇𝙇𝘼𝙃 𝘽𝙊𝙆𝙀𝙋 𝙆𝙀 𝙎𝙀𝘽𝘼𝙍 𝘿𝙄 ** `{done}` **𝙂𝙍𝙊𝙐𝙋, 𝘿𝙄 𝙏𝙊𝙇𝘼𝙆 𝘼𝘿𝙈𝙄𝙉 𝘼𝙉𝙅𝙄𝙉𝙂 𝘿𝙄 ** `{er}` **𝙂𝙍𝙊𝙐𝙋**"
    )


@poci_cmd(pattern="gucast(?: |$)(.*)")
async def gucast(event):
    xx = event.pattern_match.group(1)
    if xx:
        msg = xx
    elif event.is_reply:
        msg = await event.get_reply_message()
    else:
        return await edit_delete(event, "**𝘼𝙡𝙖𝙞 𝙇𝙪 𝙂𝙪𝙘𝙖𝙨𝙩² 𝙆𝙚𝙠 𝙅𝙖𝙢𝙚𝙩...**")
    kk = await edit_or_reply(event, "`𝙎𝙖𝙗𝙖𝙧𝙧... 𝙊𝙏𝙒 𝙆𝙞𝙧𝙞𝙢 𝙋𝙖𝙥 𝙏𝙏 𝙆𝙚 𝘿𝙊𝙄...`")
    er = 0
    done = 0
    async for x in event.client.iter_dialogs():
        if x.is_user and not x.entity.bot:
            chat = x.id
            if chat not in DEVS:
                try:
                    await event.client.send_message(chat, msg)
                    await asyncio.sleep(0.1)
                    done += 1
                except FloodWaitError as anj:
                    await asyncio.sleep(int(anj.seconds))
                    await event.client.send_message(chat, msg)
                    done += 1
                except BaseException:
                    er += 1
    await kk.edit(
        f"**𝙏𝙀𝙍𝙆𝙄𝙍𝙄𝙈 𝙆𝙀 𝙒𝘼𝙍𝙂𝘼 𝙎𝘼𝙉𝙂𝙀** `{done}` **𝘾𝙃𝘼𝙏, 𝙂𝘼𝙂𝘼𝙇 𝙒𝘼𝙍𝙂𝘼 𝙎𝙐𝘿𝘼𝙃 𝙈𝙀𝙉𝙄𝙉𝙂𝙂𝘼𝙇** `{er}` **𝘾𝙃𝘼𝙏**"
    )


CMD_HELP.update(
    {
        "gcast": f"**Plugin : **`gcast`\
        \n\n  •  **Syntax :** `{cmd}gcast` <text/reply media>\
        \n  •  **Function : **Mengirim Global Broadcast pesan ke Seluruh Grup yang kamu masuk. (Bisa Mengirim Media/Sticker)\
        \n\n  •  **Syntax :** `{cmd}gucast` <text/reply media>\
        \n  •  **Function : **Mengirim Global Broadcast pesan ke Seluruh Private Massage / PC yang masuk. (Bisa Mengirim Media/Sticker)\
    "
    }
)
