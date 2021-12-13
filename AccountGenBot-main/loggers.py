import os
import sys
from distutils.util import strtobool as sb
from logging import DEBUG, INFO, basicConfig, getLogger
from distutils.util import strtobool as sb
from logging import DEBUG, WARNING, basicConfig, getLogger, INFO
from logging.handlers import RotatingFileHandler
from pathlib import Path
from sys import argv
from telethon import TelegramClient, events, functions, types
import asyncio
import glob
import logging
import sys
from pathlib import Path
import telethon.utils
from telethon import TelegramClient
from Configs import Config

basicConfig(
            format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            level=DEBUG,
        )
logger = getLogger(__name__)
