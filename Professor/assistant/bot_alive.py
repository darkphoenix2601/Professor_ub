from telethon import events
from . import *
#from d3vilbot import YOUR_NAME
from Professor import bot

D3VIL_USER = bot.me.first_name
d3krish = bot.uid
d3vil_mention = f"[{D3VIL_USER}](tg://user?id={d3krish})"

d3vil_pic = Config.ALIVE_PIC or "https://telegra.ph/file/5abfcff75e1930dcdfaf3.mp4"
pm_caption = "  __**๐ฅ๐ฅ๐3๐ฉ๐๐ ๐๐ฆ๐ฆ๐๐ฆ๐ง๐๐ก๐ง ๐๐ฆ ๐๐๐๐ฉ๐๐ฅ๐ฅ**__\n\n"

pm_caption += f"**โโโโโโโโโโโโโโโโโโโโ**\n\n"
pm_caption += (
    f"                 โผ๐ ๐๐ฆ๐ง๐๐ฅโ\n  **ใ {d3vil_mention} ใ**\n\n"
)
pm_caption += f"โโโโโโโโโโโโโโโโโโโโ\n"
pm_caption += f"โ โขโณโ  `๐ณ๐พ๐๐พ๐๐๐๐:` `1.23.0` \n"
pm_caption += f"โ โขโณโ  `๐ต๐พ๐๐๐๐๐:` `2.0.5`\n"
pm_caption += f"โ โขโณโ  `๐ข๐๐บ๐๐๐พ๐:` [๐น๐๐๐](https://t.me/D3VIL_SUPPORT)\n"
pm_caption += f"โ โขโณโ  `๐ข๐๐พ๐บ๐๐๐:` [๐ณ3๐บ๐๐ธ๐๐ท](https://t.me/D3_krish)\n"
pm_caption += f"โ โขโณโ  `๐ฎ๐๐๐พ๐:` [๐ณ3๐๐ธ๐ป๐ถ๐๐ป๐๐ท๐ฐ๐ฝ](https://t.me/D3VILGULSHAN)\n"
pm_caption += f"โโโโโโโโโโโโโโโโโโโโ\n"
pm_caption += " [โกREPOโก](https://github.com/TEAM-D3VIL/D3vilBot) ๐น [๐License๐](https://github.com/TEAM-D3VIL/D3vilBot/blob/main/LICENSE)"

@tgbot.on(events.NewMessage(pattern="^/alive"))
async def _(event):
    await tgbot.send_file(event.chat_id, d3vil_pic, caption=pm_caption)
