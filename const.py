# Used for identify features etc., DO NOT MODIFY
VERSION = "0.4"
# DO NOT MODIFY END

TIME_BETWEEN_CHECK = os.environ.get('TIME_BETWEEN_CHECK', 10)
TIME_BETWEEN_CLEAR = os.environ.get('TIME_BETWEEN_CLEAR', 3600) # An hour
EXPIRY_TIME = os.environ.get('EXPIRY_TIME', 21600) # 6 hours
HTTP_RETRY = os.environ.get('HTTP_RETRIES', 3)

BASE_JSON_DIR = "jsons"
LOGS_DIR = "logs"

CHANNELS_JSON = "channels.json"
FETCHED_JSON = "fetched.json"

# Cookie file for login required streams. You can get your cookie with FF or Chrome extensions like "cookies.txt" (Just check https://addons.mozilla.org/ or https://chrome.google.com/webstore/)
COOKIE = os.environ.get('COOKIE', None)

# Use multi-IPs for checking. One IP per line. Also make sure that each IP is set as individual address on your interface, IP-Ranges dont work.
IP_POOL = os.environ.get('IP_POOL', None)

# Send to discord on video privated
ENABLE_PRIVATE_CHECK = os.environ.get('ENABLE_PRIVATE_CHECK', False)

# Enable Live stream download
# Replace None with file path e.g. DOWNLOAD = r"H:\DownloadArchive\%(channel)s\%(upload_date)s - %(title)s\%(upload_date)s - %(title)s (%(id)s)"
DOWNLOAD = os.environ.get('DOWNLOAD', None)
MEMBER_DOWNLOAD = os.environ.get('MEMBER_DOWNLOAD', None)
PREMIERE_DOWNLOAD = os.environ.get('PREMIERE_DOWNLOAD', None)
PRIVATED_DOWNLOAD = os.environ.get('PRIVATED_DOWNLOAD', None)

HOSHINOVA_HOST = os.environ.get('HOSHINOVA_HOST', None) # e.g `127.0.0.1` or `hoshinova`
HOSHINOVA_PORT = os.environ.get('HOSHINOVA_PORT', None) # e.g 1104
HOSHINOVA_DOWNLOAD = os.environ.get('HOSHINOVA_DOWNLOAD', None) # eg. "D:\\example"
HOSHINOVA_MEMBER_DOWNLOAD = os.environ.get('HOSHINOVA_MEMBER_DOWNLOAD', None) # eg. "D:\\members_example"
HOSHINOVA_PREMIERE_DOWNLOAD = os.environ.get('HOSHINOVA_PREMIERE_DOWNLOAD', None) # eg. "D:\\premiere_example"

# Number of threads for pekopeko's ytarchive-raw-go
PRIVATED_DOWNLOAD_THREADS = os.environ.get('PRIVATED_DOWNLOAD_THREADS', 24)

# Callbacks
ENABLED_MODULES = {
    "discord": False,
    "telegram": False
}

# If you dont know how to create a Discord webhook read here: https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks
DISCORD_WEBHOOK_URL = os.environ.get('DISCORD_WEBHOOK_URL', None)
DISCORD_SEND_FILES = os.environ.get('DISCORD_SEND_FILES', False)
DISCORD_TOKEN = os.environ.get('DISCORD_TOKEN', None)

TELEGRAM_BOT_TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN', None)
TELEGRAM_CHAT_ID = os.environ.get('TELEGRAM_CHAT_ID', None)
TELEGRAM_SEND_FILES = os.environ.get('TELEGRAM_SEND_FILES', False)

# On live
ENABLED_MODULES_ONLIVE = {
    "discord": False,
    "telegram": False,
    "pushalert": False,
    "fcm": False
}

DISCORD_WEBHOOK_URL_ONLIVE = os.environ.get('DISCORD_WEBHOOK_URL_ONLIVE', None)
DISCORD_WEBHOOK_URL_MEMBERS = os.environ.get('DISCORD_WEBHOOK_URL_MEMBERS', None)
DISCORD_WEBHOOK_URL_PREMIERE = os.environ.get('DISCORD_WEBHOOK_URL_PREMIERE', None)

TELEGRAM_BOT_TOKEN_ONLIVE = TELEGRAM_BOT_TOKEN
TELEGRAM_CHAT_ID_ONLIVE = os.environ.get('TELEGRAM_CHAT_ID_ONLIVE', None)

PUSHALERT_API_KEY = os.environ.get('PUSHALERT_API_KEY', None)
PUSHALERT_ICON = os.environ.get('PUSHALERT_ICON', None)

FCM_API_KEY = os.environ.get('FCM_API_KEY', None)
FCM_ICON = os.environ.get('FCM_ICON', None)
FCM_TARGET = os.environ.get('FCM_TARGET', '/topic/all')

# ====== Chat Downloader ====== #
# `pip install chat_downloader`
CHAT_DIR = os.environ.get('CHAT_DIR', None)

CHAT_INACTIVITY_DURATION = os.environ.get('CHAT_INACTIVITY_DURATION', 30)
CHAT_BUFFER_TIME = os.environ.get('CHAT_BUFFER_TIME', 1)
CHAT_TASK_CLEAR_INTERVAL = os.environ.get('CHAT_TASK_CLEAR_INTERVAL', 300)

# `pip install brotlipy`
# `pip install zstandard`
CHAT_COMPRESS = os.environ.get('CHAT_COMPRESS', None) # None, "brotli", "zstd"
# ====== Chat Downloader END ====== #

CALLBACK_AFTER_EXPIRY = os.environ.get('CALLBACK_AFTER_EXPIRY', False)
CHAT_CALLBACK_AFTER_EXPIRY = os.environ.get('CHAT_CALLBACK_AFTER_EXPIRY', False)
