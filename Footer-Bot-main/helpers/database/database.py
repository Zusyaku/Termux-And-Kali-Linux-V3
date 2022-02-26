# (c) @AbirHasan2005

import datetime
import motor.motor_asyncio


class Database:

    def __init__(self, uri, database_name):
        self._client = motor.motor_asyncio.AsyncIOMotorClient(uri)
        self.db = self._client[database_name]
        self.col = self.db.users

    def new_user(self, id):
        return dict(
            id=id,
            join_date=datetime.date.today().isoformat(),
            footer_text=None,
            channel_id=None,
            service_on=True,
            add_text_footer=False,
            add_photo_footer=False
        )

    async def add_user(self, id):
        user = self.new_user(id)
        await self.col.insert_one(user)

    async def is_user_exist(self, id):
        user = await self.col.find_one({'id': int(id)})
        return True if user else False

    async def total_users_count(self):
        count = await self.col.count_documents({})
        return count

    async def get_all_users(self):
        all_users = self.col.find({})
        return all_users

    async def delete_user(self, user_id):
        await self.col.delete_many({'id': int(user_id)})

    async def request_(self, id):
        user = await self.col.find_one({'id': int(id)})
        return user

    async def set_footer_text(self, id, footer_text):
        await self.col.update_one({'id': id}, {'$set': {'footer_text': footer_text}})

    async def set_channel_id(self, id, channel_id):
        await self.col.update_one({'id': id}, {'$set': {'channel_id': channel_id}})

    async def set_service_on(self, id, service_on):
        await self.col.update_one({'id': id}, {'$set': {'service_on': service_on}})

    async def set_add_text_footer(self, id, add_text_footer):
        await self.col.update_one({'id': id}, {'$set': {'add_text_footer': add_text_footer}})

    async def set_add_photo_footer(self, id, add_photo_footer):
        await self.col.update_one({'id': id}, {'$set': {'add_photo_footer': add_photo_footer}})

    async def find_user_id(self, channel_id):
        doc_ = await self.col.find_one({'channel_id': int(channel_id)})
        return doc_.get('id', None) if doc_ else None

    async def get_footer_text(self, id):
        user = await self.request_(id)
        return user.get('footer_text', False)

    async def get_channel_id(self, id):
        user = await self.request_(id)
        return user.get('channel_id', False)

    async def get_service_on(self, id):
        user = await self.request_(id)
        return user.get('service_on', True)

    async def get_add_text_footer(self, id):
        user = await self.request_(id)
        return user.get('add_text_footer', False)

    async def get_add_photo_footer(self, id):
        user = await self.request_(id)
        return user.get('add_photo_footer', False)
