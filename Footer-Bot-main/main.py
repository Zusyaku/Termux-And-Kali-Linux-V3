# (c) @AbirHasan2005

import shutil
import psutil
import asyncio
from pyromod import listen
from asyncio import TimeoutError
from pyrogram import Client, filters
from pyrogram.errors import UserNotParticipant, FloodWait
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message, CallbackQuery

from configs import Config
from helpers.database.access_db import db
from helpers.human_readable import humanbytes
from helpers.database.add_user import AddUserToDatabase
from helpers.settings import ShowSettings
from helpers.broadcast import broadcast_handler
from helpers.fetch_me import FetchMeOnChat
from helpers.add_footer import AddFooter

AHBot = Client(
    session_name=Config.SESSION_NAME,
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    bot_token=Config.BOT_TOKEN
)


@AHBot.on_message(filters.private & filters.command("start"))
async def _start(bot: Client, m: Message):
    await AddUserToDatabase(bot, m)
    try:
        await m.reply_text(
            Config.START_TEXT,
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("Support Group", url="https://t.me/DevsZone"), InlineKeyboardButton("Bots Channel", url="https://t.me/Discovery_Updates")],
                    [InlineKeyboardButton("Developer - @AbirHasan2005", url="https://t.me/AbirHasan2005")]
                ]
            ),
            quote=True
        )
    except FloodWait as e:
        await asyncio.sleep(e.x)
        await m.reply_text("Unkil no DDoS Plox!")


@AHBot.on_message(filters.private & filters.command("settings"))
async def _settings(bot: Client, event: Message):
    await AddUserToDatabase(bot, event)
    editable = await event.reply_text("Please Wait ...", quote=True)
    await ShowSettings(editable, user_id=event.from_user.id)


@AHBot.on_message(filters.channel & (filters.video | filters.document) & ~filters.edited & ~filters.private)
async def add_footer(bot: Client, event: Message):
    on_event = await db.find_user_id(event.chat.id)
    if on_event is None:
        return
    _I, _err = await FetchMeOnChat(bot, chat_id=event.chat.id)
    if _I == 404:
        print(f"Unable to Edit Message in {event.chat.id} !\nError: {_err}")
        return
    service_on = await db.get_service_on(int(on_event))
    footer_text = await db.get_footer_text(int(on_event))
    is_forward = event.forward_from_chat or event.forward_from
    if (_I.can_edit_messages is True) and (service_on is True) and (footer_text is not None) and (is_forward is None):
        await AddFooter(bot, event, footer_text, int(on_event))


@AHBot.on_message(filters.channel & filters.text & ~filters.edited & ~filters.private, group=-1)
async def add_text_footer(bot: Client, event: Message):
    on_event = await db.find_user_id(event.chat.id)
    if on_event is None:
        return
    _I, _err = await FetchMeOnChat(bot, chat_id=event.chat.id)
    if _I == 404:
        print(f"Unable to Edit Message in {event.chat.id} !\nError: {_err}")
        return
    service_on = await db.get_service_on(int(on_event))
    footer_text = await db.get_footer_text(int(on_event))
    also_footer2photo = await db.get_add_photo_footer(int(on_event))
    is_forward = event.forward_from_chat or event.forward_from
    if (_I.can_edit_messages is True) and (service_on is True) and (footer_text is not None) and (is_forward is None) and (also_footer2photo is True):
        await AddFooter(bot, event, footer_text, int(on_event))


@AHBot.on_message(filters.channel & filters.photo & ~filters.edited & ~filters.private)
async def add_text_footer(bot: Client, event: Message):
    on_event = await db.find_user_id(event.chat.id)
    if on_event is None:
        return
    _I, _err = await FetchMeOnChat(bot, chat_id=event.chat.id)
    if _I == 404:
        print(f"Unable to Edit Message in {event.chat.id} !\nError: {_err}")
        return
    service_on = await db.get_service_on(int(on_event))
    footer_text = await db.get_footer_text(int(on_event))
    also_footer2text = await db.get_add_text_footer(int(on_event))
    is_forward = event.forward_from_chat or event.forward_from
    if (_I.can_edit_messages is True) and (service_on is True) and (footer_text is not None) and (is_forward is None) and (also_footer2text is True):
        await AddFooter(bot, event, footer_text, int(on_event))


@AHBot.on_message(filters.private & filters.command("broadcast") & filters.user(Config.BOT_OWNER) & filters.reply)
async def _broadcast(_, event: Message):
    await broadcast_handler(event)


@AHBot.on_message(filters.private & filters.command("status") & filters.user(Config.BOT_OWNER))
async def _status(_, event: Message):
    total, used, free = shutil.disk_usage(".")
    total = humanbytes(total)
    used = humanbytes(used)
    free = humanbytes(free)
    cpu_usage = psutil.cpu_percent()
    ram_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent
    total_users = await db.total_users_count()
    await event.reply_text(
        text=f"**Total Disk Space:** {total} \n**Used Space:** {used}({disk_usage}%) \n**Free Space:** {free} \n**CPU Usage:** {cpu_usage}% \n**RAM Usage:** {ram_usage}%\n\n**Total Users in DB:** `{total_users}`",
        parse_mode="Markdown",
        quote=True
    )


@AHBot.on_message(filters.private & filters.command("disable") & filters.user(Config.BOT_OWNER))
async def handler_disabler(bot: Client, event: Message):
    if len(event.command) > 1:
        if event.command[1].startswith("-100"):
            get_user_id = await db.find_user_id(channel_id=int(event.command[1]))
            if get_user_id is None:
                await event.reply_text(f"Chat Not Found in Database!")
            else:
                await db.delete_user(user_id=get_user_id)
                await event.reply_text(f"User Data of {str(get_user_id)} Removed From Database!")
                await bot.leave_chat(chat_id=event.chat.id)
        else:
            await db.delete_user(user_id=int(event.command[1]))
            await event.reply_text(f"User Data of {event.command[1]} Removed From Database!")


@AHBot.on_callback_query()
async def callback_handlers(bot: Client, cb: CallbackQuery):
    if cb.message.chat.type not in ["private"]:
        return
    if "triggerService" in cb.data:
        cache_service_on = await db.get_service_on(cb.from_user.id)
        await db.set_service_on(cb.from_user.id, service_on=(False if (cache_service_on is True) else True))
        await cb.answer("Changed Service Mode Successfully", show_alert=True)
        await ShowSettings(cb.message, user_id=cb.from_user.id)
    elif "setAlsoFooter2Text" in cb.data:
        cache_also_footer2text = await db.get_add_text_footer(cb.from_user.id)
        await db.set_add_text_footer(cb.from_user.id, add_text_footer=(False if (cache_also_footer2text is True) else True))
        await cb.answer(f"Ok, I will {'not ' if (cache_also_footer2text is True) else ''}add Footer to Text Messages too!", show_alert=True)
        await ShowSettings(cb.message, user_id=cb.from_user.id)
    elif "setAlsoFooter2Photo" in cb.data:
        cache_also_footer2photo = await db.get_add_photo_footer(cb.from_user.id)
        await db.set_add_photo_footer(cb.from_user.id, add_photo_footer=(False if (cache_also_footer2photo is True) else True))
        await cb.answer(f"Ok, I will {'not ' if (cache_also_footer2photo is True) else ''}add Footer to Photos!", show_alert=True)
        await ShowSettings(cb.message, user_id=cb.from_user.id)
    elif "setFooterText" in cb.data:
        await cb.message.edit("Ok Unkil,\nNow Send Me Footer Text. Max 1024 Characters.\n\nPress /cancel for Cancelling this process.")
        try:
            event_: Message = await bot.listen(cb.message.chat.id, filters=filters.text, timeout=300)
            if event_.text:
                if event_.text == "/cancel":
                    await event_.delete(True)
                    await cb.message.edit("Process Cancelled!")
                else:
                    cache_footer = event_.text.markdown
                    await db.set_footer_text(cb.from_user.id, cache_footer)
                    await cb.message.edit(
                        text=f"Footer Collected!\n\n**Footer Text:**\n{cache_footer}",
                        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Go To Settings", callback_data="showSettings")]])
                    )
        except TimeoutError:
            await cb.message.edit("Unkil,\n5 Minutes Passed!\nNow Trigger Again From /settings 😐")
    elif "showSettings" in cb.data:
        await ShowSettings(cb.message, user_id=cb.from_user.id)
    elif "rmFooterText" in cb.data:
        await db.set_footer_text(cb.from_user.id, footer_text=None)
        await cb.answer("Footer Text Removed!", show_alert=True)
        await ShowSettings(cb.message, user_id=cb.from_user.id)
    elif "showFooterText" in cb.data:
        footer_text = await db.get_footer_text(cb.from_user.id)
        await cb.message.edit(f"**Here is Your Footer Text:**\n{footer_text}", parse_mode="markdown", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Go To Settings", callback_data="showSettings")]]))
    elif "setChannelID" in cb.data:
        await cb.message.edit(
            text="Ok Unkil,\nNow Add me to Channel as Admin & Forward a Message From Channel.\n\nPress /cancel for Cancelling this process."
        )
        try:
            event_: Message = await bot.listen(cb.message.chat.id, timeout=300)
            if event_.forward_from_chat and ((await db.is_user_exist(event_.forward_from_chat.id)) is False):
                try:
                    _I, _err = await FetchMeOnChat(bot, chat_id=event_.forward_from_chat.id)
                    if _I == 404:
                        await cb.message.edit(f"Unable to Edit Message in {str(event_.forward_from_chat.id)} !\nError: {_err}")
                        return
                    if _I and (_I.can_edit_messages is True):
                        if await db.find_user_id(channel_id=event_.forward_from_chat.id) is None:
                            try:
                                UserClient = await bot.get_chat_member(chat_id=event_.forward_from_chat.id, user_id=(await bot.get_me()).id)
                                if UserClient.can_edit_messages is True:
                                    await db.set_channel_id(cb.from_user.id, channel_id=event_.forward_from_chat.id)
                                    await cb.message.edit("Successfully Added Channel to Database!", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Go To Settings", callback_data="showSettings")]]))
                                else:
                                    await cb.message.edit("Sorry Unkil,\nYou don't have rights to Edit Messages on this Channel!")
                            except:
                                await cb.message.edit("Sorry Unkil,\nYou are not Admin in this channel!")
                        else:
                            await cb.message.edit("Sorry Unkil,\nAlready this channel in Database! Can't add same channel again.")
                    else:
                        await cb.message.edit(f"I don't have rights to edit messages in {_I.title} !!\n\nPlease Give Rights else I can't add Footer.")
                except UserNotParticipant:
                    await cb.message.edit("Unable to Add Channel in Database!\nI am not Admin in Channel.")
                except Exception as err:
                    await cb.message.edit(f"Unable to Find Channel!\n\n**Error:** `{err}`", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Support Group", url="https://t.me/DevsZone")]]))
            elif event_.text and (event_.text == "/cancel"):
                await cb.message.edit("Process Cancelled!")
        except TimeoutError:
            await cb.message.edit("Unkil,\n5 Minutes Passed!\nNow Trigger Again From /settings 😐")


AHBot.run()
