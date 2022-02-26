# (c) @AbirHasan2005

from configs import Config
from database.database_handlers import Database

mongodb = Database(Config.MONGODB_URI, Config.BOT_USERNAME)
