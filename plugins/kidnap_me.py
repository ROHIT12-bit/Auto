from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio

@Client.on_message(filters.command("kidnap_me") & filters.private)
async def kidnap_me(client, message):
    # Step 1: Temporary message
    temp_msg = await message.reply(
        "<code>Gᴇɴ Mᴇssᴀɢᴇ... ᴏʜ, ᴅᴏ ʏᴏᴜ ᴋɴᴏᴡ\nᴡʜᴀᴛ ɪ'ᴍ ᴛʜɪɴᴋɪɴɢ?</code>"
    )
    await asyncio.sleep(2)
    await temp_msg.edit(
        "<code>Dᴏɴᴇ sᴇɴᴅɪɴɢ... ᴡᴏʏᴏᴜ ʜɪᴛ ᴍʏ ᴍɪɴᴅ, ɴᴏᴡ ?</code>"
    )
    await asyncio.sleep(1)
    await temp_msg.delete()

    # Step 2: Sticker
    await client.send_sticker(
        chat_id=message.chat.id,
        sticker="CAACAgUAAxkBAAEin5FoTUn9ef0gFsZtJhlgTWCtH5jI-gACHgoAAsmuGVVnKBvEVZZMvDYE"
    )

    # Step 3: Main message
    await client.send_photo(
        chat_id=message.chat.id,
        photo="https://i.ibb.co/7JjXq5s8/5aaac15c3b60.jpg",
        caption=(
            "<blockquote>Wʜᴇʀᴇ ᴅᴏ ʏᴏᴜ ᴅʀᴇᴀᴍ ᴏғ ᴘʟᴀᴄɪɴɢ ᴍᴇ... ɪɴ ᴛʜᴇ ᴄᴏʀɴᴇʀs ᴏғ ʏᴏᴜʀ ʜᴇᴀʀᴛ "
            "ᴡʜᴇʀᴇ ɴᴏ ᴏɴᴇ ᴇʟsᴇ ᴄᴀɴ ᴛᴏᴜᴄʜ, ᴏʀ ɪɴ ʏᴏᴜʀ ᴀʀᴍꜱ ᴡʜᴇʀᴇ ᴇᴠᴇʀʏ ʙᴇᴀᴛ ᴏғ ʏᴏᴜʀ ʜᴇᴀʀᴛ "
            "ᴡʜɪsᴘᴇʀs ᴍʏ ɴᴀᴍᴇ ?</blockquote>\n\n"
            "<blockquote>Cʜᴏᴏsᴇ ᴀɴ ᴏᴘᴛɪᴏɴ ʙᴇʟᴏᴡ :</blockquote>"
        ),
        parse_mode="html",
        reply_markup=InlineKeyboardMarkup([
            [
                InlineKeyboardButton("➕ Aᴅᴅ ᴍᴇ ᴛᴏ ᴄʜᴀɴɴᴇʟ", url="https://t.me/YourBotUsername?startchannel=true"),
                InlineKeyboardButton("➕ Aᴅᴅ ᴍᴇ ᴛᴏ ɢʀᴏᴜᴘ", url="https://t.me/YourBotUsername?startgroup=true")
            ],
            [InlineKeyboardButton("Cʟᴏsᴇ ✖️", callback_data="close")]
        ])
    )
