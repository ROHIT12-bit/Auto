from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio

@Client.on_message(filters.command("help") & filters.private)
async def help_cmd(client, message):
    # Step 1: Create temporary message
    progress = await message.reply("<code>Cʀᴇᴀᴛɪɴɢ ᴍᴇssᴀɢᴇ...</code>")
    await asyncio.sleep(2)
    await progress.edit("<code>Dᴏɴᴇ sᴇɴᴅɪɴɢ...</code>")
    await asyncio.sleep(1)
    await progress.delete()

    # Step 2: Send sticker
    await client.send_sticker(
        chat_id=message.chat.id,
        sticker="CAACAgUAAxkBAAEin5FoTUn9ef0gFsZtJhlgTWCtH5jI-gACHgoAAsmuGVVnKBvEVZZMvDYE"
    )

    # Step 3: Final photo message with blockquote
    await client.send_photo(
        chat_id=message.chat.id,
        photo="https://i.ibb.co/YFsddVdW/08e1dd709652.jpg",
        caption=(
            "<blockquote><b>𝗨𝗦𝗘𝗥 𝗚𝗨𝗜𝗗𝗘</b></blockquote>\n\n"
            "<blockquote>➥ Kɪɴᴅʟʏ ᴀᴅᴅ ᴛʜɪs ʙᴏᴛ ᴛᴏ ʏᴏᴜʀ ᴇsᴛᴇᴇᴍᴇᴅ ᴄʜᴀɴɴᴇʟ, ᴀɴᴅ ɪᴛ ᴡɪʟʟ "
            "ɢʀᴀᴄᴇғᴜʟʟʏ ʙᴇɢɪɴ ᴀᴘᴘʀᴏᴠɪɴɢ ᴀʟʟ ɴᴇᴡ ᴍᴇᴍʙᴇʀs ᴡɪᴛʜ ᴇғғɪᴄɪᴇɴᴄʏ ᴀɴᴅ ᴄᴀʀᴇ.</blockquote>"
        ),
        parse_mode="html",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("Dᴇᴠᴇʟᴏᴘᴇʀ", url="https://t.me/Otakukart7")],
            [
                InlineKeyboardButton("Mᴀɪɴ ᴄʜᴀɴɴᴇʟ", url="https://t.me/StrawHatsXAnime"),
                InlineKeyboardButton("Sᴜᴘᴘᴏʀᴛ", url="https://t.me/StrawHatsXAnime")
            ],
            [InlineKeyboardButton("Cʟᴏsᴇ ✖️", callback_data="close")]
        ]),
        message_effect_id=5104841245755180586  # 🎉 Firework animation
    )
