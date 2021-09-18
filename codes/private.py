from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("CAACAgQAAx0CTv65QgABBfJlYF6VCrGMm6OJ23AxHmD6qUSWESsAAhoQAAKm8XEeD5nrjz5IJFYeBA")
    await message.reply_text(
        f"""**Hey, I'm {bn} 🎵

ɪ ᴄᴀɴ ᴘʟᴀʏ ᴍᴜꜱɪᴄ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ'ꜱ ᴠᴏɪᴄᴇ ᴄᴀʟʟ. ᴅᴇᴠᴇʟᴏᴘᴇᴅ ʙʏ [xᴍᴀʀᴛʏ ꜱᴀʟɪᴍ](https://t.me/Xmartperson).

ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴀɴᴅ ᴘʟᴀʏ ᴍᴜꜱɪᴄ ꜰʀᴇᴇʟʏ!**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🛠 ꜱᴏᴜʀᴄᴇ ᴄᴏᴅᴇ 🛠", url="https://github.com/S780821/XMARTY_MUSIC")
                  ],[
                    InlineKeyboardButton(
                        "💬 ɢʀᴏᴜᴘ", url="https://t.me/XMARTY_Support"
                    ),
                    InlineKeyboardButton(
                        "🔊 ᴄʜᴀɴɴᴇʟ", url="https://t.me/XMARTY_SUPPORT"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "➕ ʏʀʀ ᴍᴜᴊʜᴇ ɴᴀ ʟᴇ ᴊᴀᴏ ᴋʜᴜᴅ ᴋᴀ ʙɴᴀ ʟᴏ ➕", url="https://t.me/XMARTY_MUSIC_BOT?startgroup=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**ᴀʀᴇ ʏʀʀ ᴊɪɴᴅᴀ ʜᴏᴏ ✅**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔊 ᴄʜᴀɴɴᴇʟ", url="https://t.me/XMARTY_SUPPORT")
                ]
            ]
        )
   )


