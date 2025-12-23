from pyrogram import Client
from config import Config  # Import the Config class

# Access the configuration values from the Config class
API_ID = Config.API_ID
API_HASH = Config.API_HASH
BOT_TOKEN = Config.BOT_TOKEN

app = Client(
    name="AutoApproveBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="plugins")  # Ensure the plugins directory exists
)

if __name__ == "__main__":
    app.run()
