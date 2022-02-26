# (c) @AbirHasan2005

from handlers.database.access_db import db
from pyrogram.types import Message


async def AddUserToDatabase(cmd: Message):
    if not await db.is_user_exist(cmd.from_user.id):
        await db.add_user(cmd.from_user.id)
