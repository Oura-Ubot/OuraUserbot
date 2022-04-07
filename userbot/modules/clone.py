# Coded by KenHV
# FORM Man-Userbot <https://github.com/mrismanaziz/Man-Userbot>
# ReCode by @OuraCakep

from telethon.tl.functions.account import UpdateProfileRequest
from telethon.tl.functions.photos import DeletePhotosRequest, UploadProfilePhotoRequest
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import InputPhoto

from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP, DEVS, LOGS, STORAGE
from userbot.utils import edit_or_reply, poci_cmd

if not hasattr(STORAGE, "userObj"):
    STORAGE.userObj = False


@poci_cmd(pattern="clone ?(.*)")
async def impostor(event):
    inputArgs = event.pattern_match.group(1)
    xx = await edit_or_reply(event, "`Otw Nyamar Jadi Anak Haram...`")
    if "restore" in inputArgs:
        await event.edit("**`Kembali Jadi Anak Shaleh...`**")
        if not STORAGE.userObj:
            return await xx.edit("**`Masih Jadi Anak Shaleh, Clone Dulu Anak Haramnya!!!**")
        await updateProfile(event, STORAGE.userObj, restore=True)
        return await xx.edit("**`Berhasil Menjadi Jadi Anak Shaleh Kembali...🐣`**")
    if inputArgs:
        try:
            user = await event.client.get_entity(inputArgs)
        except BaseException:
            return await xx.edit("**Username/ID tidak valid.**")
        userObj = await event.client(GetFullUserRequest(user))
    elif event.reply_to_msg_id:
        replyMessage = await event.get_reply_message()
        if replyMessage.sender_id in DEVS:
            return await xx.edit(
                "**`Ampe Kiamat Juga Ga Akan Bisa Gblk Lu Clone Tuhan Lu Sendiri!!!😡`**"
            )
        if replyMessage.sender_id is None:
            return await xx.edit("**`Ga Bakal Bisa Gblkkk Nyamar Jadi Admin Anonim Mah Tolol 😭`**")
        userObj = await event.client(GetFullUserRequest(replyMessage.sender_id))
    else:
        return await xx.edit("**Ketik** `.help clone` **Kalo Mau Cosplay Jadi Anak Haram.**")

    if not STORAGE.userObj:
        STORAGE.userObj = await event.client(GetFullUserRequest(event.sender_id))

    LOGS.info(STORAGE.userObj)
    await xx.edit("**Otw Nyamar Jadi Anak Haram...**")
    await updateProfile(event, userObj)
    await xx.edit("**`Horeee Berhasil... Aku Anak Haram Dan Kamu Anak Anjing... 😙**")


async def updateProfile(event, userObj, restore=False):
    firstName = (
        "Deleted Account"
        if userObj.user.first_name is None
        else userObj.user.first_name
    )
    lastName = "" if userObj.user.last_name is None else userObj.user.last_name
    userAbout = userObj.about if userObj.about is not None else ""
    userAbout = "" if len(userAbout) > 70 else userAbout
    if restore:
        userPfps = await event.client.get_profile_photos("me")
        userPfp = userPfps[0]
        await event.client(
            DeletePhotosRequest(
                id=[
                    InputPhoto(
                        id=userPfp.id,
                        access_hash=userPfp.access_hash,
                        file_reference=userPfp.file_reference,
                    )
                ]
            )
        )
    else:
        try:
            userPfp = userObj.profile_photo
            pfpImage = await event.client.download_media(userPfp)
            await event.client(
                UploadProfilePhotoRequest(await event.client.upload_file(pfpImage))
            )
        except BaseException:
            pass
    await event.client(
        UpdateProfileRequest(about=userAbout, first_name=firstName, last_name=lastName)
    )


CMD_HELP.update(
    {
        "clone": f"**Plugin : **`clone`\
        \n\n  •  **Syntax :** `{cmd}clone` <reply/username/ID>\
        \n  •  **Function : **Untuk mengclone identitas dari username/ID Telegram yang diberikan.\
        \n\n  •  **Syntax :** `{cmd}clone restore`\
        \n  •  **Function : **Mengembalikan ke identitas asli anda.\
        \n\n  •  **NOTE :** `{cmd}clone restore` terlebih dahulu sebelum mau nge `{cmd}clone` lagi.\
    "
    }
)
