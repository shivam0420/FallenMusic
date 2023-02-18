from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID", "10476191"))
API_HASH = getenv("API_HASH", "709b4184f6116b4d824ea9fa74a1c4b0")

BOT_TOKEN = getenv("BOT_TOKEN", "5815997851:AAE7QUC8yNpI34VBFMZq5mmWa1ri_6LTfz0")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "900000009"))

OWNER_ID = int(getenv("OWNER_ID", "5367839854"))

PING_IMG = getenv("PING_IMG", "https://te.legra.ph/file/6f99c49bdb4679acad717.jpg")
START_IMG = getenv("START_IMG", "https://te.legra.ph/file/f8ba75bdbb9931cbc8229.jpg")

SESSION = getenv("SESSION", "BQB_HsKh4KuYqeszg_6wbp6pbto_oiRtLcHwA49n79TCmbd1ICa1VZ1XotDBcRqtePVTQdXQelmGalZypjxAIoKWqPl_XFW_5Wt4zdOnVaIaZSNEY2JSJ5HMccrxIDjojUQEieJzxAVUhkX_jfZiVJesXzi0sDbbLq5EVRsqXXGfuNLvSKajEz3vCfpXd2EYom-wszDCK_RJYMS12MEY2EfyY_K7qY5DDBxh6gDkugEyizaj9fqtW9tDPQRHnByHTlTbBiUyyXXptpNuWTZukbhm62JMGj01vyqNqszZv0VfOb4zhH5lWUnzgREqzKreQ_LVaqHmTLvmjgIZpzB9OHvnAAAAAVRGepsA")

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/brandinvisible_brothers")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/brandinvisible_brothers")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5708872347").split()))


FAILED = "https://te.legra.ph/file/4c896584b592593c00aa8.jpg"
