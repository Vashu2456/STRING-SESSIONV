from os import getenv
from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID", "25581940"))
API_HASH = getenv("API_HASH" , "1e80acd755ceab02b3e2a22d49b25c18")

BOT_TOKEN = getenv("BOT_TOKEN" , "7344614680:AAHzbJqWxPLErNB63AgOcgxSYYLyBstJT3c")
#OWNER_ID = int(getenv("7496416021"))
OWNER_ID = int(getenv("OWNER_ID", "7496416021"))
MONGO_DB_URI = getenv("MONGO_DB_URI", " mongodb+srv://vobero4050:rMDlUdxhAw9MDeaO@cluster2345908.hlfgzxh.mongodb.net/?retryWrites=true&w=majority&appName=Cluster2345908")
MUST_JOIN = getenv("MUST_JOIN", "DEMON_SQUAD_001")
