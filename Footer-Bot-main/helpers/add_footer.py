# (c) @AbirHasan2005

import asyncio
from configs import Config
from pyrogram import Client
from pyrogram.types import Message
from pyrogram.errors import FloodWait, MediaCaptionTooLong, MessageNotModified
from helpers.contact_user import NotifyUser


async def AddFooter(bot: Client, event: Message, text: str, user_id: int):
    """
    Custom Caption Editor Function for Footer Bot.

    :param bot: Pass Bot Client.
    :param event: Pass Message object.
    :param text: Pass Footer Text.
    :param user_id: Pass user_id same as on_event.
    """

    try:
        if event.text is None:
            await event.edit_caption(
                caption=f"{event.caption.markdown if (event.caption is not None) else ''}\n{text}",
                parse_mode="markdown"
            )
        else:
            await event.edit(
                text=f"{event.text.markdown}\n{text}",
                parse_mode="markdown"
            )
    except MediaCaptionTooLong:
        await NotifyUser(
            bot=bot,
            text=f"Unable to Add Footer Text to [This Message](https://t.me/{'c/' + str(event.chat.id) + '/' + str(event.message_id) if (event.chat.username is None) else event.chat.username + '/' + str(event.chat.id) + '/' + str(event.message_id)}.\n\n**Reason:** `Media Message Caption is Too Long!`",
            user_id=user_id
        )
        return
    except MessageNotModified:
        await NotifyUser(
            bot=bot,
            text=f"Unable to Add Footer Text to [This Message](https://t.me/{'c/' + str(event.chat.id) + '/' + str(event.message_id) if (event.chat.username is None) else event.chat.username + '/' + str(event.chat.id) + '/' + str(event.message_id)}.\n\n**Reason:** `Multiple Buttons Editor Bots Editing Message!`",
            user_id=user_id
        )
        return
    except FloodWait as e:
        if e.x > 180:
            await bot.leave_chat(chat_id=event.chat.id)
            await NotifyUser(
                bot=bot,
                text=f"Sorry, Unkil.\nGot 3 Minutes FloodWait from `{str(event.chat.id)}` !!\n\nSo I left that Channel.",
                user_id=user_id
            )
            await NotifyUser(
                bot=bot,
                text=f"Hemlo, Unkil.\nGot 3 Minutes FloodWait from `{str(event.chat.id)}` !!\n\nSo I left that Channel.",
                user_id=Config.BOT_OWNER
            )
            return
        print(f"Sleeping for {e.x + 5}s - {event.chat.id} - @{event.chat.username}")
        await asyncio.sleep(e.x)
        await asyncio.sleep(5)
        await AddFooter(bot, event, text, user_id)
    except Exception as err:
        await NotifyUser(
            bot=bot,
            text=f"**Warning:** I am unable to add footer in `{event.chat.id}`\n\n**Reason:** `{err}`",
            user_id=Config.BOT_OWNER
        )
        return
