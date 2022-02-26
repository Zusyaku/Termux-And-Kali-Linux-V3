# (c) @AbirHasan2005

import asyncio
from configs import Config
from pyrogram import Client
from pyrogram.errors import FloodWait, UserNotParticipant
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


async def ForceSub(bot: Client, cmd: Message):
    try:
        user = await bot.get_chat_member(chat_id=(int(Config.UPDATES_CHANNEL) if Config.UPDATES_CHANNEL.startswith("-100") else Config.UPDATES_CHANNEL), user_id=cmd.from_user.id)
        if user.status == "kicked":
            await bot.send_message(
                chat_id=cmd.chat.id,
                text="Sorry Unkil, You are Banned! You will be Kicked from This Group within 15 Seconds.\n"
                     "Contact: [Support Group](https://t.me/linux_repo).",
                disable_web_page_preview=True,
                reply_to_message_id=cmd.message_id
            )
            await asyncio.sleep(15)
            return 404
    except UserNotParticipant:
        try:
            invite_link = await bot.create_chat_invite_link(chat_id=(int(Config.UPDATES_CHANNEL) if Config.UPDATES_CHANNEL.startswith("-100") else Config.UPDATES_CHANNEL))
        except FloodWait as e:
            print(f"Sleep of {e.x}s caused by FloodWait")
            await asyncio.sleep(e.x)
            return 200
        except Exception as err:
            print(f"Unable to do Force Subscribe to {Config.UPDATES_CHANNEL}\n\nError: {err}")
            return 200
        send_ = await bot.send_message(
            chat_id=cmd.chat.id,
            text=f"Hello {cmd.from_user.mention},\n\n"
                 f"**Please [Join Channel]({invite_link.invite_link}) to Send Messages to This Group!**\n\n"
                 "Till you join channel you will be muted in this group!",
            reply_to_message_id=cmd.message_id,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("🤖 Join Channel 🤖", url=invite_link.invite_link)]
                ]
            )
        )
        return 400
    except FloodWait as e:
        print(f"Sleep of {e.x}s caused by FloodWait")
        await asyncio.sleep(e.x)
        return 200
    except Exception as err:
        print(f"Unable to do Force Subscribe to {Config.UPDATES_CHANNEL}\n\nError: {err}")
        return 200
