# (c) @AbirHasan2005

import asyncio
from pyrogram import Client, filters, idle
from pyrogram.errors import UserNotParticipant
from pyrogram.types import Message, ChatPermissions

from configs import Config
from handlers.database.access_db import db
from handlers.forcesub_handler import ForceSub
from handlers.forwarder_handler import forwardMessage
from handlers.send_mesage_handler import sendMessage
from handlers.database.add_user import AddUserToDatabase

User = Client(
    session_name=Config.STRING_SESSION,
    api_id=Config.API_ID,
    api_hash=Config.API_HASH
)
Bot = Client(
    session_name="Abir-Save-Group",
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    bot_token=Config.BOT_TOKEN
)


@User.on_message(filters.group & (filters.document | filters.video) & ~filters.edited)
async def files_handler(bot: Client, cmd: Message):
    media = cmd.document or cmd.video
    if media.file_name.rsplit(".", 1)[-1] in Config.BLOCKED_EXTENSIONS:
        return
    if media.file_size < 5242880:
        return
    if (Config.FORCE_SUB_CHANNEL is not None) and (cmd.from_user.is_bot is False):
        await AddUserToDatabase(cmd)
        Fsub = await ForceSub(Bot, cmd)
        if Fsub == 400:
            await db.set_joined_channel(cmd.from_user.id, joined_channel=False)
            await db.set_group_id(cmd.from_user.id, group_id=cmd.chat.id)
            try:
                await bot.restrict_chat_member(
                    chat_id=cmd.chat.id,
                    user_id=cmd.from_user.id,
                    permissions=ChatPermissions(can_send_messages=False)
                )
            except:
                pass
            return
        elif Fsub == 404:
            try:
                await bot.kick_chat_member(chat_id=cmd.chat.id, user_id=cmd.from_user.id)
            except:
                pass
        else:
            await db.delete_user(cmd.from_user.id)
    forward = await forwardMessage(cmd)
    if cmd.from_user.is_bot:
        text = "This File will be deleted in 10 minutes.\n\n" \
               "But,\n" \
               "File Stored in Database!\n" \
               f"**File Name:** `{media.file_name}`\n\n" \
               f"[👉 Get File Now 👈](https://t.me/{(await Bot.get_me()).username}?start=AbirHasan2005_{str(forward.message_id)})"
    else:
        text = f"{cmd.from_user.mention} Unkil,\n" \
               "This File will be deleted in 10 minutes.\n\n" \
               "But,\n" \
               "Your File stored in Database!\n\n" \
               f"**File Name:** `{media.file_name}`\n\n" \
               f"[👉 Get Your File Now 👈](https://t.me/{(await Bot.get_me()).username}?start=AbirHasan2005_{str(forward.message_id)})"
    await sendMessage(
        bot=bot,
        message_id=cmd.message_id,
        chat_id=cmd.chat.id,
        text=text
    )
    await asyncio.sleep(600)
    try:
        await cmd.delete(True)
    except Exception as err:
        print(f"Unable to Delete Media Message!\nError: {err}\n\nMessage ID: {cmd.message_id}")


@User.on_message(filters.private & (filters.text | filters.sticker) & ~filters.edited)
async def text_handler(_, cmd: Message):
    await cmd.reply_text(
        "Hi Unkil!\n"
        "I am Group Files Store Userbot.\n\n"
        "Add me to Group I will Save Group Files & Delete Them After 10 Minutes. Also I will Reply with Revive Link.\n"
        "**Demo Group:** [Discovery Cloud](https://t.me/joinchat/O9WIjhCGHLo0YmQ0)",
        disable_web_page_preview=True
    )


@User.on_message(filters.group & filters.text & ~filters.edited)
async def Fsub_handler(bot: Client, event: Message):
    if (Config.FORCE_SUB_CHANNEL is not None) and (event.from_user.is_bot is False):
        await AddUserToDatabase(event)
        Fsub = await ForceSub(Bot, event)
        if Fsub == 400:
            await db.set_joined_channel(event.from_user.id, joined_channel=False)
            await db.set_group_id(event.from_user.id, group_id=event.chat.id)
            try:
                await bot.restrict_chat_member(
                    chat_id=event.chat.id,
                    user_id=event.from_user.id,
                    permissions=ChatPermissions(can_send_messages=False)
                )
            except:
                pass
        elif Fsub == 404:
            try:
                await bot.kick_chat_member(chat_id=event.chat.id, user_id=event.from_user.id)
            except:
                pass
        else:
            await db.delete_user(event.from_user.id)


@Bot.on_message(filters.private & filters.command("start") & ~filters.edited)
async def start_handler(bot: Client, event: Message):
    __data = event.text.split("_")[-1]
    if __data == "/start":
        await sendMessage(bot, "Go Away Unkil", event.message_id, event.chat.id)
    else:
        file_id = int(__data)
        try:
            await bot.forward_messages(chat_id=event.chat.id, from_chat_id=Config.DB_CHANNEL_ID, message_ids=file_id)
        except:
            await sendMessage(bot, "Unable to Get Message!\n\nReport at @DevsZone !!", event.message_id, event.chat.id)


@Bot.on_chat_member_updated()
async def handle_Fsub_Join(bot: Client, event: Message):
    """
    Auto Unmute Member after joining channel.

    :param bot: pyrogram.Client
    :param event: pyrogram.types.Message
    """

    if Config.FORCE_SUB_CHANNEL:
        try:
            user_ = await bot.get_chat_member(event.chat.id, event.from_user.id)
            if user_.is_member is False:
                return
        except UserNotParticipant:
            return
        group_id = await db.get_group_id(event.from_user.id)
        group_message_id = await db.get_group_message_id(event.from_user.id)
        if group_id:
            try:
                await bot.unban_chat_member(chat_id=int(group_id), user_id=event.from_user.id)
                try:
                    await bot.delete_messages(chat_id=int(group_id), message_ids=group_message_id, revoke=True)
                except Exception as err:
                    print(f"Unable to Delete Message!\nError: {err}")
                await db.delete_user(user_id=event.from_user.id)
            except Exception as e:
                print(f"Skipping FSub ...\nError: {e}")

# Start User Client
User.start()
print("Userbot Started!")
# Start Bot Client
Bot.start()
print("Bot Started!")
# Loop Clients till Disconnects
idle()
# Stop User Client
User.stop()
print("\n")
print("Userbot Stopped!")
# Stop Bot Client
Bot.stop()
print("Bot Stopped!")
