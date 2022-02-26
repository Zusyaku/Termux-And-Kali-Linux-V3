# (c) @AbirHasan2005

from configs import Config
from handlers.database.database import Database

db = Database(Config.MONGODB_URI, "Discovery-Project-0")
