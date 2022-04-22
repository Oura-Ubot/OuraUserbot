from time import sleep

from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP
from userbot.utils import edit_or_reply, poci_cmd


@poci_cmd(pattern="p(?: |$)(.*)")
async def _(event):
    await event.client.send_message(
        event.chat_id,
        "**𝘼𝙎𝙎𝘼𝙇𝘼𝙈𝙐'𝘼𝙇𝘼𝙄𝙆𝙐𝙈 𝙂𝘼 𝙅𝘼𝙒𝘼𝘽 𝙋𝙆𝙄☭**",
        reply_to=event.reply_to_msg_id,
    )
    await event.delete()


@poci_cmd(pattern="P(?: |$)(.*)")
async def _(event):
    xx = await edit_or_reply(event, f"**𝘼𝙇𝙇𝙊 𝙎𝘼𝙔𝘼𝙉𝙂...🥺**")
    sleep(2)
    await xx.edit("**𝘼𝙎𝙎𝘼𝙇𝘼𝙈𝙐'𝘼𝙇𝘼𝙄𝙆𝙐𝙈...𝙂𝘼 𝙅𝘼𝙒𝘼𝘽 𝙋𝙆𝙄**")


@poci_cmd(pattern="l(?: |$)(.*)")
async def _(event):
    await event.client.send_message(
        event.chat_id, "**𝙒𝘼'𝘼𝙇𝘼𝙄𝙆𝙐𝙈𝙎𝘼𝙇𝘼𝙈 𝙉𝙂𝙀𝙉𝙏𝙊𝙏𝙏𝙏...**", reply_to=event.reply_to_msg_id
    )
    await event.delete()


@poci_cmd(pattern="L(?: |$)(.*)")
async def _(event):
    xx = await edit_or_reply(event, f"**𝘼𝙎𝙏𝘼𝙂𝘼𝙔... 𝙂𝘼 𝙅𝘼𝙒𝘼𝘽 𝙋𝙆𝙄**")
    sleep(2)
    await xx.edit("**𝙒𝘼'𝘼𝙇𝘼𝙄𝙆𝙐𝙈𝙎𝘼𝙇𝘼𝙈 𝙅𝘼𝙉𝘾𝙊𝙆...**")



CMD_HELP.update(
    {
        "salam": f"**Plugin : **`salam`\
        \n\nㅤㅤ•**Syntax** : {cmd}p\
        \n•**Function : **Assalamualaikum Dulu Biar Sopan..\
        \n\nㅤㅤ•**Syntax** : {cmd}P\
        \n•**Function : **salam Kenal dan salam\
        \n\nㅤㅤ•**Syntax** : {cmd}l\
        \n•**Function : **Untuk Menjawab salam\
        \n\nㅤㅤ•**Syntax** :{cmd}L\
        \n•**Function : **Untuk menjawab salam\
    "
    })
