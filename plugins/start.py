import asyncio
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Client.on_message(filters.command("start") & filters.private)
async def start_command(client, message):
    initial = await message.reply(
        "<code>ᴡᴇʟᴄᴏᴍᴇ, ʙᴀʙʏ...ɪ'ᴠᴇ ʙᴇᴇɴ ᴄʀᴀᴠɪɴɢ ʏᴏᴜʀ ᴘʀᴇsᴇɴᴄᴇ ғᴇᴇʟs ᴘᴇʀғᴇᴄᴛ ɴᴏᴡ ᴛʜᴀᴛ ʏᴏᴜ'ʀᴇ ʜᴇʀᴇ</code>",
        parse_mode="html"
    )

    await asyncio.sleep(1.8)
    await initial.edit_text("Sᴛᴀʀᴛɪɴɢ...")
    await asyncio.sleep(2)
    await initial.delete()

    await client.send_sticker(
        chat_id=message.chat.id,
        sticker="CAACAgUAAxkBAAEin5FoTUn9ef0gFsZtJhlgTWCtH5jI-gACHgoAAsmuGVVnKBvEVZZMvDYE"
    )

    await message.reply(
        "<code>Yᴏᴜ’ʀᴇ ᴀʟʟ sᴇᴛ, ʙᴀʙᴇ… ɴᴏᴡ ɢᴏ ᴏɴ ᴀɴᴅ ᴇɴᴊᴏʏ ᴛʜᴇ ʙᴏᴛ.</code>",
        parse_mode="html"
    )

    await client.send_photo(
        chat_id=message.chat.id,
        photo="https://i.ibb.co/HyNL4Xh/25f3a522b2b7.jpg",
        caption=(
            f"<b>Hᴇʏᴏ {message.from_user.first_name}</b>\n\n"
            "<code>I'ᴍ ᴀɴ Aᴜᴛᴏ Aᴘᴘʀᴏᴠᴇ Bᴏᴛ. Aᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴀɴᴅ ᴍᴀᴋᴇ ᴍᴇ ᴀɴ "
            "ᴀᴅᴍɪɴ ᴡɪᴛʜ ᴀᴅᴅ ᴍᴇᴍʙᴇʀs ᴘᴇʀᴍɪssɪᴏɴ.\n"
            "I'ʟʟ ʜᴀɴᴅʟᴇ ᴀᴘᴘʀᴏᴠᴀʟs ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ, sᴏ ʏᴏᴜ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴛᴏ.\n"
            "ʟᴇᴛ ᴍᴇ ᴅᴏ ᴛʜᴇ ʙᴏʀɪɴɢ sᴛᴜғғ.</code>"
        ),
        parse_mode="html",
        reply_markup=InlineKeyboardMarkup([
            [
                InlineKeyboardButton("Mᴀɪɴ ᴄʜᴀɴɴᴇʟ", url="https://t.me/StrawHatsXAnime"),
                InlineKeyboardButton("Sᴜᴘᴘᴏʀᴛ", url="https://t.me/StrawHatsXAnime")
            ],
            [
                InlineKeyboardButton("× Dᴇᴠᴇʟᴏᴘᴇʀ ×", url="https://t.me/Otakukart7")
            ],
            [
                InlineKeyboardButton("Aʙᴏᴜᴛ", callback_data="about"),
                InlineKeyboardButton("Cʟᴏsᴇ", callback_data="close")
            ]
        ])
    )

# ➕ About Button Handler
@Client.on_callback_query(filters.regex("about"))
async def about_callback(client, callback_query: CallbackQuery):
    await callback_query.message.edit_caption(
        caption=(
            "<b><blockquote>Sᴀʏ ʏᴇs ʜᴜɴᴛᴇʀ ɪ’ᴍ ᴀʟʟ ʏᴏᴜʀs.</blockquote></b>\n\n"
            "<blockquote>◈ Oᴡɴᴇʀ : <a href='https://t.me/Otakukart7'>ᴄʟɪᴄᴋ ʜᴇʀᴇ</a>\n"
            "◈ Dᴇᴠᴇʟᴏᴘᴇʀ : <a href='https://t.me/Otakukart7'>ᴄʟɪᴄᴋ ʜᴇʀᴇ</a>\n"
            "◈ Mᴀɪɴ Cʜᴀɴɴᴇʟ : <a href='https://t.me/StrawHatsXAnime'>ᴄʟɪᴄᴋ ʜᴇʀᴇ</a>\n"
            "◈ Sᴜᴘᴘᴏʀᴛ Cʜᴀɴɴᴇʟ : <a href='https://t.me/StrawHatsXAnime'>ᴄʟɪᴄᴋ ʜᴇʀᴇ</a>\n"
            "◈ Sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ : <a href='https://t.me/StrawHatsXAnime'>ᴄʟɪᴄᴋ ʜᴇʀᴇ</a></blockquote>"
        ),
        parse_mode="html",
        reply_markup=InlineKeyboardMarkup([
            [
                InlineKeyboardButton("« Bᴀᴄᴋ", callback_data="back"),
                InlineKeyboardButton("Close", callback_data="close")
            ]
        ])
    )

# ➕ Back and Close Handler
@Client.on_callback_query(filters.regex("back"))
async def back_callback(client, callback_query: CallbackQuery):
    await start_command(client, callback_query.message)

@Client.on_callback_query(filters.regex("close"))
async def close_callback(client, callback_query: CallbackQuery):
    await callback_query.message.delete()
