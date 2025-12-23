from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio

@Client.on_message(filters.command("myid") & filters.private)
async def user_id_message(client, message):
    # Step 1: Fetching message
    loading = await message.reply("<code>Fᴇᴛᴄʜɪɴɢ ʏᴏᴜʀ ɪɴғᴏʀᴍᴀᴛɪᴏɴ...</code>")
    await asyncio.sleep(2)
    await loading.edit("<code>Dᴏɴᴇ Sᴇɴᴅɪɴɢ...</code>")
    await asyncio.sleep(1)
    await loading.delete()

    # Step 2: Sticker
    await client.send_sticker(
        chat_id=message.chat.id,
        sticker="CAACAgUAAxkBAAEin5FoTUn9ef0gFsZtJhlgTWCtH5jI-gACHgoAAsmuGVVnKBvEVZZMvDYE"
    )

    # Step 3: Final message
    await client.send_photo(
        chat_id=message.chat.id,
        photo="https://i.ibb.co/vx2JCHD/ca944da5a91d.jpg",
        caption=(
            "<blockquote>Yᴏᴜʀ ᴜsᴇʀ ɪᴅ ɪs... <code>{}</code>\n\n"
            "ʙᴜᴛ ᴏʀ ᴍᴀʏʙᴇ ɪᴛ'ꜱ ᴛɪᴍᴇ ɪ ɢᴇᴛ ᴛᴏ ᴋɴᴏᴡ ʏᴏᴜ ʙᴇᴛᴛᴇʀ , ᴄᴏᴍᴘʟᴇᴛᴇʟʏ </blockquote>"
        ).format(message.from_user.id),
        parse_mode="html",
        reply_markup=InlineKeyboardMarkup([
            [
                InlineKeyboardButton("Dᴇᴠᴇʟᴏᴘᴇʀ", url="https://t.me/Otakukart7"),
                InlineKeyboardButton("Cʟᴏsᴇ ✖️", callback_data="close")
            ]
        ]),
        message_effect_id=5104841245755180586
    )
