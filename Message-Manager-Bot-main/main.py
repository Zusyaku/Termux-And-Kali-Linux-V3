# (c) @AbirHasan2005

from configs import Config
from database.access_database import mongodb
from helpers.settings_msg import show_settings
from helpers.message_deletor import delete_message
from helpers.custom_filters_handler import setup_callbacks_for_custom_filters, blocked_words_loop, blocked_ext_checker

from pyrogram import Client, filters, idle
from pyrogram.types import Message, ForceReply, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton

AHBot = Client(
    session_name=Config.BOT_USERNAME,
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    bot_token=Config.BOT_TOKEN
)
UserBot = Client(
    session_name=Config.USER_SESSION_STRING,
    api_id=Config.API_ID,
    api_hash=Config.API_HASH
)


@AHBot.on_message(filters.command(['start', f'start@{Config.BOT_USERNAME}']))
async def start_handler(bot: Client, message: Message):
    if (not await mongodb.is_chat_exist(message.chat.id)) and (message.chat.type != "private"):
        try:
            getChat = await bot.get_chat(chat_id=message.chat.id)
        except:
            await message.reply_text(
                text="Make me Admin in this Chat!\n\nElse I will not work properly!",
                quote=True
            )
            return
        await mongodb.add_chat(message.chat.id)
        await bot.send_message(
            Config.LOG_CHANNEL,
            f"#NEW_CHAT: \n\nNew Chat [{getChat.title}]({getChat.invite_link}) Started !!",
            parse_mode="Markdown",
            disable_web_page_preview=True
        )
    await message.reply_text(
        text=Config.START_TEXT,
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("Open Settings", callback_data="goToSettings")]
            ]
        ),
        quote=True
    )


@AHBot.on_message(filters.command(["settings", f"settings@{Config.BOT_USERNAME}"]) & ~filters.private & ~filters.edited)
async def settings_handler(bot: Client, message: Message):
    user = await bot.get_chat_member(chat_id=message.chat.id, user_id=message.from_user.id)
    print(f"User Status: {user.status}\nCan Change Info: {user.can_change_info}")
    if not await mongodb.is_chat_exist(message.chat.id):
        try:
            getChat = await bot.get_chat(chat_id=message.chat.id)
        except:
            await message.reply_text(
                text="Make me Admin in this Chat!\n\nElse I will not work properly!",
                quote=True
            )
            return
        await mongodb.add_chat(message.chat.id)
        await bot.send_message(
            Config.LOG_CHANNEL,
            f"#NEW_CHAT: \n\nNew Chat [{getChat.title}]({getChat.invite_link}) Started !!",
            parse_mode="Markdown",
            disable_web_page_preview=True
        )
    if (user.status not in ["administrator", "creator"]) and ((user.can_change_info is False) or (user.can_change_info is None)):
        await message.delete(True)
        return
    editable = await message.reply_text(
        text="Please Wait ...",
        quote=True
    )
    await show_settings(editable)


@AHBot.on_message(filters.reply & filters.text & ~filters.private & ~filters.edited)
async def reply_handler(bot: Client, message: Message):
    if not await mongodb.is_chat_exist(message.chat.id):
        return
    user = await bot.get_chat_member(chat_id=message.chat.id, user_id=message.from_user.id)
    if message.reply_to_message and (Config.ASK_FOR_BLOCKED_WORDS_LIST in (message.reply_to_message.text or message.reply_to_message.caption)) and (user.status in ["administrator", "creator"]) and (user.can_change_info is True):
        await message.reply_to_message.delete()
        fetch_data = message.text.splitlines()
        while ("" in fetch_data):
            fetch_data.remove("")
        await mongodb.set_blocked_words(message.chat.id, fetch_data)
        await message.reply_text(
            text=f"Successfully Added Blocked Words Filter!\n\n**Blocked Words:** `{fetch_data}`",
            quote=True,
            disable_web_page_preview=True,
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("Go Back to Settings", callback_data="goToSettings")]
                ]
            )
        )
    elif message.reply_to_message and (Config.ASK_FOR_BLOCKED_EXT_LIST in message.reply_to_message.text) and (user.status in ["administrator", "creator"]) and (user.can_change_info is True):
        await message.reply_to_message.delete()
        fetch_data = message.text.splitlines()
        while ("" in fetch_data):
            fetch_data.remove("")
        await mongodb.set_blocked_exts(message.chat.id, fetch_data)
        await message.reply_text(
            text=f"Successfully Added Blocked Extensions Filter!\n\n**Blocked Extensions:** `{fetch_data}`",
            quote=True,
            disable_web_page_preview=True,
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("Go Back to Settings", callback_data="goToSettings")]
                ]
            )
        )


@UserBot.on_message((filters.text | filters.media) & ~filters.private & ~filters.edited, group=-1)
async def main_handler(_, message: Message):
    if not await mongodb.is_chat_exist(message.chat.id):
        return
    check_data = await mongodb.get_custom_filters(message.chat.id)
    blocked_words = await mongodb.get_blocked_words(message.chat.id)
    if (await mongodb.get_blocked_exts(message.chat.id)) is not None:
        is_ext_blocked = await blocked_ext_checker(message, message.chat.id)
        if is_ext_blocked == 400:
            await delete_message(message)
            return
    if ((message.forward_from or message.forward_from_chat) is not None) and ("forward" not in check_data):
        await delete_message(message)
        return
    if (len(check_data) == 8) or (((message.video is not None) and ("video" in check_data)) or ((message.document is not None) and ("document" in check_data)) or ((message.photo is not None) and ("photo" in check_data)) or ((message.audio is not None) and ("audio" in check_data)) or ((message.text is not None) and ("text" in check_data)) or ((message.sticker is not None) and ("sticker" in check_data)) or ((message.animation is not None) and ("gif" in check_data))):
        pass
    else:
        await delete_message(message)
        return
    if blocked_words is not None:
        loop_data = await blocked_words_loop(blocked_words, message)
        if loop_data == 400:
            await delete_message(message)
            return
    load_blocked_words = await mongodb.get_blocked_words(message.chat.id)
    if load_blocked_words:
        is_word_blocked = await blocked_words_loop(load_blocked_words, message)
        if is_word_blocked == 400:
            await delete_message(message)
            return
    allow_server_messages = await mongodb.allowServiceMessageDelete(message.chat.id)
    if (allow_server_messages is False) and (message.service is True):
        await delete_message(message)
        return
    print("Message Not Deleted!")


@AHBot.on_callback_query()
async def callback_handlers(bot: Client, cb: CallbackQuery):
    user = await bot.get_chat_member(chat_id=cb.message.chat.id, user_id=cb.from_user.id)
    print(f"User Status: {user.status}\nCan Change Info: {user.can_change_info}")
    if (user.status not in ["administrator", "creator"]) and ((user.can_change_info is False) or (user.can_change_info is None)):
        await cb.answer("You are not allowed to do that!", show_alert=True)
        return
    print(f"{cb.from_user.mention} Sent Callback Data:\n`{cb.data}`")
    if "blockFileExtensions" in cb.data:
        await cb.message.reply_to_message.reply_text(
            text=Config.ASK_FOR_BLOCKED_EXT_LIST,
            disable_web_page_preview=True,
            quote=True,
            reply_markup=ForceReply(selective=True)
        )
        await cb.message.delete(True)
    elif "blockWords" in cb.data:
        await cb.message.reply_to_message.reply_text(
            text=Config.ASK_FOR_BLOCKED_WORDS_LIST,
            disable_web_page_preview=True,
            quote=True,
            reply_markup=ForceReply(selective=True)
        )
    elif "setCustomFilters" in cb.data:
        await setup_callbacks_for_custom_filters(cb)
    elif cb.data.startswith("set_custom_filter_"):
        data_load = await mongodb.get_custom_filters(cb.message.chat.id)
        get_cb_data = cb.data.split("_", 3)[3]
        if get_cb_data == "default":
            data_load = ["video", "document", "photo", "audio", "text", "sticker", "gif", "forward"]
            await mongodb.set_blocked_words(id=cb.message.chat.id, blocked_words=None)
            await mongodb.set_blocked_exts(id=cb.message.chat.id, blocked_exts=None)
            await cb.answer("Changed Every Filters to Default!\nAlso Changed Blocked Words & Blocked Extensions to None.", show_alert=True)
        else:
            if get_cb_data not in data_load:
                data_load.append(get_cb_data)
            elif get_cb_data in data_load:
                data_load.remove(get_cb_data)
        await mongodb.set_custom_filters(id=cb.message.chat.id, custom_filters=data_load)
        await setup_callbacks_for_custom_filters(cb)
    elif "allowServiceMessagesDelete" in cb.data:
        allowServiceMessagesDelete = await mongodb.allowServiceMessageDelete(cb.message.chat.id)
        if allowServiceMessagesDelete is True:
            await mongodb.set_allowServiceMessageDelete(cb.message.chat.id, allow_service_message=False)
            await cb.answer("Okay!\nFrom now I will Not Delete Service Messages!", show_alert=True)
        elif allowServiceMessagesDelete is False:
            await mongodb.set_allowServiceMessageDelete(cb.message.chat.id, allow_service_message=True)
            await cb.answer("Okay!\nFrom now I will Delete Service Messages!", show_alert=True)
        await show_settings(cb.message)
    elif "goToSettings" in cb.data:
        await show_settings(cb.message)
    elif "showBlockedWords" in cb.data:
        if (await mongodb.get_blocked_words(cb.message.chat.id)) is None:
            await cb.answer("No Words Blocked Yet!", show_alert=True)
        else:
            await cb.message.edit(
                text=f"**The Below Words are Blocked in this Chat:**\n\n{'`' + '`, `'.join(await mongodb.get_blocked_words(cb.message.chat.id)) + '`'}",
                disable_web_page_preview=True,
                parse_mode="Markdown",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [InlineKeyboardButton("Go To Settings", callback_data="goToSettings")],
                        [InlineKeyboardButton("Close ❎", callback_data="closeMeh")]
                    ]
                )
            )
    elif "showBlockedExtensions" in cb.data:
        if (await mongodb.get_blocked_exts(cb.message.chat.id)) is None:
            await cb.answer("No File Extensions Blocked Yet!", show_alert=True)
        else:
            await cb.message.edit(
                text=f"**The Below File Extensions are Blocked in this Chat:**\n\n{'`' + '`,  `'.join(await mongodb.get_blocked_exts(cb.message.chat.id)) + '`'}",
                disable_web_page_preview=True,
                parse_mode="Markdown",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [InlineKeyboardButton("Go To Settings", callback_data="goToSettings")],
                        [InlineKeyboardButton("Close ❎", callback_data="closeMeh")]
                    ]
                )
            )
    elif "closeMeh" in cb.data:
        await cb.message.delete(True)


AHBot.start()
UserBot.start()
idle()
UserBot.stop()
AHBot.stop()
