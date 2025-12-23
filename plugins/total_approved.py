from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio
from config import ADMINS
from database import get_all_approved_users

@Client.on_message(filters.command("total_approved") & filters.private)
async def total_approved_users(client, message):
    if message.from_user.id not in ADMINS:
        return await message.reply("<code>❌ Aᴄᴄᴇss Dᴇɴɪᴇᴅ ʙᴀʙʏ... Yᴏᴜ’ʀᴇ ɴᴏᴛ ᴀ ᴘᴀʀᴛ ᴏғ ᴍʏ ʀᴏʏᴀʟ ᴛᴇᴀᴍ 😤</code>")

    # Step 1: Loading message
    temp = await message.reply("<code>Gᴀᴛʜᴇʀɪɴɢ ᴀᴘᴘʀᴏᴠᴇᴅ ᴀɴɢᴇʟꜱ...</code>")
    await asyncio.sleep(2)
    await temp.delete()

    # Step 2: Get user count
    approved_users = await get_all_approved_users()
    total = len(approved_users)

    # Step 3: Style message
    await client.send_photo(
        chat_id=message.chat.id,
        photo="https://i.ibb.co/0tvBnDd/9ef221ea1e6f.jpg",
        caption=(
            "<b><i>✨ Tᴏᴛᴀʟ Aᴘᴘʀᴏᴠᴇᴅ ᴜsᴇʀs</i></b>\n\n"
            f"<code>➥ Aᴘᴘʀᴏᴠᴇᴅ ʜᴇᴀʀᴛꜱ ᴏɴ ᴍʏ ʟɪsᴛ: {total}</code>\n"
            "<i>ɴᴏᴛ ᴇᴠᴇʀʏᴏɴᴇ ɢᴇᴛꜱ ᴀᴘᴘʀᴏᴠᴇᴅ, ʙᴜᴛ ʏᴏᴜ ᴅɪᴅ 💘</i>"
        ),
        parse_mode="html",
        reply_markup=InlineKeyboardMarkup([
            [
                InlineKeyboardButton("👑 Mᴀɴᴀɢᴇ ᴀᴅᴍɪɴs", callback_data="admins_panel"),
                InlineKeyboardButton("✖️ Cʟᴏꜱᴇ", callback_data="close")
            ]
        ]),
        message_effect_id=5104841245755180586  # Optional: Fancy fireworks ✨
    )
