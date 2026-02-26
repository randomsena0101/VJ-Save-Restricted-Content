# Don't Remove Credit Tg - @VJ_Bots
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01

import os

# Login feature, if you want then True , if you don't want then False
LOGIN_SYSTEM = bool(os.environ.get('LOGIN_SYSTEM', True)) # True or False

if LOGIN_SYSTEM == False:
    # if login system is False then fill your tg account session below 
    STRING_SESSION = os.environ.get("STRING_SESSION", "AQIzImMAI_Bzq8pvW5EtPvSvTfAfd4o7AFQd4CxBLf_KqDZMlLbcmHMPreQBjSh32nW6GctDwJcOsLBIYzgPw0P9RjOUv0wGUoOqfqxHASEV3sH_9xpez-J-TaDisZc8ILUwCXhfHOmES13sVPJA-D_rOkRolgZB5t0v-gmlD-54FfDqqYjHZZGy4plUGxVyEZrg2y3xhjWbAqTdQhvXKCjHUZ6Sy_MxmCtJ2SYeNmdjP3wpvgiU43Fog7AJ_dSGVWcjtaTs9eR-5G_R7N8WqoNxziamBEdgkxrZyizFt0tMZU3PJiMSgi8x3u1tEyX45lApMNcfitXorxGZtrOY0L5bsIKM-wAAAAHpC8m5AA")
else:
    STRING_SESSION = None

# Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8737801641:AAE7QoFn2deJt2WfTjVDt10hJGQow0wwgHA")

# Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "36905571"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "36677bbab05f148b95f91b13dbc57ea1")

# Your Owner / Admin Id For Broadcast 
ADMINS = int(os.environ.get("ADMINS", "8204831161"))

# Your Channel Id In Which Bot Upload Downloaded Video/File/Message etc.
# And Make Your Bot Admin In this channel with full rights.
# if you don't want to upload in channel then leave it blank don't fill anything.
CHANNEL_ID = os.environ.get("CHANNEL_ID", "")

# Your Mongodb Database Url
# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = os.environ.get("DB_URI", "") # Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_NAME = os.environ.get("DB_NAME", "vjsavecontentbot")

# Increase time as much as possible to avoid floodwait, spamming and tg account ban issues.
WAITING_TIME = int(os.environ.get("WAITING_TIME", "10")) # time in seconds

# If You Want Error Message In Your Personal Message Then Turn It True Else If You Don't Want Then Flase
ERROR_MESSAGE = bool(os.environ.get('ERROR_MESSAGE', True))
