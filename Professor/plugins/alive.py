from telethon import events
from telethon.events import NewMessage
from telethon.tl.custom import Dialog
from telethon.tl.types import Channel, Chat, User
from telethon.errors import ChatSendInlineForbiddenError as noin
from telethon.errors.rpcerrorlist import BotMethodInvalidError as dedbot

from . import *

#-------------------------------------------------------------------------------

d3vil_pic = Config.ALIVE_PIC or "https://telegra.ph/file/5abfcff75e1930dcdfaf3.mp4"
pm_caption = "  __**๐ฅ๐ฅ๐๐ฏ๐ฌ๐ฃ๐ข๐ฐ๐ฐ๐ฌ๐ฏ ๐๐ฌ๐ฑ ๐ฆ๐ฐ ๐๐ฉ๐ฆ๐ณ๐ข๐ฅ๐ฅ**__\n\n"

pm_caption += f"**โโโโโโโโโโโโโโโโโโโโ**\n\n"
pm_caption += (
    f"                 โผ๐ ๐๐ฆ๐ง๐๐ฅโ\n  **ใ {d3vil_mention} ใ**\n\n"
)
pm_caption += f"โโโโโโโโโโโโโโโโโโโโ\n"
pm_caption += f"โ โขโณโ  `๐ณ๐พ๐๐พ๐๐๐๐:` `{tel_ver}` \n"
pm_caption += f"โ โขโณโ  `๐ต๐พ๐๐๐๐๐:` `{d3vil_ver}`\n"
pm_caption += f"โ โขโณโ  `๐ฒ๐๐ฝ๐:` `{is_sudo}`\n"
pm_caption += f"โ โขโณโ  `๐ข๐๐บ๐๐๐พ๐:` [๐น๐๐๐](https://t.me/Miss_AkshiV1_Updates)\n"
pm_caption += f"โ โขโณโ  `๐ข๐๐พ๐บ๐๐๐:` [๐ฟ๐๐๐๐๐๐๐๐ ๐ฐ๐๐๐](https://t.me/Professer_Ashu)\n"
pm_caption += f"โ โขโณโ  `๐ฎ๐๐๐พ๐:` [ฦคฦฆฦ ฦะฦงฦงฦ ฦฆ ฦฦงำฦฒ](https://t.me/Miss_Akshi)\n"
pm_caption += f"โโโโโโโโโโโโโโโโโโโโ\n"
pm_caption += " [โกREPOโก](https://github.com/darkphoenix2601/PROFESSOR_UB) ๐น [๐License๐](https://github.com/darkphoenix2601/PROFESSOR_UB/tree/d)"


#-------------------------------------------------------------------------------

@bot.on(d3vil_cmd(outgoing=True, pattern="alive$"))
@bot.on(sudo_cmd(pattern="alive$", allow_sudo=True))
async def up(d3vil):
    if d3vil.fwd_from:
        return
    await d3vil.get_chat()
    await d3vil.delete()
    await bot.send_file(d3vil.chat_id, d3vil_pic, caption=pm_caption)
    await d3vil.delete()

msg = f"""
**โก ๐๐ฏ๐ฌ๐ฃ๐ข๐ฐ๐ฐ๐ฌ๐ฏ ๐๐ฌ๐ฑ ๐ฆ๐ฐ ๐๐ฉ๐ฆ๐ณ๐ข โก**
{Config.ALIVE_MSG}
**๐ ๐ฑ๐๐ ๐๐๐๐๐๐ ๐**
**โผ๐ ๐๐ฆ๐ง๐๐ฅโ   :**  **ใ{d3vil_mention}ใ**
**โโโโโโโโโโโโโโโโโโโโ**
**โ โณโ  ๐ง๐ฒ๐น๐ฒ๐๐ต๐ผ๐ป :**  `{tel_ver}`
**โ โณโ  ๐3๐ฉ๐๐๐๐ข๐ง  :**  **{d3vil_ver}**
**โ โณโ  ๐จ๐ฝ๐๐ถ๐บ๐ฒ   :**  `{uptime}`
**โ โณโ  ๐๐ฏ๐๐๐ฒ    :**  **{abuse_m}**
**โ โณโ  ๐ฆ๐๐ฑ๐ผ      :**  **{is_sudo}**
**โโโโโโโโโโโโโโโโโโโโ
"""
botname = Config.BOT_USERNAME

@bot.on(d3vil_cmd(pattern="d3vil$"))
@bot.on(sudo_cmd(pattern="d3vil$", allow_sudo=True))
async def d3vil_a(event):
    try:
        d3vil = await bot.inline_query(botname, "alive")
        await d3vil[0].click(event.chat_id)
        if event.sender_id == d3krish:
            await event.delete()
    except (noin, dedbot):
        await eor(event, msg)


CmdHelp("alive").add_command(
  "alive", None, "Shows the Default Alive Message"
).add_command(
  "d3vil", None, "Shows Inline Alive Menu with more details."
).add()
