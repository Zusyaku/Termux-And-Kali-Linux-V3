# (c) @AbirHasan2005

import asyncio
from configs import Config
from database.access_database import mongodb as db
from pyrogram.errors import MessageNotModified, FloodWait
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, Message


async def setup_callbacks_for_custom_filters(cb: CallbackQuery):
    get_data = await db.get_custom_filters(cb.message.chat.id)
    markup = [
        [InlineKeyboardButton(f"Allow Videos {'✅' if ('video' in get_data) else '❌'}",
                              callback_data="set_custom_filter_video"),
         InlineKeyboardButton(f"Allow Documents {'✅' if ('document' in get_data) else '❌'}",
                              callback_data="set_custom_filter_document")],
        [InlineKeyboardButton(f"Allow Photos {'✅' if ('photo' in get_data) else '❌'}",
                              callback_data="set_custom_filter_photo"),
         InlineKeyboardButton(f"Allow Audios {'✅' if ('audio' in get_data) else '❌'}",
                              callback_data="set_custom_filter_audio")],
        [InlineKeyboardButton(f"Allow Stickers {'✅' if ('sticker' in get_data) else '❌'}",
                              callback_data="set_custom_filter_sticker"),
         InlineKeyboardButton(f"Allow GIFs {'✅' if ('gif' in get_data) else '❌'}",
                              callback_data="set_custom_filter_gif")],
        [InlineKeyboardButton(f"Allow Forwarded Messages {'✅' if ('forward' in get_data) else '❌'}",
                              callback_data="set_custom_filter_forward")],
        [InlineKeyboardButton(f"Allow Text Messages {'✅' if ('text' in get_data) else '❌'}",
                              callback_data="set_custom_filter_text")]
    ]
    if get_data is not None:
        markup.append([InlineKeyboardButton("Keep Default Filters", callback_data="set_custom_filter_default")])
    markup.append([InlineKeyboardButton("Go Back to Settings", callback_data="goToSettings")])
    markup.append([InlineKeyboardButton("Close ❎", callback_data="closeMeh")])

    try:
        await cb.message.edit(
            text=f"**What is Custom Filters?**\n{Config.ABOUT_CUSTOM_FILTERS_TEXT}\n\n**Here You Can Setup Your Custom Filters:**",
            disable_web_page_preview=True,
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup(markup)
        )
    except FloodWait as e:
        await asyncio.sleep(e.x)
        pass
    except MessageNotModified:
        pass


async def blocked_words_loop(blocked_words, update):
    if (update.text is None) and (update.caption is None):
        return 200
    for a in range(len(blocked_words)):
        if blocked_words[a].lower() in (update.text or update.caption).lower():
            return 400


async def blocked_ext_checker(message: Message, chat_id):
    blocked_exts = await db.get_blocked_exts(chat_id)
    media = message.document or message.video or message.audio or message.sticker
    if (media is not None) and (media.file_name is not None):
        _file = media.file_name.rsplit(".", 1)
        if (len(_file) == 2) and (_file[-1].lower() in blocked_exts):
            return 400
        else:
            return 200
    else:
        return 200
