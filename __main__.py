from pyrogram import Client
from config import Config  # Ensure this exists and correctly provides API_ID, API_HASH, BOT_TOKEN

# Define plugin directory
plugins = dict(root="plugins")

# Initialize Pyrogram client
Bot = Client(
    "AutoApproveBot",
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    bot_token=Config.BOT_TOKEN,
    plugins=plugins
)

if __name__ == "__main__":
    print(">> Auto Approval Bot Started Successfully! <<")
    Bot.run()
