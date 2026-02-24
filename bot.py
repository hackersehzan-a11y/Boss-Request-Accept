import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ChatJoinRequest

# Bot Credentials (Environment Variables)
API_ID = int(os.environ.get("API_ID", "12345"))
API_HASH = os.environ.get("API_HASH", "your_hash")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "your_token")

app = Client("AutoAcceptBot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

START_IMG = "https://graph.org/file/fc480c25a52ffb1a6363b-3e0e68a18b9f7a0517.jpg"

@app.on_chat_join_request()
async def accept_request(client, request: ChatJoinRequest):
    user_id = request.from_user.id
    chat_name = request.chat.title
    
    try:
        # Request Accept Karein
        await client.approve_chat_join_request(request.chat.id, user_id)
        
        # User ko Stylish DM bhejein
        text = f"ʜᴇʟʟᴏ {request.from_user.first_name}!\n\nʏᴏᴜʀ ʀᴇǫᴜᴇsᴛ ᴛᴏ ᴊᴏɪɴ **{chat_name}** ʜᴀs ʙᴇᴇɴ ᴀᴘᴘʀᴏᴠᴇᴅ. ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴏᴜʀ ᴄᴏᴍᴍᴜɴɪᴛʏ!"
        
        buttons = InlineKeyboardMarkup([
            [InlineKeyboardButton("➕ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ", url=f"https://t.me/{(await client.get_me()).username}?startgroup=true")],
            [InlineKeyboardButton("👨‍💻 ᴏᴡɴᴇʀ", url="https://t.me/YourUsername"), 
             InlineKeyboardButton("🆘 sᴜᴘᴘᴏʀᴛ", url="https://t.me/YourSupportGroup")],
            [InlineKeyboardButton("❓ ʜᴇʟᴘ", callback_data="help_msg")]
        ])
        
        await client.send_photo(user_id, photo=START_IMG, caption=text, reply_markup=buttons)
        
    except Exception as e:
        print(f"Error: {e}")

@app.on_message(filters.command("start"))
async def start_cmd(client, message):
    await message.reply_text("ʙᴏᴛ ɪs ᴀʟɪᴠᴇ ᴀɴᴅ ᴡᴏʀᴋɪɴɢ! ɪ ᴡɪʟʟ ᴀᴜᴛᴏ-ᴀᴄᴄᴇᴘᴛ ᴀʟʟ ᴊᴏɪɴ ʀᴇǫᴜᴇsᴛs.")

print("Bot is Starting...")
app.run()
