from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from helpers.filters import other_filters2

@Client.on_message(filters.command("alive") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**नमस्कार , मैं  अभी काम कर सकता हु, आप मेरी चिंता ना करे।\n\n\n 🏷️Bot Status:- Working \n🏷️ Bot Uptime: Since Hosted\n 🏷️ Updates: UP-DATED\n 🏷️ MUSICAL BOT 😈😈**""",
      reply_markup=InlineKeyboardMarkup(
                       [[
                          InlineKeyboardButton(
                             "🌐 सूचनाएं", url="https://t.me/ShubhamMusics")
                       ],[
                          InlineKeyboardButton(
                             "🎑 Source Code", url="https://github.com/shubham-king/IndianMusic")
                       ]]
                    ))