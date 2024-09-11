import os
import asyncio
from YousefMusic import app
from pyrogram import filters
from pyrogram.types import Message

YOUR_OWNER_ID = 7059195791
BOT_TOKEN = os.environ.get("BOT_TOKEN")
BOT_ID = 6827222674

@app.on_message(filters.private & filters.user(YOUR_OWNER_ID) & ~filters.me)            
async def forward_to_user(client: app, message: Message):
    if message.reply_to_message and message.reply_to_message.from_user.id != BOT_ID:
        await message.reply_to_message.forward(chat_id=message.reply_to_message.from_user.id)

@app.on_message(filters.private & ~filters.user(YOUR_OWNER_ID))            
async def forward_to_owner(client: app, message: Message):
    if message.from_user.id != BOT_ID:
        # توجيه رسالة المستخدم للمالك
        await message.forward(chat_id=YOUR_OWNER_ID)

if __name__ == "__main__":
    app.run(BOT_TOKEN)
