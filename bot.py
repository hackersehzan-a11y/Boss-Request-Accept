import os
import logging
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ChatJoinRequest

# Logging setup (Render logs me error dekhne ke liye)
logging.basicConfig(level=logging.INFO)

# Environment Variables
API_ID = os.environ.get("23903140")
API_HASH = os.environ.get("579f1bcf3eac1660d81ef34b09906012")
BOT_TOKEN = os.environ.get("BOT_TOKEN")

# Check if vars are missing
if not all([API_ID, API_HASH, BOT_TOKEN]):
    print("❌ ERROR: API_ID, API_HASH, or BOT_TOKEN is missing in Render Env Vars!")
    exit(1)

app = Client(
    "AutoAcceptBot",
    api_id=int(API_ID),
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

START_IMG = "https://graph.org/file/fc480c25a52ffb1a6363b-3e0e68a18b9f7a0517.jpg"

@app.on_chat_join_request()
async def handle_request(client, request: ChatJoinRequest):
    try:
        # User ko accept karo
        await client.approve_chat_join_request(request.chat.id, request.from_user.id)
        
        # Stylish DM Message
        text = (
            f"ʜᴇʟʟᴏ {request.from_user.first_name}!\n\n"
            f"ʏᴏᴜʀ ʀᴇǫᴜᴇsᴛ ᴛᴏ ᴊᴏɪɴ **{request.chat.title}** ʜᴀs ʙᴇᴇɴ ᴀᴘᴘʀᴏᴠᴇᴅ ✅\n\n"
            "ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴛʜᴇ ᴄᴏᴍᴍᴜɴɪᴛʏ!"
        )
        
        buttons = InlineKeyboardMarkup([
            [InlineKeyboardButton("➕ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ", url=f"https://t.me/{(await client.get_me()).username}?startgroup=true")],
            [InlineKeyboardButton("🆘 sᴜᴘᴘᴏʀᴛ", url="https://t.me/YourSupport"), 
             InlineKeyboardButton("👨‍💻 ᴏᴡɴᴇʀ", url="https://t.me/YourOwner")]
        ])
        
        await client.send_photo(request.from_user.id, photo=START_IMG, caption=text, reply_markup=buttons)
        
        # LOGGING FOR YOU (As per your saved info)
        print(f"ʟᴏɢ: ɴᴇᴡ ᴜsᴇʀ {request.from_user.id} ᴀᴄᴄᴇᴘᴛᴇᴅ ɪɴ {request.chat.id}")

    except Exception as e:
        logging.error(f"Error in auto-accept: {e}")

@app.on_message(filters.command("start") & filters.private)
async def start(client, message):
    text = "ʙᴏᴛ ɪs ʀᴜɴɴɪɴɢ ᴘᴇʀғᴇᴄᴛʟʏ! ɪ ᴡɪʟʟ ᴀᴜᴛᴏ-ᴀᴄᴄᴇᴘᴛ ᴀʟʟ ᴊᴏɪɴ ʀᴇǫᴜᴇsᴛs."
    await message.reply_text(text)

if __name__ == "__main__":
    print("🚀 Bot Started Successfully!")
    app.run()
