from os import getenv

class Config:
    API_ID = int(getenv("API_ID", "20793620"))  # replace with your default/fallback
    API_HASH = getenv("API_HASH", "a712d2b8486f26c4dee5127cc9ae0615")
    BOT_TOKEN = getenv("BOT_TOKEN", "7865046885:AAFqyAAfNAxgyderBQwts1WPJCcADjhVhzw")
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://pokemonchannel098:yaE7BvFwWIXdb3HQ@cluster0.gdr57.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    DB_NAME = getenv("DB_NAME", "AutoApproveDB")
    OWNER_ID = int(getenv("OWNER_ID", "6853851676"))  # optional, but useful for admin checks
    ADMINS = list(map(int, os.getenv("ADMINS", "").split()))
