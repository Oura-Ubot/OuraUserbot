from time import sleep

from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP
from userbot.utils import edit_or_reply, poci_cmd


@poci_cmd(pattern="p(?: |$)(.*)")
async def _(event):
    await event.client.send_message(
        event.chat_id,
        "**πΌπππΌππΌππ'πΌππΌππππ ππΌ ππΌππΌπ½ πππβ­**",
        reply_to=event.reply_to_msg_id,
    )
    await event.delete()


@poci_cmd(pattern="P(?: |$)(.*)")
async def _(event):
    xx = await edit_or_reply(event, f"**πΌπππ ππΌππΌππ...π₯Ί**")
    sleep(2)
    await xx.edit("**πΌπππΌππΌππ'πΌππΌππππ...ππΌ ππΌππΌπ½ πππ**")


@poci_cmd(pattern="l(?: |$)(.*)")
async def _(event):
    await event.client.send_message(
        event.chat_id, "**ππΌ'πΌππΌππππππΌππΌπ πππππππππ...**", reply_to=event.reply_to_msg_id
    )
    await event.delete()


@poci_cmd(pattern="L(?: |$)(.*)")
async def _(event):
    xx = await edit_or_reply(event, f"**πΌπππΌππΌπ... ππΌ ππΌππΌπ½ πππ**")
    sleep(2)
    await xx.edit("**ππΌ'πΌππΌππππππΌππΌπ ππΌππΎππ...**")



CMD_HELP.update(
    {
        "salam": f"**Plugin : **`salam`\
        \n\nγ€γ€β’**Syntax** : {cmd}p\
        \nβ’**Function : **Assalamualaikum Dulu Biar Sopan..\
        \n\nγ€γ€β’**Syntax** : {cmd}P\
        \nβ’**Function : **salam Kenal dan salam\
        \n\nγ€γ€β’**Syntax** : {cmd}l\
        \nβ’**Function : **Untuk Menjawab salam\
        \n\nγ€γ€β’**Syntax** :{cmd}L\
        \nβ’**Function : **Untuk menjawab salam\
    "
    })
