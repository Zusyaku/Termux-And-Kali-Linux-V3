import os


class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", None)
    MONGO_DB = os.environ.get("MONGO_DB", None)
    API_HASH = os.environ.get("API_HASH", None)
    API_ID = int(os.environ.get("API_ID", None))
    ACCOUNT_GEN_NAME = os.environ.get("ACCOUNT_GEN_NAME", "Alt-Balaji")
    JTU_ENABLE = os.environ.get("JTU_ENABLE", False)
    CHANNEL_USERNAME = os.environ.get("CHANNEL_USERNAME", None)
    CHANNEL_URL = os.environ.get("CHANNEL_URL", None)
    DUMB_CHAT = int(os.environ.get("DUMB_CHAT", False))
    OWNER_ID = int(os.environ.get("OWNER_ID", None))
    GEN_LIMIT_PERDAY = int(os.environ.get("GEN_LIMIT_PERDAY", 2))
