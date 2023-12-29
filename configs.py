from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "21011056"))
    API_HASH = getenv("API_HASH", "696033b1a9c35f0dc027f8ecfbaa9645")
    BOT_TOKEN = getenv("BOT_TOKEN", "6320458686:AAEfXjxOus-sZy4o4QY3vYzzjUf0351RUZU")
    FSUB = getenv("FSUB", "anjaliautoapprovrbot")
    CHID = int(getenv("CHID", "-1001970031336"))
    SUDO = list(map(int, getenv("SUDO").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://Bikash:Bikash@bikash.yl2nhcy.mongodb.net/?retryWrites=true&w=majority")
    
cfg = Config()
