import logging
import os

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
LOGGER = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.WARNING)


class ENV_VARS(object):
    API_ID = int(os.environ.get("API_ID", "10086141"))
    API_HASH = os.environ.get("API_HASH", "d086fe989f76e713f1c86e5dd7ad5409")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6650645222:AAEO0DoR7McOFH_EVaf9KIpPiS4R4kzWJHc")
    BOT_USERNAME = os.environ.get("Scout23bot")
    #AUTH_USER = int(os.environ.get("AUTH_USER", 5071059420))


Config = ENV_VARS

handler = Config.BOT_USERNAME


class CMD(object):
    START = ["start", f"start@{handler}"]
