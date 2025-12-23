# plugins/acceptall.py
from pyrogram import Client, filters
from pyrogram.types import Message
from config import Config
from database import is_admin
import asyncio

@Client.on_message(filters.command("acceptall") & filters.group)
async def accept_all_requests(client: Client, message: Message):
    chat_id = message.chat.id
    user_id = message.from_user.id

    # 🛡 Check if user is OWNER or admin
    if user_id != Config.OWNER_ID and not is_admin(user_id):
        return await message.reply("<code>⛔ Yᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴀᴜᴛʜᴏʀɪᴢᴇᴅ ᴛᴏ ᴜꜱᴇ ᴛʜɪꜱ.</code>")

    # 📊 Initial status
    status_msg = await message.reply(
        "<code>➥ Sᴛᴀʀᴛɪɴɢ ᴛᴏ ᴀᴘᴘʀᴏᴠᴇ...</code>\n"
        "<code>❏ Aᴘᴘʀᴏᴠᴇᴅ : 0</code>\n"
        "<code>❏ Sᴋɪᴘᴘᴇᴅ : 0</code>\n"
        "<code>❏ Tᴏᴛᴀʟ : 0</code>",
        quote=True
    )

    approved = 0
    skipped = 0
    total = 0

    try:
        async for join_request in client.get_chat_join_requests(chat_id):
            total += 1
            try:
                await client.approve_chat_join_request(chat_id, join_request.user.id)
                approved += 1
            except Exception:
                skipped += 1

            # Update progress
            await status_msg.edit(
                f"<code>➥ Aᴘᴘʀᴏᴠɪɴɢ...</code>\n"
                f"<code>❏ Aᴘᴘʀᴏᴠᴇᴅ : {approved}</code>\n"
                f"<code>❏ Sᴋɪᴘᴘᴇᴅ : {skipped}</code>\n"
                f"<code>❏ Tᴏᴛᴀʟ : {total}</code>"
            )
            await asyncio.sleep(0.3)

    except Exception as e:
        await status_msg.edit(f"<code>⛔ Error:</code> <code>{e}</code>")
        return

    # ✅ Done
    await status_msg.edit(
        f"<code>✅ ᴀʟʟ ᴅᴏɴᴇ !</code>\n"
        f"<code>❏ Aᴘᴘʀᴏᴠᴇᴅ : {approved}</code>\n"
        f"<code>❏ Sᴋɪᴘᴘᴇᴅ : {skipped}</code>\n"
        f"<code>❏ Tᴏᴛᴀʟ : {total}</code>"
    )
