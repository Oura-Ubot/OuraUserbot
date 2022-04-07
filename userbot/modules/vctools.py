# Copyright (C) 2021 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.
#
# Ported by @mrismanaziz
# FROM Man-Userbot <https://github.com/mrismanaziz/Man-Userbot>
#
# Kalo mau ngecopas, jangan hapus credit ya goblok

from pytgcalls import StreamType
from pytgcalls.exceptions import AlreadyJoinedError
from pytgcalls.types.input_stream import InputAudioStream, InputStream
from telethon.tl.functions.channels import GetFullChannelRequest as getchat
from telethon.tl.functions.phone import CreateGroupCallRequest as startvc
from telethon.tl.functions.phone import DiscardGroupCallRequest as stopvc
from telethon.tl.functions.phone import EditGroupCallTitleRequest as settitle
from telethon.tl.functions.phone import GetGroupCallRequest as getvc
from telethon.tl.functions.phone import InviteToGroupCallRequest as invitetovc

from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP, call_py
from userbot.utils import edit_delete, edit_or_reply, poci_cmd


async def get_call(event):
    mm = await event.client(getchat(event.chat_id))
    xx = await event.client(getvc(mm.full_chat.call, limit=1))
    return xx.call


def user_list(l, n):
    for i in range(0, len(l), n):
        yield l[i : i + n]


@poci_cmd(pattern="startvc$")
async def start_voice(c):
    me = await c.client.get_me()
    chat = await c.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    if not admin and not creator:
        await edit_delete(c, f"**Tololl {me.first_name} Lu Bukan Admin Tod.👮**")
        return
    try:
        await c.client(startvc(c.chat_id))
        await edit_or_reply(c, "`Gudang Dosa Telah Di Buka...`")
    except Exception as ex:
        await edit_delete(c, f"**ERROR:** `{ex}`")


@poci_cmd(pattern="stopvc$")
async def stop_voice(c):
    me = await c.client.get_me()
    chat = await c.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    if not admin and not creator:
        await edit_delete(c, f"**Tololl {me.first_name} Lu Bukan Admin Tod.👮**")
        return
    try:
        await c.client(stopvc(await get_call(c)))
        await edit_or_reply(c, "`Gudang Dosa Di tutup! Silahkan Tobat..`")
    except Exception as ex:
        await edit_delete(c, f"**ERROR:** `{ex}`")


@poci_cmd(pattern="vcinvite")
async def _(c):
    xxnx = await edit_or_reply(c, "`Mengajak Anak Shaleh Untuk Berbuat Dosa...`")
    users = []
    z = 0
    async for x in c.client.iter_participants(c.chat_id):
        if not x.bot:
            users.append(x.id)
    botpoci = list(user_list(users, 6))
    for p in botpoci:
        try:
            await c.client(invitetovc(call=await get_call(c), users=p))
            z += 6
        except BaseException:
            pass
    await xxnx.edit(f"`{z}` **Anak Shaleh Berhasil diundang ke VCS**")


@poci_cmd(pattern="vctitle(?: |$)(.*)")
async def change_title(e):
    title = e.pattern_match.group(1)
    me = await e.client.get_me()
    chat = await e.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    if not title:
        return await edit_delete(e, "**Silahkan Masukan Title Obrolan Suara Grup**")

    if not admin and not creator:
        await edit_delete(e, f"**Tololl {me.first_name} Lu Bukan Admin Tod.👮**")
        return
    try:
        await e.client(settitle(call=await get_call(e), title=title.strip()))
        await edit_or_reply(e, f"**Berhasil Mengubah Judul VCS Menjadi** `{title}`")
    except Exception as ex:
        await edit_delete(e, f"**ERROR:** `{ex}`")


@poci_cmd(pattern="joinvc(?: |$)(.*)")
async def _(event):
    Pocong = await edit_or_reply(event, "`Ikutan VCS...`")
    if len(event.text.split()) > 1:
        chat_id = event.text.split()[1]
        try:
            chat_id = await event.client.get_peer_id(int(chat_id))
        except Exception as e:
            return await Pocong.edit(f"**ERROR:** `{e}`")
    else:
        chat_id = event.chat_id
    file = "./userbot/resources/audio-pocong.mp3"
    if chat_id:
        try:
            await call_py.join_group_call(
                chat_id,
                InputStream(
                    InputAudioStream(
                        file,
                    ),
                ),
                stream_type=StreamType().local_stream,
            )
            await Pocong.edit(
                f"❀ **Berhasil Join Ke Gudang Dosa**\n└ **Chat ID:** `{chat_id}`"
            )
        except AlreadyJoinedError:
            await call_py.leave_group_call(chat_id)
            await edit_delete(
                Pocong,
                "**ERROR:** `Karena akun sedang berada di Gudang Dosa`\n\n• Silahkan coba `.joinvc` lagi",
                45,
            )
        except Exception as e:
            await Pocong.edit(f"**INFO:** `{e}`")


@poci_cmd(pattern="leavevc(?: |$)(.*)")
async def vc_end(event):
    Pocong = await edit_or_reply(event, "`Proses Tobat...`")
    if len(event.text.split()) > 1:
        chat_id = event.text.split()[1]
        try:
            chat_id = await event.client.get_peer_id(int(chat_id))
        except Exception as e:
            return await Pocong.edit(f"**ERROR:** `{e}`")
    else:
        chat_id = event.chat_id
    if chat_id:
        try:
            await call_py.leave_group_call(chat_id)
            await edit_delete(
                Pocong,
                f"❀ **Berhasil Tobat dari Gudang Dosa**\n└ **Chat ID:** `{chat_id}`",
            )
        except Exception as e:
            await Pocong.edit(f"**INFO:** `{e}`")


CMD_HELP.update(
    {
        "vctools": f"**Plugin : **`vctools`\
        \n\n  •  **Syntax :** `{cmd}startvc`\
        \n  •  **Function : **Untuk Memulai voice chat group\
        \n\n  •  **Syntax :** `{cmd}stopvc`\
        \n  •  **Function : **Untuk Memberhentikan voice chat group\
        \n\n  •  **Syntax :** `{cmd}joinvc` atau `{cmd}joinvc` <chatid/username gc>\
        \n  •  **Function : **Untuk Bergabung ke voice chat group\
        \n\n  •  **Syntax :** `{cmd}leavevc` atau `{cmd}leavevc` <chatid/username gc>\
        \n  •  **Function : **Untuk Turun dari voice chat group\
        \n\n  •  **Syntax :** `{cmd}vctitle` <title vcg>\
        \n  •  **Function : **Untuk Mengubah title/judul voice chat group\
        \n\n  •  **Syntax :** `{cmd}vcinvite`\
        \n  •  **Function : **Mengundang Member group ke voice chat group (anda harus sambil bergabung ke OS/VCG)\
    "
    }
)
