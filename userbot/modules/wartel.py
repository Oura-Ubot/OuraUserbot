# @Owaitingforyou
# Oura-Userbot
# Recode by @OuraCakep


from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP
from userbot.utils import edit_or_reply, poci_cmd


@poci_cmd(pattern="dekk(?: |$)(.*)")
async def _(event):
    await edit_or_reply(event, "**`𝙄𝙉𝙂𝘼𝙏 𝘿𝙀𝙆 𝘾𝙄𝙉𝙏𝘼 𝙏𝘼𝙆 𝙎𝙀𝙇𝘼𝙈𝘼𝙉𝙔𝘼 𝙄𝙉𝘿𝘼𝙃`**")


CMD_HELP.update(
    {
        "gipeaway": f"**Plugin : **`wartel`\
        \n\nㅤㅤ•**Syntax** : {cmd}a-z\
        \n•**Function : **Kata-Kata dari warga telegram\
    "
    })
