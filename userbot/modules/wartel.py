# @Owaitingforyou
# Oura-Userbot
# Recode by @OuraCakep


from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP
from userbot.utils import edit_or_reply, poci_cmd


@poci_cmd(pattern="dekk(?: |$)(.*)")
async def _(event):
    await edit_or_reply(event, "**`ππππΌπ πΏππ πΎππππΌ ππΌπ ππππΌππΌπππΌ πππΏπΌπ`**")


@poci_cmd(pattern="hha(?: |$)(.*)")
async def _(event):
    await edit_or_reply(event, "**`ππππΏπππ ππΌππ πππΏπΌπ πππππΌπ ππππΌππΌ πππππππΌπ`**") 


@poci_cmd(pattern="avv(?: |$)(.*)")
async def _(event):
    await edit_or_reply(event, "**`ππΌπππΌ ππππ½πΌππΌπ ππππΌπ, π½πππΌπ ππππΌππΌπΌπ ππ`**")


@poci_cmd(pattern="vyori(?: |$)(.*)")
async def _(event):
    await edit_or_reply(event, "**`ππππΌ πππΌπ ππππ, ππππΏπππ ππππππ ππ πΌππΌ @alyciaa_028`**") 

CMD_HELP.update(
    {
        "gipeaway": f"**Plugin : **`wartel`\
        \n\nγ€γ€β’**Syntax** : {cmd}a-z\
        \nβ’**Function : **Kata-Kata dari warga telegram\
    "
    })
