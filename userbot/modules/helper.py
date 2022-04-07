""" Userbot module for other small commands. """
from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP, owner
from userbot.utils import edit_or_reply, poci_cmd


@poci_cmd(pattern="ihelp$")
async def usit(event):
    await edit_or_reply(
        event,
        f"**Halo {owner} Kalo Anda Tidak Tau Perintah Untuk Memerintah Ku Ketik** `.help` Atau Bisa Minta Bantuan Ke:\n"
        f"❀ **GroupSupport :** [Grup Support](t.me/OuraaSupport)\n"
        f"❀ **Channel :** [Channel](t.me/OuraaProject)\n"
        f"❀ **OwnerRepo :** [Oura Cakep](t.me/Owaitingforyou)\n"
        f"❀ **Repo :** [OuraUserbot](https://github.com/Oura-Ubot/OuraUserbot)\n",
    )


@poci_cmd(pattern="listvar$")
async def var(event):
    await edit_or_reply(
        event,
        "**Daftar Lengkap Vars Dari OuraUserbot:** [KLIK DISINI](https://telegra.ph/ㅤ-04-04-5)",
    )


CMD_HELP.update(
    {
        "helper": f"**Plugin : **`helper`\
        \n\n  •  **Syntax :** `{cmd}ihelp`\
        \n  •  **Function : **Bantuan Untuk Man-Userbot.\
        \n\n  •  **Syntax :** `{cmd}listvar`\
        \n  •  **Function : **Melihat Daftar Vars.\
        \n\n  •  **Syntax :** `{cmd}repo`\
        \n  •  **Function : **Melihat Repository Man-Userbot.\
        \n\n  •  **Syntax :** `{cmd}string`\
        \n  •  **Function : **Link untuk mengambil String Man-Userbot.\
    "
    }
)
