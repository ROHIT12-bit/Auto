# plugins/broadcast.py
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import Config
from database import approved_users_col
import asyncio

def get_all_approved_users():
    users = set()
    for chat in approved_users_col.find():
        users.update(chat.get("approved", []))
    return list(users)

@Client.on_message(filters.command("broadcast") & filters.private)
async def broadcast_replied_message(client, message):
    if message.from_user.id != Config.OWNER_ID:
        return await message.reply("<code>⛔ Aᴄᴄᴇss ᴅᴇɴɪᴇᴅ. Oɴʟʏ ᴏᴡɴᴇʀ ᴄᴀɴ ʙʀᴏᴀᴅᴄᴀꜱᴛ.</code>")

    if not message.reply_to_message:
        return await message.reply("<code>💌 Rᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ʙʀᴏᴀᴅᴄᴀsᴛ</code>")

    status = await message.reply("<code>➥ Sᴇᴅᴜᴄɪɴɢ ᴀʟʟ ᴍʏ ᴜsᴇʀs...</code>")
    await asyncio.sleep(2)

    total = 0
    success = 0
    failed = 0

    for user_id in get_all_approved_users():
        try:
            await message.reply_to_message.copy(chat_id=user_id)
            success += 1
        except:
            failed += 1
        total += 1
        await asyncio.sleep(0.5)

    await status.edit(
        f"<b>🎯 Bʀᴏᴀᴅᴄᴀꜱᴛ Rᴇsᴜʟᴛ</b>\n\n"
        f"<code>➥ Tᴏᴛᴀʟ   : {total}</code>\n"
        f"<code>✔️ Sᴇɴᴛ    : {success}</code>\n"
        f"<code>❌ Fᴀɪʟᴇᴅ : {failed}</code>\n\n"
        f"<i>ɪ ʙʟᴇssᴇᴅ ᴛʜᴇᴍ ᴡɪᴛʜ ʏᴏᴜʀ ᴡᴏʀᴅs 💌</i>",
        parse_mode="html",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("✖️ Cʟᴏꜱᴇ", callback_data="close")]
        ])
            )
