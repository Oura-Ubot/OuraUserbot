# 🍀 © @tofik_dn
# ⚠️ Do not remove credits

import requests
import random
from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP
from userbot.utils import poci_cmd
from telethon.tl.types import InputMessagesFilterVideo


@poci_cmd(pattern="asupan$")
async def _(event):
    try:
        asupannya = [
            asupan
            async for asupan in event.client.iter_messages(
                "@Asupan_Pocong", filter=InputMessagesFilterVideo
            )
        ]
        await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(asupannya),
            caption=f"𝙉𝙞𝙝 𝘼𝙨𝙪𝙥𝙖𝙣 𝘽𝙪𝙖𝙩 𝙇𝙪 𝙔𝙖𝙣𝙜 𝙇𝙖𝙜𝙞 𝙎𝙖𝙣𝙜𝙚...🥵",
        )
        await event.delete()
    except Exception:
        await event.edit("Tidak bisa menemukan video asupan.")


@poci_cmd(pattern="wibu$")
async def _(event):
    try:
        wibukntl = [
            wibu
            async for wibu in event.client.iter_messages(
                "@pocongwibu", filter=InputMessagesFilterVideo
            )
        ]
        await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(wibukntl),
            caption=f"𝙒𝙞𝙗𝙪𝙪 𝙆𝙤𝙣𝙩𝙤𝙡 𝘽𝙖𝙪 𝘽𝙖𝙬𝙖𝙣𝙜𝙜 𝙖𝙬𝙠𝙬𝙠𝙬𝙠...🤪",
        )
        await event.delete()
    except Exception:
        await event.edit("Tidak bisa menemukan video asupan.")


@poci_cmd(pattern="chika$")
async def _(event):
    try:
        response = requests.get("https://api-alphabot.herokuapp.com/api/asupan/chika?apikey=Alphabot").json()
        await event.client.send_file(event.chat_id, response["url"])
        await event.delete()
    except Exception:
        await event.edit("**Tidak bisa menemukan video chikakiku.**")


CMD_HELP.update(
    {
        "asupan": f"**Plugin : **`asupan`\
        \n\n  •  **Syntax :** `{cmd}asupan`\
        \n  •  **Function : **Untuk Mengirim video asupan secara random.\
        \n\n  •  **Syntax :** `{cmd}chika`\
        \n  •  **Function : **Untuk Mengirim video chikakiku secara random.\
    "
    }
)

CMD_HELP.update(
    {
        "wibu": f"**Plugin : **`Wibu`\
        \n\n  •  **Syntax :** `{cmd}wibu`\
        \n  •  **Function : **Mengirim secara random video anime\
    "
    }
)
