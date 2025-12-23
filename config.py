from os import getenv

class Config:
    API_ID = int(getenv("API_ID", "26047636"))  # replace with your default/fallback
    API_HASH = getenv("API_HASH", "d8b1ed69ae1f937c5dd4d3cc8c8de440")
    BOT_TOKEN = getenv("BOT_TOKEN", "8549321688:AAHnCSOG7AyFSHnT6VkDWyjFk8Y1cOEXvcw")
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://pokemonchannel098:yaE7BvFwWIXdb3HQ@cluster0.gdr57.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    DB_NAME = getenv("DB_NAME", "AutoApproveDB")
    OWNER_ID = int(getenv("OWNER_ID", "8367080346"))  # optional, but useful for admin checks
    ADMINS = list(map(int, os.getenv("ADMINS", "").split()))
