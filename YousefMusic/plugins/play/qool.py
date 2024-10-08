from pyrogram import Client, filters
from pyrogram.types import Message
from gtts import gTTS
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import os
from YousefMusic import app
from config import *


@app.on_message(filters.command("قولي", ""))
async def speak(_, message: Message):
    chat_id = message.chat.id
    data = message.text.split(maxsplit=1)
    if len(data) < 2:return await message.reply("↢ اكتب قول + الجمله \nمثال : قول مازن \n√", reply_to_message_id=message.id)
    wait = await message.reply('↢ المره الجايه هتدفع 100ج عشان الامر بصوت بنت', reply_to_message_id=message.id)
    if data[1].isascii():
        language = 'en'
    else:
        language = 'ar'
    audio = gTTS(text=data[1], lang=language)
    audio.save(f"{message.from_user.username}.mp3"),

    with open(f"{message.from_user.username}.mp3", "rb") as audio:
        await app.send_voice(chat_id=chat_id, voice=audio, reply_to_message_id=message.id)
        await wait.delete()
    os.remove(f"{message.from_user.username}.mp3"),
