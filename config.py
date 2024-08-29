from os import getenv
from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID", "25581940"))
API_HASH = getenv("API_HASH" , "1e80acd755ceab02b3e2a22d49b25c18")

BOT_TOKEN = getenv("BOT_TOKEN" , "7344614680:AAHzbJqWxPLErNB63AgOcgxSYYLyBstJT3c")
#OWNER_ID = int(getenv("7496416021"))
OWNER_ID = int(getenv("OWNER_ID", "7496416021"))
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://Lucky:Lucky@atlascluster.f7lck9c.mongodb.net/?retryWrites=true&w=majority")
MUST_JOIN = getenv("MUST_JOIN", "demon_squad_help_desk")
