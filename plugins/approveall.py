# plugins/approveall.py
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio

@Client.on_message(filters.command("approveall") & filters.private)
async def approve_all_guide(client, message):
    # 🕒 Step 1: Temporary "Hold" message
    temp_msg = await message.reply("<code>Hᴏʟᴅ ᴜᴘ, ᴄᴜᴛɪᴇ... ɴᴏᴛ sᴏ ғᴀsᴛ</code>")
    await asyncio.sleep(2)
    await temp_msg.edit("<code>Dᴏɴᴇ sᴇɴᴅɪɴɢ</code>")
    await asyncio.sleep(1)
    await temp_msg.delete()

    # 🖼 Step 2: Sticker
    await client.send_sticker(
        chat_id=message.chat.id,
        sticker="CAACAgUAAxkBAAEin5FoTUn9ef0gFsZtJhlgTWCtH5jI-gACHgoAAsmuGVVnKBvEVZZMvDYE"
    )

    # 📜 Step 3: Guide Message
    await client.send_photo(
        chat_id=message.chat.id,
        photo="https://i.ibb.co/RwcRQyk/6ca3f606cad4.jpg",
        caption=(
            "<b>𝗙𝗢𝗟𝗟𝗢𝗪 𝗧𝗛𝗘𝗦𝗘 𝗦𝗧𝗘𝗣𝗦</b>\n\n"
            "<b>➥ Sᴛᴇᴘ 1:</b> Aᴅᴅ <b>@AniXApproveBot</b> ᴛᴏ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ.\n"
            "<b>➥ Sᴛᴇᴘ 2:</b> Mᴀᴋᴇ ɪᴛ ᴀɴ ᴀᴅᴍɪɴ ᴡɪᴛʜ ᴀᴅᴅ ᴜsᴇʀs ᴘᴇʀᴍɪssɪᴏɴ.\n"
            "<b>➥ Sᴛᴇᴘ 3:</b> Sᴇɴᴅ <code>/acceptall</code> ɪɴ ᴛʜᴀᴛ ᴄʜᴀɴɴᴇʟ ᴛᴏ ᴀᴜᴛᴏ-ᴀᴘᴘʀᴏᴠᴇ ᴀʟʟ ᴘᴇɴᴅɪɴɢ ʀᴇǫᴜᴇsᴛꜱ.\n\n"
            "⚠️ <i>Tip: Rᴇᴍᴏᴠᴇ ᴍᴇ ᴀғᴛᴇʀ ᴛʜᴇ ᴡᴏʀᴋ ɪs ᴅᴏɴᴇ.</i>"
        ),
        parse_mode="html",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("Sᴜᴘᴘᴏʀᴛ", url="https://t.me/StrawHatsXAnime")],
            [
                InlineKeyboardButton("Dᴇᴠᴇʟᴏᴘᴇʀ", url="https://t.me/Otakukart7"),
                InlineKeyboardButton("Cʟᴏsᴇ ✖️", callback_data="close")
            ]
        ])
    )
