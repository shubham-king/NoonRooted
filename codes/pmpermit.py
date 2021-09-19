
from pyrogram import Client
import asyncio
from config import SUDO_USERS, PMPERMIT , BOT_USERNAME 
from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from callsmusic.callsmusic import client as USER

PMSET =True
pchats = []

@USER.on_message(filters.text & filters.private & ~filters.me & ~filters.bot)
async def pmPermit(client: USER, message: Message):
    if PMPERMIT == "ENABLE":
        if PMSET:
            chat_id = message.chat.id
            if chat_id in pchats:
                return
            await USER.send_message(
                message.chat.id,
               f"🥴नमस्कार आप अभी  हमारे सहयोगी से बाते करने की कोशिश कर रहे है जो की अनिवार्य नहीं है। इसके बावजूद अगर अपने msg किया तो आप को ban कर दिया जाएगा।👇🏻",
                    reply_markup=InlineKeyboardMarkup(
                       [[
                          InlineKeyboardButton(
                             "Add Me", url="https://t.me/{BOT_USERNAME}?startgroup=true")
                       ],[
                          InlineKeyboardButton(
                             "😈ᴏꜰꜰɪᴄɪᴀʟ ᴄʜᴀᴛ", url="https://t.me/Chatting_Officials")
                       ],[
                          InlineKeyboardButton(
                             "ꜱᴏᴜʀᴄᴇ ᴄᴏᴅᴇ", url="https://github.com/shubham-king/IndianMusic)
                       ],[
                          InlineKeyboardButton(
                             "ꜱᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ", url="https://t.me/Music_Enviroment"),
                          InlineKeyboardButton(
                             "🎑 ᴜᴘᴅᴀᴛᴇꜱ ᴄʜᴀɴɴᴇʟꜱ", url="https://t.me/ShubhamMusics")
                       ]]
                    ))
            return

    

@Client.on_message(filters.command(["/pmchat"]))
async def bye(client: Client, message: Message):
    if message.from_user.id in SUDO_USERS:
        global PMSET
        text = message.text.split(" ", 1)
        queryy = text[1]
        if queryy == "on":
            PMSET = True
            await message.reply_text("Pmpermit turned on")
            return
        if queryy == "off":
            PMSET = None
            await message.reply_text("Pmpermit turned off")
            return

@USER.on_message(filters.text & filters.private & filters.me)        
async def autopmPermiat(client: USER, message: Message):
    chat_id = message.chat.id
    if not chat_id in pchats:
        pchats.append(chat_id)
        await message.reply_text("ये बात कर सकते है क्युकी अपने बात करनी शुरू की है।")
        return
    message.continue_propagation()    
    
@USER.on_message(filters.command("a", [".", ""]) & filters.me & filters.private)
async def pmPermiat(client: USER, message: Message):
    chat_id = message.chat.id
    if not chat_id in pchats:
        pchats.append(chat_id)
        await message.reply_text("आप अब बात कर सके है।")
        return
    message.continue_propagation()    
    

@USER.on_message(filters.command("da", [".", ""]) & filters.me & filters.private)
async def rmpmPermiat(client: USER, message: Message):
    chat_id = message.chat.id
    if chat_id in pchats:
        pchats.remove(chat_id)
        await message.reply_text("आप अब से बात नही कर सकते ।")
        return
    message.continue_propagation()    
