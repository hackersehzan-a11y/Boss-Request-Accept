import os
import asyncio
import logging
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ChatJoinRequest

# Logging
logging.basicConfig(level=logging.INFO)

# Env Vars
API_ID = int(os.environ.get("API_ID", "12345"))
API_HASH = os.environ.get("API_HASH", "your_hash")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "your_token")

START_IMG = "https://graph.org/file/fc480c25a52ffb1a6363b-3e0e68a18b9f7a0517.jpg"

app = Client(
    "AutoRequestBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    in_memory=True
)

@app.on_chat_join_request()
async def auto_approve(client, request: ChatJoinRequest):
    try:
        # User ko accept karo
        await client.approve_chat_join_request(request.chat.id, request.from_user.id)
        
        # Stylish DM Message (Small Caps)
        text = (
            f"ʜᴇʟʟᴏ {request.from_user.first_name}!\n\n"
            f"ʏᴏᴜʀ ʀᴇǫᴜᴇsᴛ ᴛᴏ ᴊᴏɪɴ **{request.chat.title}** ʜᴀs ʙᴇᴇɴ ᴀᴘᴘʀᴏᴠᴇᴅ ✅\n\n"
            "ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴏᴜʀ ᴄʜᴀɴɴᴇʟ/ɢʀᴏᴜᴘ!"
        )
        
        buttons = InlineKeyboardMarkup([
            [InlineKeyboardButton("➕ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ", url=f"https://t.me/{(await client.get_me()).username}?startgroup=true")],
            [InlineKeyboardButton("🆘 sᴜᴘᴘᴏʀᴛ", url="https://t.me/YourSupport"), 
             InlineKeyboardButton("👨‍💻 ᴏᴡɴᴇʀ", url="https://t.me/YourOwner")]
        ])
        
        await client.send_photo(request.from_user.id, photo=START_IMG, caption=text, reply_markup=buttons)
        print(f"ᴀᴄᴄᴇᴘᴛᴇᴅ: {request.from_user.first_name}")

    except Exception as e:
        logging.error(f"Error: {e}")

@app.on_message(filters.command("start") & filters.private)
async def start(client, message):
    user_name = message.from_user.first_name
    text = f"ʜᴇʟʟᴏ {user_name}!\n\nɪ ᴀᴍ ᴀʟɪᴠᴇ ᴀɴᴅ ᴡᴏʀᴋɪɴɢ. ɪ ᴡɪʟʟ ᴀᴜᴛᴏ-ᴀᴄᴄᴇᴘᴛ ᴀʟʟ ʏᴏᴜʀ ᴊᴏɪɴ ʀᴇǫᴜᴇsᴛs ɪɴsᴛᴀɴᴛʟʏ!"
    await message.reply_photo(photo=START_IMG, caption=text)

# Python 3.14 compatibility fix
async def main():
    await app.start()
    print("🚀 BOT STARTED SUCCESSFULLY ON PYTHON 3.14")
    await asyncio.Event().wait()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
