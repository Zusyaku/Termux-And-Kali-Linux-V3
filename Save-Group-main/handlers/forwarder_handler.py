# (c) @AbirHasan2005

import asyncio
from pyrogram.types import Message
from pyrogram.errors import FloodWait
from configs import Config


async def forwardMessage(file: Message):
    try:
        data = await file.forward(chat_id=Config.DB_CHANNEL_ID)
        return data
    except FloodWait as e:
        print(f"Sleep of {e.x}s caused by FloodWait")
        await asyncio.sleep(e.x)
        await forwardMessage(file)
