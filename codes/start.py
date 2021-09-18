from datetime import datetime
from time import time

from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup

from config import BOT_USERNAME
from helpers.decorators import sudo_users_only
from helpers.filters import command

START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)


async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)

@Client.on_message(filters.command("start"))
async def start(client, m: Message):
   if m.chat.type == 'private':
      await m.reply(f"🏷️ नमस्कार, मैं एक बोट हुं जो आपके ग्रुप में गाना बजा सकता है। और अपका मनोरजन कर सकता हु। \n\n संगीत क्या है : संगीत माधुर्य, सामंजस्य, ताल और समय के तत्वों के माध्यम से एक रचना का निर्माण करने के लिए ध्वनियों को समय पर व्यवस्थित करने की कला है। यह सभी मानव समाजों के सार्वभौमिक सांस्कृतिक पहलुओं में से एक है। ",
                    reply_markup=InlineKeyboardMarkup(
                       [[
                          InlineKeyboardButton(
                             "📀 मुझे ग्रुप में जोड़ें", url="https://t.me/{BOT_USERNAME}?startgroup=true")
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
                             "🎑 Source Code", url="https://github.com/shubham-king/IndianMusic")
                       ]]
                    ))
   else:
      await m.reply("**✨ अभी मैं जिंदा हूं सरजी... ✨**",
                          reply_markup=InlineKeyboardMarkup(
                       [[
                          InlineKeyboardButton(
                             "🌐 सूचनाएं", url="https://t.me/ShubhamMusics")
                       ],[
                          InlineKeyboardButton(
                             "🔥 ꜱᴏᴜʀᴄᴇ ᴄᴏᴅᴇ", url="https://github.com/shubham-king/IndianMusic")
                       ],[
                          InlineKeyboardButton(
                             "📚 सहायता", url="https://t.me/Music_Enviroment")
                       ]]
                    )
                    )

@Client.on_message(command(["alive", f"alive@{BOT_USERNAME}"]) & filters.group & ~filters.edited)
async def alive(_, m: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await m.reply_text(
        f"""✅ **मैं काम कर रहा हु**\n<b>💠 **uptime:**</b> `{uptime}`""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✨ बाते ", url=f"https://t.me/Chatting_Officials"
                    ),
                    InlineKeyboardButton(
                        "📣 सूचनाएं", url=f"https://t.me/ShubhamMusics"
                    )
                ]
            ]
        )
    )


@Client.on_message(command(["ping", f"ping@{BOT_USERNAME}"]) & ~filters.edited)
async def ping_pong(_, m: Message):
    sturt = time()
    m_reply = await m.reply_text("शुभम म्यूजिक...")
    delta_ping = time() - sturt
    await m_reply.edit_text(
        "🏓 ℙ𝕠𝕟𝕘`!!`\n"
        f"⚡️ `{delta_ping * 1000:.3f} ms`"
    )


@Client.on_message(command(["uptime", f"uptime@{BOT_USERNAME}"]) & ~filters.edited)
@sudo_users_only
async def get_uptime(_, m: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await m.reply_text(
        "🤖 Shubham Music status 🤖\n\n"
        f"• **uptime:** `{uptime}`\n"
        f"• **start time:** `{START_TIME_ISO}`"
    )
