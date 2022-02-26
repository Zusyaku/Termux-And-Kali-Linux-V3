# (c) @AbirHasan2005

import datetime
import motor.motor_asyncio


class Database:
    def __init__(self, uri, database_name):
        self._client = motor.motor_asyncio.AsyncIOMotorClient(uri)
        self.db = self._client[database_name]
        self.col = self.db.chats

    def new_chat(self, id):
        return dict(
            id=id,
            join_date=datetime.date.today().isoformat(),
            custom_filters=["video", "document", "photo", "audio", "text", "sticker", "gif", "forward"],
            blocked_exts=None,
            blocked_words=None,
            allow_service_message=False
        )

    async def add_chat(self, id):
        chat = self.new_chat(id)
        await self.col.insert_one(chat)

    async def is_chat_exist(self, id):
        chat = await self.col.find_one({'id': int(id)})
        return True if chat else False

    async def total_chat_count(self):
        count = await self.col.count_documents({})
        return count

    async def get_all_chats(self):
        all_chats = self.col.find({})
        return all_chats

    async def delete_chat(self, chat_id):
        await self.col.delete_many({'id': int(chat_id)})

    async def set_custom_filters(self, id, custom_filters):
        await self.col.update_one({'id': id}, {'$set': {'custom_filters': custom_filters}})

    async def get_custom_filters(self, id):
        user = await self.col.find_one({'id': int(id)})
        return user.get('custom_filters', ["video", "document", "photo", "audio", "text", "sticker", "gifs", "forward"])

    async def get_blocked_exts(self, id):
        user = await self.col.find_one({'id': int(id)})
        return user.get('blocked_exts', None)

    async def set_blocked_exts(self, id, blocked_exts):
        await self.col.update_one({'id': id}, {'$set': {'blocked_exts': blocked_exts}})

    async def get_blocked_words(self, id):
        user = await self.col.find_one({'id': int(id)})
        return user.get('blocked_words', None)

    async def set_blocked_words(self, id, blocked_words):
        await self.col.update_one({'id': id}, {'$set': {'blocked_words': blocked_words}})

    async def allowServiceMessageDelete(self, id):
        user = await self.col.find_one({'id': int(id)})
        return user.get('allow_service_message', None)

    async def set_allowServiceMessageDelete(self, id, allow_service_message):
        await self.col.update_one({'id': int(id)}, {'$set': {'allow_service_message': allow_service_message}})