import asyncio
from datetime import datetime
import io
import os
from pathlib import Path

from telethon import events, functions, types
from telethon.tl.types import InputMessagesFilterDocument

from . import *


@bot.on(d3vil_cmd(pattern=r"cmds"))
@bot.on(sudo_cmd(pattern=r"cmds", allow_sudo=True))
async def kk(event):
    if event.fwd_from:
        return
    reply_to_id = event.message.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    cmd = "ls d3vilbot/plugins"
    thumb = d3vil_logo
    process = await asyncio.create_subprocess_sd3vil(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    o = stdout.decode()
    _o = o.split("\n")
    o = "\n".join(_o)
    OUTPUT = f"π«πππ ππΏ π―ππππππ ππ π»ππ :- \n\n{o}\n\n<><><><><><><><><><><><><><><><><><><><><><><><>\nHELP:- π¨πΏ πππ ππΊππ ππ ππππ πππΎ πΌππππΊππ½π πΏππ πΊ ππππππ, π½π :- \n.plinfo <ππππππ ππΊππΎ> πππππππ πππΎ < > π»ππΊπΌππΎππ. \ππ©πππ {d3vil_grp} πΏππ πππΎππ."
    if len(OUTPUT) > 69:
        with io.BytesIO(str.encode(OUTPUT)) as out_file:
            out_file.name = "cmd_list.text"
            d3vil_file = await bot.send_file(
                event.chat_id,
                out_file,
                force_document=True,
                allow_cache=False,
                thumb=thumb,
                reply_to=reply_to_id,
            )
            await edit_or_reply(d3vil_file, f"Output Too Large. This is the file for the list of plugins in bot.\n\n**BY :-** {D3VIL_USER}")
            await event.delete()


@bot.on(d3vil_cmd(pattern=r"send (?P<shortname>\w+)", outgoing=True))
@bot.on(sudo_cmd(pattern=r"send (?P<shortname>\w+)", allow_sudo=True))
async def send(event):
    if event.fwd_from:
        return
    message_id = event.message.id
    thumb = d3vil_logo
    input_str = event.pattern_match.group(1)
    omk = f"**β’ α΄Κα΄Ι’ΙͺΙ΄ Ι΄α΄α΄α΄ β** `{input_str}`\n**β’ α΄α΄Κα΄α΄α΄α΄α΄ ΚΚ β** {d3vil_mention}\n\nβ‘ **[ΚΙΙ’ΙΥΌΙaΚΚ α΄? α΄α΄α΄α΄ α΄3α΄ ΙͺΚ]({chnl_link})** β‘"
    the_plugin_file = "./d3vilbot/plugins/{}.py".format(input_str)
    if os.path.exists(the_plugin_file):
        lauda = await event.client.send_file(
            event.chat_id,
            the_plugin_file,
            thumb=thumb,
            caption=omk,
            force_document=True,
            allow_cache=False,
            reply_to=message_id,
        )
        await event.delete()
    else:
        await eod(event, "π₯πππΎ πππ πΏππππ½..... πͺπΎπ")


@bot.on(d3vil_cmd(pattern="install ?(.*)"))
@bot.on(sudo_cmd(pattern="install ?(.*)", allow_sudo=True))
async def install(event):
    if event.fwd_from:
        return
    b = 1
    owo = event.text[9:]
    d3vil = await eor(event, "__Installing.__")
    if event.reply_to_msg_id:
        try:
            downloaded_file_name = await event.client.download_media(  # pylint:disable=E0602
                await event.get_reply_message(),
                "./d3vilbot/plugins/"  # pylint:disable=E0602
            )
            if owo != "-f":
                op = open(downloaded_file_name, "r")
                rd = op.read()
                op.close()
                try:
                    for harm in HARMFUL:
                        if harm in rd:
                            os.remove(downloaded_file_name)
                            return await d3vil.edit(f"**β οΈ WARNING !!** \n\n__Replied plugin file contains some harmful & hacking codes. Please consider checking the file. If you still want to install then use__ `{hl}install -f`. \n\n**Codes Detected :** \nβ’ {harm}")
                except BaseException:
                    pass
            if "(" not in downloaded_file_name:
                path1 = Path(downloaded_file_name)
                shortname = path1.stem
                load_module(shortname.replace(".py", ""))
                if shortname in CMD_LIST:
                    string = "**Commands found in** `{}`\n".format((os.path.basename(downloaded_file_name)))
                    for i in CMD_LIST[shortname]:
                        string += "  β’  `" + i 
                        string += "`\n"
                        if b == 1:
                            a = "__Installing..__"
                            b = 2
                        else:
                            a = "__Installing...__"
                            b = 1
                        await d3vil.edit(a)
                    return await d3vil.edit(f"βοΈ **πΈππππππππ ππππππ** :- `{shortname}` \nβ¨ π±π :- {d3vil_mention}\n\n{string}\n\n        β‘ **[ΚΙΙ’ΙΥΌΙaΚΚ α΄? α΄α΄α΄α΄ α΄3α΄ ΙͺΚ]({chnl_link})** β‘", link_preview=False)
                return await d3vil.edit(f"Installed module `{os.path.basename(downloaded_file_name)}`")
            else:
                os.remove(downloaded_file_name)
                return await eod(d3vil, f"**Failed to Install** \n`Error`\nModule already installed or unknown format")
        except Exception as e: 
            await eod(d3vil, f"**Failed to Install** \n`Error`\n{str(e)}")
            return os.remove(downloaded_file_name)

@bot.on(d3vil_cmd(pattern=r"uninstall (?P<shortname>\w+)", outgoing=True))
@bot.on(sudo_cmd(pattern=r"uninstall (?P<shortname>\w+)", allow_sudo=True))
async def uninstall(d3vilkrish):
    if d3vilkrish.fwd_from:
        return
    shortname = d3vilkrish.pattern_match["shortname"]
    dir_path =f"./d3vilbot/plugins/{shortname}.py"
    try:
        remove_plugin(shortname)
        os.remove(dir_path)
        await eod(d3vilkrish, f"Uninstalled `{shortname}` successfully")
    except OSError as e:
        await d3vilkrish.edit("Error: %s : %s" % (dir_path, e.strerror))


@bot.on(d3vil_cmd(pattern=r"unload (?P<shortname>\w+)$"))
@bot.on(sudo_cmd(pattern=r"unload (?P<shortname>\w+)$", allow_sudo=True))
async def unload(event):
    if event.fwd_from:
        return
    shortname = event.pattern_match["shortname"]
    try:
        remove_plugin(shortname)
        await event.edit(f"π²ππΌπΌπΎπππΏππππ πππππΊπ½πΎπ½ `{shortname}`")
    except Exception as e:
        await event.edit(
            "Successfully unloaded {shortname}\n{}".format(
                shortname, str(e)
            )
        )


@bot.on(d3vil_cmd(pattern=r"load (?P<shortname>\w+)$"))
@bot.on(sudo_cmd(pattern=r"load (?P<shortname>\w+)$", allow_sudo=True))
async def load(event):
    if event.fwd_from:
        return
    shortname = event.pattern_match["shortname"]
    try:
        try:
            remove_plugin(shortname)
        except BaseException:
            pass
        load_module(shortname)
        await event.edit(f"π²ππΌπΌπΎπππΏππππ πππΊπ½πΎπ½ `{shortname}`")
    except Exception as e:
        await event.edit(
            f"Sorry, could not load {shortname} because of the following error.\n{str(e)}"
        )

CmdHelp("core").add_command(
  "install", "<reply to a .py file>", "Installs the replied python file if suitable to π3π³π¦π©ππ¬π±'s codes."
).add_command(
  "uninstall", "<plugin name>", "Uninstalls the given plugin from π3π³π¦π©ππ¬π±. To get that again do .restart", "uninstall alive"
).add_command(
  "load", "<plugin name>", "Loades the unloaded plugin to your userbot", "load alive"
).add_command(
  "unload", "<plugin name>", "Unloads the plugin from your userbot", "unload alive"
).add_command(
  "send", "<file name>", "Sends the given file from your userbot server, if any.", "send alive"
).add_command(
  "cmds", None, "Gives out the list of modules in D3vilBot."
).add()


