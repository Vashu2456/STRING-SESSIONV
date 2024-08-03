from os import getenv
from dotenv import load_dotenv

load_dotenv()
API_ID = int(getenv("API_ID", "19197570"))
API_HASH = getenv("API_HASH", "0401e837796d193ec9ae6e17cb8cfbf8")

BOT_TOKEN = getenv("BOT_TOKEN", "7291541483:AAHHpQrh3xanO3joNs7z32Jt8umDx-XoURM")
OWNER_ID = int(getenv("OWNER_ID", "6798074818"))

MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://monivps5:monivps5@cluster0.kmbq8we.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
MUST_JOIN = getenv("MUST_JOIN", "TMK_MUSICCHANNEL")
