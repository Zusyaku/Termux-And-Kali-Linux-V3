# (c) @AbirHasan2005

import os


class Config(object):
    API_ID = int(os.environ.get("API_ID", 123456))
    API_HASH = os.environ.get("API_HASH")
    BOT_TOKEN = os.environ.get("BOT_TOKEN")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", ":memory:")
    MONGODB_URI = os.environ.get("MONGODB_URI")
    OWNER_ID = int(os.environ.get("OWNER_ID", 1445283714))
    BOT_USERNAME = os.environ.get("BOT_USERNAME")
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL"))

    ASK_FOR_BLOCKED_WORDS_LIST = os.environ.get("ASK_FOR_BLOCKED_WORDS_LIST",
                                                "Reply to this message with a list of Blocked Words. If those in Message I will not Forward them!\n\nExample:\nhello\nhacker\ncracker\njoin\nabuse heroku\njoin my channel\nchutiyappa")
    ASK_FOR_BLOCKED_EXT_LIST = os.environ.get("ASK_FOR_BLOCKED_EXT_LIST",
                                              "Reply to this message with a list of Blocked Extensions. If any file with that extension I will not forward that file!\n\nExample:\nzip\nmkv\ntorrent\ntxt\npy\ncap\nmp4\nmp3\nrar\n\nExtensions should be in lower case!")
    START_TEXT = """
Hi, This is Massages Manager Bot!
I can do many things with messages in a Group.

Check /settings !! 
"""
    ABOUT_CUSTOM_FILTERS_TEXT = """
Custom Filters is for deleting only separate type Media Messages or Only Text Messages.
Like you can set only delete `photo` or `video` or `document` or `audio` or `text` ...

If Need More Help Ask in [Support Group](https://t.me/JoinOT)!
"""