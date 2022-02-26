# (c) @AbirHasan2005

import asyncio
from pyrogram import Client
from pyrogram.errors import UserIsBlocked, FloodWait
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from helpers.database.access_db import db
from configs import Config


async def NotifyUser(bot: Client, text: str, user_id: int):
    """
    A Custom Send Message to User Function. Send a Message to User via user_id.

    :param bot: Pass Bot Client.
    :param text: Text Message to Send to User.
    :param user_id: User ID.
    """

    try:
        await bot.send_message(
            chat_id=user_id,
            text=text,
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Support Group", url="https://t.me/linux_repo")]])
        )
    except FloodWait as e:
        await asyncio.sleep(e.x)
        await NotifyUser(bot, text, user_id)
    except UserIsBlocked:
        await db.delete_user(user_id=user_id)
    except Exception as e:
        await bot.send_message(
            chat_id=Config.LOG_CHANNEL,
            text=f"#USER_CONTACT_ERROR:\nUnable to Send Message to {str(user_id)} !\nError: {e}"
        )
