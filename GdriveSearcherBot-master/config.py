import os

BOT_TOKEN = os.environ.get("BOT_TOKEN", "bot_token")
API_ID = int(os.environ.get("API_ID", 12345678))
API_HASH = os.environ.get("API_HASH", "hash")
RESULTS_COUNT = int(os.environ.get("RESULTS_COUNT", 4))  # NOTE Number of results to show, 4 is better
SUDO_CHATS_ID = list(set(int(x) for x in os.environ.get("SUDO_CHATS_ID", "-1001485393652 -1005456463651").split()))
DRIVE_NAME = list(set(x for x in os.environ.get("DRIVE_NAME", "Root,Cartoon,Course,Movies,Series,Others").split(",")))
DRIVE_ID = list(set(x for x in os.environ.get("DRIVE_ID", "1B9A3QqQqF31IuW2om3Qhr-wkiVLloxw8 12wNJTjNnR-CNBOTnLHqe-1vqFvCRLecn").split()))
INDEX_URL = list(set(x for x in os.environ.get("INDEX_URL", "https://dl.null.tech/0: https://dl.null.tech/0:/Cartoon").split()))
