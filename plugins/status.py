from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio
import time

# Store bot start time
BOT_START_TIME = time.time()

@Client.on_message(filters.command("status") & filters.private)
async def status_handler(client, message):
    # Step 1: Temp loading
    temp = await message.reply("<code>Fᴇᴛᴄʜɪɴɢ ʙᴏᴛ ᴅᴀᴛᴀ...</code>")
    await asyncio.sleep(2)
    await temp.edit("<code>ᴅᴏɴᴇ ɢᴀᴛʜᴇʀɪɴɢ...</code>")
    await asyncio.sleep(1)
    await temp.delete()

    # Step 2: Firework sticker
    await client.send_sticker(
        chat_id=message.chat.id,
        sticker="CAACAgUAAxkBAAEin5FoTUn9ef0gFsZtJhlgTWCtH5jI-gACHgoAAsmuGVVnKBvEVZZMvDYE"
    )

    # Step 3: Uptime calc
    uptime = time.time() - BOT_START_TIME
    uptime_str = time.strftime("%Hh %Mm %Ss", time.gmtime(uptime))

    # Fake data placeholders (replace with real DB later)
    total_users = 1234
    total_admins = 5

    # Step 4: Status report
    await client.send_photo(
        chat_id=message.chat.id,
        photo="https://i.ibb.co/vx2JCHD/ca944da5a91d.jpg",
        caption=(
            "<b><i> » Bᴏᴛ Sᴛᴀᴛᴜꜱ ʀᴇᴘᴏʀᴛ</i></b>\n\n"
            "⫸ <b>Tᴏᴛᴀʟ Uꜱᴇʀꜱ</b> : <code>{}</code>\n"
            "⫸ <b>Aᴅᴍɪɴꜱ</b> : <code>{}</code>\n"
            "⫸ <b>Uᴘᴛɪᴍᴇ</b> : <code>{}</code>\n\n"
            "<i>ʜᴜɴᴛᴇʀ x ɴᴇᴠᴇʀ sʟᴇᴇᴘꜱ...</i>"
        ).format(total_users, total_admins, uptime_str),
        parse_mode="html",
        reply_markup=InlineKeyboardMarkup([
            [
                InlineKeyboardButton("Dᴇᴠᴇʟᴏᴘᴇʀ", url="https://t.me/Otakukart7"),
                InlineKeyboardButton("Cʟᴏꜱᴇ ✖️", callback_data="close")
            ]
        ]),
        message_effect_id=5104841245755180586
    )
