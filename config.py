import os

class Config:
    API_ID = int(os.getenv("API_ID", "26047636"))
    API_HASH = os.getenv("API_HASH", "d8b1ed69ae1f937c5dd4d3cc8c8de440")
    BOT_TOKEN = os.getenv("BOT_TOKEN", "8549321688:AAHnCSOG7AyFSHnT6VkDWyjFk8Y1cOEXvcw")
    MONGO_URI = os.getenv("MONGO_URI")
    DB_NAME = os.getenv("DB_NAME", "AutoApproveDB")
    OWNER_ID = int(os.getenv("OWNER_ID", "8367080346"))
    ADMINS = list(map(int, os.getenv("ADMINS", "8367080346").split()))
