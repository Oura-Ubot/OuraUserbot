# Ported By @sintureveryday
# Kamu Kaya Kontol
# t.me/panyekyks

from time import sleep

from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP
from userbot.utils import poci_cmd


@poci_cmd(pattern="sok(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1.5)
    await typew.edit("**WOII**")
    sleep(1.5)
    await typew.edit("**KONTOL**")
    sleep(1.5)
    await typew.edit("**KALO MENTAL MASIH PATUNGAN**")
    sleep(1.5)
    await typew.edit("**GAUSAH SOK KERAS DEH**")
    sleep(1.5)
    await typew.edit("**GA KEREN LO BEGITU NGENTOT**")
