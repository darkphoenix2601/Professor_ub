from telethon import events
from telethon.tl.functions.channels import EditAdminRequest
from telethon.tl.types import ChatAdminRights
import asyncio
from Professor.sql.gban_sql import is_gbanned, gbaner, ungbaner, all_gbanned
from Professor.sql import gmute_sql as gsql
from . import *


@bot.on(d3vil_cmd(pattern=r"gban ?(.*)"))
@bot.on(sudo_cmd(pattern=r"gban ?(.*)", allow_sudo=True))
async def _(event):
    d3vil = await eor(event, "`Gbanning...`")
    reason = ""
    if event.reply_to_msg_id:
        userid = (await event.get_reply_message()).sender_id
        try:
            reason = event.text.split(" ", maxsplit=1)[1]
        except IndexError:
            reason = ""
    elif event.pattern_match.group(1):
        usr = event.text.split(" ", maxsplit=2)[1]
        userid = await get_user_id(usr)
        try:
            reason = event.text.split(" ", maxsplit=2)[2]
        except IndexError:
            reason = ""
    elif event.is_private:
        userid = (await event.get_chat()).id
        try:
            reason = event.text.split(" ", maxsplit=1)[1]
        except IndexError:
            reason = ""
    else:
        return await eod(d3vil, "**To gban a user i need a userid or reply to his/her message!!**")
    name = (await event.client.get_entity(userid)).first_name
    chats = 0
    if userid == d3krish:
        return await eod(d3vil, "🥴 **Nashe me hai kya lawde ‽**")
    if str(userid) in DEVLIST:
        return await eod(d3vil, "😑 **GBan my creator ?¿ Really‽**")
    if is_gbanned(userid):
        return await eod(
            d3vil,
            "This kid is already gbanned and added to my **Gban Watch!!**",
        )
    async for gfuck in event.client.iter_dialogs():
        if gfuck.is_group or gfuck.is_channel:
            try:
                await event.client.edit_permissions(gfuck.id, userid, view_messages=False)
                chats += 1
            except BaseException:
                pass
    gbaner(userid)
    gmsg = f"🥴 𝚃𝙷𝙸𝚂 𝚄𝚂𝙴𝚁 𝙶𝙻𝙾𝙱𝙰𝙻 𝙱𝙰𝙽  【[{name}](tg://user?id={userid})】 **𝙱𝚈 :** 『{d3vil_mention}』\n\n📍 𝙰𝚍𝚍𝚎𝚍 𝚝𝚘 𝙶𝚋𝚊𝚗 𝚆𝚊𝚝𝚌𝚑!!\n** 𝚃𝚘𝚝𝚊𝚕 𝙲𝚑𝚊𝚝𝚜 :**  `{chats}`"
    if reason != "":
        gmsg += f"\n**𝚁𝚎𝚊𝚜𝚘𝚗 ➳➠ :**  `{reason}`"
    ogmsg = f"[{name}](tg://user?id={userid}) **𝙸𝚜 𝚗𝚘𝚠 𝙶𝙱𝚊𝚗𝚗𝚎𝚍 𝚋𝚢** {d3vil_mention} **in**  `{chats}`  **𝙲𝚑𝚊𝚝𝚜!! 😏**\n\n**📍 𝙰𝚕𝚜𝚘 𝙰𝚍𝚍𝚎𝚍 𝚝𝚘 𝙶𝚋𝚊𝚗 𝚆𝚊𝚝𝚌𝚑!!**"
    if reason != "":
        ogmsg += f"\n**𝚁𝚎𝚊𝚜𝚘𝚗 ➳➠ :**  `{reason}`"
    if Config.ABUSE == "ON":
        await bot.send_file(event.chat_id, cjb, caption=gmsg)
    else:
        await d3vil.edit(ogmsg)


@bot.on(d3vil_cmd(pattern=r"ungban ?(.*)"))
@bot.on(sudo_cmd(pattern=r"ungban ?(.*)", allow_sudo=True))
async def _(event):
    d3vil = await eor(event, "`Ungban in progress...`")
    if event.reply_to_msg_id:
        userid = (await event.get_reply_message()).sender_id
    elif event.pattern_match.group(1):
        userid = await get_user_id(event.pattern_match.group(1))
    elif event.is_private:
        userid = (await event.get_chat()).id
    else:
        return await eod(d3vil, "`Reply to a user or give their userid... `")
    name = (await event.client.get_entity(userid)).first_name
    chats = 0
    if not is_gbanned(userid):
        return await eod(d3vil, "`User is not gbanned.`")
    async for gfuck in event.client.iter_dialogs():
        if gfuck.is_group or gfuck.is_channel:
            try:
                await event.client.edit_permissions(gfuck.id, userid, view_messages=True)
                chats += 1
            except BaseException:
                pass
    ungbaner(userid)
    await d3vil.edit(
        f"📍 [{name}](tg://user?id={userid}) **𝚒𝚜 𝚗𝚘𝚠 𝚄𝚗𝚐𝚋𝚊𝚗𝚗𝚎𝚍 𝚏𝚛𝚘𝚖 `{chats}` 𝚌𝚑𝚊𝚝𝚜 𝚊𝚗𝚍 𝚛𝚎𝚖𝚘𝚟𝚎𝚍 𝚏𝚛𝚘𝚖 𝙶𝚋𝚊𝚗 𝚆𝚊𝚝𝚌𝚑!!**",
    )


@bot.on(d3vil_cmd(pattern="listgban$"))
@bot.on(sudo_cmd(pattern="listgban$", allow_sudo=True))
async def already(event):
    gbanned_users = all_gbanned()
    GBANNED_LIST = "**Gbanned Users :**\n"
    if len(gbanned_users) > 0:
        for user in gbanned_users:
            name = (await bot.get_entity(int(user))).first_name
            GBANNED_LIST += f"📍 [{name}](tg://user?id={user.chat_id})\n"
    else:
        GBANNED_LIST = "No Gbanned Users!!"
    await edit_or_reply(event, GBANNED_LIST)


@bot.on(events.ChatAction)
async def _(event):
    if event.user_joined or event.added_by:
        user = await event.get_user()
        chat = await event.get_chat()
        if is_gbanned(str(user.id)):
            if chat.admin_rights:
                try:
                    await event.client.edit_permissions(
                        chat.id,
                        user.id,
                        view_messages=False,
                    )
                    gban_watcher = f"⚠️⚠️**𝚆𝚊𝚛𝚗𝚒𝚗𝚐**⚠️⚠️\n\n`Gbanned User Joined the chat!!`\n**⚜️ Victim Id :**  [{user.first_name}](tg://user?id={user.id})\n"
                    gban_watcher += f"**🔥 𝙰𝚌𝚝𝚒𝚘𝚗 🔥**  \n`Banned this piece of shit....` **AGAIN!**"
                    await event.reply(gban_watcher)
                except BaseException:
                    pass


@bot.on(d3vil_cmd(pattern=r"gkick ?(.*)"))
@bot.on(sudo_cmd(pattern=r"gkick ?(.*)", allow_sudo=True))
async def gkick(event):
    d3vil = await eor(event, "`Kicking globally...`")
    if event.reply_to_msg_id:
        userid = (await event.get_reply_message()).sender_id
    elif event.pattern_match.group(1):
        userid = await get_user_id(event.pattern_match.group(1))
    elif event.is_private:
        userid = (await event.get_chat()).id
    else:
        return await eod(d3vil, "`Reply to some msg or add their id.`")
    name = (await event.client.get_entity(userid)).first_name
    chats = 0
    if userid == d3krish:
        return await eod(d3vil, "**🥴 Nashe me hai kya lawde!!**")
    if str(userid) in DEVLIST:
        return await eod(d3vil, "**😪 I'm not going to gkick my developer!!**")
    async for gkick in event.client.iter_dialogs():
        if gkick.is_group or gkick.is_channel:
            try:
                await bot.kick_participant(gkick.id, userid)
                chats += 1
            except BaseException:
                pass
    gkmsg = f"🏃 **Globally Kicked** [{name}](tg://user?id={userid})'s butts !! \n\n📝 **Chats :**  `{chats}`"
    if Config.ABUSE == "ON":
        await bot.send_file(event.chat_id, cjb, caption=gkmsg)
    else:
        await d3vil.edit(gkmsg)


@bot.on(d3vil_cmd(pattern=r"gmute ?(\d+)?"))
@bot.on(sudo_cmd(allow_sudo=True, pattern=r"gmute ?(\d+)?"))
async def gm(event):
    private = False
    if event.fwd_from:
        return
    elif event.is_private:
        await eor(event, "`Trying to gmute user...`")
        await asyncio.sleep(2)
        private = True
    reply = await event.get_reply_message()
    if event.pattern_match.group(1) is not None:
        userid = event.pattern_match.group(1)
    elif reply is not None:
        userid = reply.sender_id
    elif private is True:
        userid = event.chat_id
    else:
        return await eod(event, "Need a user to gmute. Reply or give userid to gmute them..")
    event.chat_id
    await event.get_chat()
    if gsql.is_gmuted(userid, "gmute"):
        return await eod(event, "This kid is already Gmuted.")
    try:
        if str(userid) in DEVLIST:
            return await eod(event, "**Sorry I'm not going to gmute them..**")
    except:
        pass
    try:
        gsql.gmute(userid, "gmute")
    except Exception as e:
        await eod(event, "Error occured!\nError is " + str(e))
    else:
        await eor(event, "Shhh.... Now keep quiet !!")
        


@bot.on(d3vil_cmd(outgoing=True, pattern=r"ungmute ?(\d+)?"))
@bot.on(sudo_cmd(allow_sudo=True, pattern=r"ungmute ?(\d+)?"))
async def endgmute(event):
    private = False
    if event.fwd_from:
        return
    elif event.is_private:
        await eor(event, "`Trying to ungmute !!`")
        await asyncio.sleep(2)
        private = True
    reply = await event.get_reply_message()
    if event.pattern_match.group(1) is not None:
        userid = event.pattern_match.group(1)
    elif reply is not None:
        userid = reply.sender_id
    elif private is True:
        userid = event.chat_id
    else:
        return await eod(event,"Please reply to a user or add their into the command to ungmute them.")
    event.chat_id
    if not gsql.is_gmuted(userid, "gmute"):
        return await eod(event, "I don't remember I gmuted him...")
    try:
        gsql.ungmute(userid, "gmute")
    except Exception as e:
        await eod(event, "Error occured!\nError is " + str(e))
    else:
        await eor(event, "Ok!! Speak")


@command(incoming=True)
async def watcher(event):
    if gsql.is_gmuted(event.sender_id, "gmute"):
        await event.delete()


CmdHelp("global_cmnd").add_command(
  "gban", "<reply>/<userid>", "Globally Bans the mentioned user in 'X' chats you are admin with ban permission."
).add_command(
  "ungban", "<reply>/<userid>", "Globally Unbans the user in 'X' chats you are admin!"
).add_command(
  "listgban", None, "Gives the list of all GBanned Users."
).add_command(
  "gkick", "<reply>/<userid>", "Globally Kicks the user in 'X' chats you are admin!"
).add_command(
  "gmute", "<reply> or <userid>", "Globally Mutes the User."
).add_command(
  "ungmute", "<reply> or <userid>", "Globally Unmutes the gmutes user."
).add()
