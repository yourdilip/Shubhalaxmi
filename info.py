import re
import requests
from os import environ
from Script import script 

# Regex pattern for ID validation
id_pattern = re.compile(r'^.\d+$')

# Function to check if a setting is enabled
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Shortlink Function
def get_short_url(original_url):
    if IS_SHORTLINK:  # Check if shortlink mode is enabled
        api_url = f"https://{SHORTLINK_URL}/api"
        params = {
            'api': SHORTLINK_API,
            'url': original_url,
        }
        response = requests.get(api_url, params=params)
        if response.status_code == 200:
            data = response.json()
            if data.get("status") == "success":
                return data.get("shortenedUrl")
    return original_url  # Return the original URL if shortening fails

# Bot information
SESSION = environ.get('SESSION', 'TechVJBot')
API_ID = int(environ.get('API_ID', '2393757'))
API_HASH = environ.get('API_HASH', '89f1050bae8e86a68c3e2278bcfbfc9b')
BOT_TOKEN = environ.get('BOT_TOKEN', "7310217905:AAGvFevznbhKHk69SYLhsMp3-nccKb6G5HY")

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
PICS = (environ.get('PICS', 'https://te.legra.ph/file/00c2b881ab6dd8680b232.jpg')).split()
NOR_IMG = environ.get("NOR_IMG", "https://graph.org/file/b69af2db776e4e85d21ec.jpg")
MELCOW_VID = environ.get("MELCOW_VID", "https://t.me/DeiEppudra/5")
SPELL_IMG = environ.get("SPELL_IMG", "https://te.legra.ph/file/15c1ad448dfe472a5cbb8.jpg")

# Admins, Channels & Users
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002206464807'))
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '1078638766').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1001660466640 -1001505006734').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '1078638766').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []

# Auth channel
REQUEST_TO_JOIN_MODE = bool(environ.get('REQUEST_TO_JOIN_MODE', False))
TRY_AGAIN_BTN = bool(environ.get('TRY_AGAIN_BTN', False))
auth_channel = environ.get('AUTH_CHANNEL', '')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://rockerz2ktg:riyazkk2003@cluster0.jzchbww.mongodb.net/?retryWrites=true&w=majority")
DATABASE_NAME = environ.get('DATABASE_NAME', "cluster0")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')
IMDB = False  # Change to False if IMDb results should be disabled

# Premium And Referral Settings
PREMIUM_AND_REFERAL_MODE = bool(environ.get('PREMIUM_AND_REFERAL_MODE', False))
REFERAL_COUNT = int(environ.get('REFERAL_COUNT', '20'))
REFERAL_PREMEIUM_TIME = environ.get('REFERAL_PREMEIUM_TIME', '1month')

# Shortlink Info
SHORTLINK_MODE = bool(environ.get('SHORTLINK_MODE', True))
SHORTLINK_URL = environ.get('SHORTLINK_URL', 'publicearn.com')
SHORTLINK_API = environ.get('SHORTLINK_API', '998ddd78dda4c6984ae045c0f21bc71ef09672f1')
IS_SHORTLINK = bool(environ.get('IS_SHORTLINK', True))

# Function to create download button
def create_download_button(file_url):
    short_url = get_short_url(file_url)  # Use shortened URL if IS_SHORTLINK is enabled
    button = InlineKeyboardButton(text="Download", url=short_url)
    return button

# Others
MAX_B_TN = environ.get("MAX_B_TN", "5")
PORT = environ.get("PORT", "8080")
MSG_ALRT = environ.get('MSG_ALRT', 'Hello My Dear Friends ❤️')
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", f"{script.CAPTION}")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", f"{script.IMDB_TEMPLATE_TXT}")
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)

# Choose Option Settings 
LANGUAGES = ["malayalam", "mal", "tamil", "tam" ,"english", "eng", "hindi", "hin", "telugu", "tel", "kannada", "kan"]
SEASONS = ["season 1", "season 2", "season 3", "season 4", "season 5", "season 6", "season 7", "season 8", "season 9", "season 10"]
EPISODES = ["E01", "E02", "E03", "E04", "E05", "E06", "E07", "E08", "E09", "E10", "E11", "E12", "E13", "E14", "E15", "E16", "E17", "E18", "E19", "E20", "E21", "E22", "E23", "E24", "E25", "E26", "E27", "E28", "E29", "E30", "E31", "E32", "E33", "E34", "E35", "E36", "E37", "E38", "E39", "E40"]
QUALITIES = ["360p", "480p", "720p", "1080p", "1440p", "2160p"]
YEARS = ["1900", "1991", "1992", "1993", "1994", "1995", "1996", "1997", "1998", "1999", "2000", "2001", "2002", "2003", "2004", "2005", "2006", "2007", "2008", "2009", "2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022", "2023", "2024", "2025"]


                           # Don't Remove Credit @Rockerz2z
                           # Subscribe Telegram Channel For All Movies @Rockerz2z
                           # Ask Doubt on telegram @


# Online Stream and Download
STREAM_MODE = bool(environ.get('STREAM_MODE', True)) # Set True or False

# If Stream Mode Is True Then Fill All Required Variable, If False Then Don't Fill.
MULTI_CLIENT = False
SLEEP_THRESHOLD = int(environ.get('SLEEP_THRESHOLD', '60'))
PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
if 'DYNO' in environ:
    ON_HEROKU = True
else:
    ON_HEROKU = False
URL = environ.get("URL", "https://tough-willyt-riyazahamedkk-da7cd84e.koyeb.app/")


# Rename Info : If True Then Bot Rename File Else Not
RENAME_MODE = bool(environ.get('RENAME_MODE', False)) # Set True or False

# Auto Approve Info : If True Then Bot Approve New Upcoming Join Request Else Not
AUTO_APPROVE_MODE = bool(environ.get('AUTO_APPROVE_MODE', True)) # Set True or False

LOG_STR = "Current Cusomized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for you queries.\n" if IMDB else "IMBD Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found , Users will be redirected to send /start to Bot PM instead of sending file file directly\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled files will be send in PM, instead of sending start.\n")
LOG_STR += ("SINGLE_BUTTON is Found, filename and files size will be shown in a single button instead of two separate buttons\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled , filename and file_sixe will be shown as different buttons\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be send along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n")
LOG_STR += ("Long IMDB storyline enabled." if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled , Plot will be shorter.\n")
LOG_STR += ("Spell Check Mode Is Enabled, bot will be suggesting related movies if movie not found\n" if SPELL_CHECK_REPLY else "SPELL_CHECK_REPLY Mode disabled\n")
LOG_STR += (f"MAX_LIST_ELM Found, long list will be shortened to first {MAX_LIST_ELM} elements\n" if MAX_LIST_ELM else "Full List of casts and crew will be shown in imdb template, restrict them by adding a value to MAX_LIST_ELM\n")
LOG_STR += f"Your current IMDB template is {IMDB_TEMPLATE}"


# Don't Remove Credit @Rockerz2z
# Subscribe Telegram Channel For All Movies @Rockerz2z
# Ask Doubt on telegram @Rockerz2z
