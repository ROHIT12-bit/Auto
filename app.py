# app.py
import threading
from flask import Flask
from pyrogram import Client
from config import Config

app = Flask(__name__)

@app.route('/')
def home():
    return "✅ Auto Approval Bot is online!"

def run_bot():
    plugins = dict(root="plugins")
    Bot = Client(
        "AutoApproveBot",
        api_id=Config.API_ID,
        api_hash=Config.API_HASH,
        bot_token=Config.BOT_TOKEN,
        plugins=plugins
    )
    Bot.run()

if __name__ == "__main__":
    threading.Thread(target=run_bot).start()
    app.run(host="0.0.0.0", port=8080)
