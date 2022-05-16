# @Owaitingforyou
# Oura-Userbot
# Recode by @OuraCakep


from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP
from userbot.utils import edit_or_reply, poci_cmd


@poci_cmd(pattern="dekk(?: |$)(.*)")
async def _(event):
    await edit_or_reply(event, "**`𝙄𝙉𝙂𝘼𝙏 𝘿𝙀𝙆 𝘾𝙄𝙉𝙏𝘼 𝙏𝘼𝙆 𝙎𝙀𝙇𝘼𝙈𝘼𝙉𝙔𝘼 𝙄𝙉𝘿𝘼𝙃`**")


@poci_cmd(pattern="hha(?: |$)(.*)")
async def _(event):
    await edit_or_reply(event, "**`𝙎𝙀𝙉𝘿𝙄𝙍𝙄 𝙏𝘼𝙋𝙄 𝙏𝙄𝘿𝘼𝙆 𝙋𝙀𝙍𝙉𝘼𝙃 𝙈𝙀𝙍𝘼𝙎𝘼 𝙆𝙀𝙎𝙀𝙋𝙄𝘼𝙉`**") 


@poci_cmd(pattern="avv(?: |$)(.*)")
async def _(event):
    await edit_or_reply(event, "**`𝙃𝘼𝙉𝙔𝘼 𝙈𝙀𝙈𝘽𝘼𝙇𝘼𝙎 𝙋𝙀𝙎𝘼𝙉, 𝘽𝙐𝙆𝘼𝙉 𝙋𝙀𝙍𝘼𝙎𝘼𝘼𝙉 𝙈𝙐`**")


@poci_cmd(pattern="vyori(?: |$)(.*)")
async def _(event):
    await edit_or_reply(event, "**`𝙉𝙂𝙂𝘼 𝙐𝘿𝘼𝙃 𝙆𝙀𝙋𝙊, 𝙁𝙊𝙇𝙇𝙊𝙒 𝘼𝙅𝘼 @ALYCIAA_028`**") 

CMD_HELP.update(
    {
        "gipeaway": f"**Plugin : **`wartel`\
        \n\nㅤㅤ•**Syntax** : {cmd}a-z\
        \n•**Function : **Kata-Kata dari warga telegram\
    "
    })
