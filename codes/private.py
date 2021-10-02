from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_USERNAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("CAACAgQAAx0CTv65QgABBfJlYF6VCrGMm6OJ23AxHmD6qUSWESsAAhoQAAKm8XEeD5nrjz5IJFYeBA")
    await message.reply_text(
        f"""** नमस्कार, मैं एक बोट हुं जो आपके ग्रुप में गाना बजा सकता है। और अपका मनोरजन कर सकता हु। \n और साथ में मैं ग्रुप के VC Chat मे live stream भी STREAM कर सकता हु। \n\n संगीत क्या है : संगीत माधुर्य, सामंजस्य, ताल और समय के तत्वों के माध्यम से एक रचना का निर्माण करने के लिए ध्वनियों को समय पर व्यवस्थित करने की कला है। यह सभी मानव समाजों के सार्वभौमिक सांस्कृतिक पहलुओं में से एक है। 
                **""",
        reply_markup=InlineKeyboardMarkup(
                       [[
                          InlineKeyboardButton(
                             "📀 मुझे ग्रुप में जोड़ें", url="https://t.me/{bn}?startgroup=true")
                       ],[
                          InlineKeyboardButton(
                             "🌐 सूचनाएं", url="https://t.me/ShubhamMusics")
                       ],[
                          InlineKeyboardButton(
                             "ℹ️ सहायता ", url="https://t.me/Music_Enviroment")
                       ],[
                          InlineKeyboardButton(
                             "🏷️ दोस्तो से बाते ", url="https://t.me/Chatting_Officials"),
                          InlineKeyboardButton(
                             "🎑 Source Code", url="https://github.com/shubham-king/NoonRooted")
                       ]]
                    ))

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""** 🏷️नमस्कार, मैं एक बोट हुं जो आपके ग्रुप में गाना बजा सकता है। और अपका मनोरजन कर सकता हु। **""",
      reply_markup=InlineKeyboardMarkup(
                       [[
                          InlineKeyboardButton(
                             "🌐 सूचनाएं", url="https://t.me/ShubhamMusics")
                       ],[
                          InlineKeyboardButton(
                             "ℹ️ सहायता ", url="https://t.me/Music_Enviroment")
                       ],[
                          InlineKeyboardButton(
                             "🏷️ दोस्तो से बाते ", url="https://t.me/Chatting_Officials"),
                          InlineKeyboardButton(
                             "🎑 Source Code", url="https://github.com/shubham-king/IndianMusic")
                       ]]
                    ))


