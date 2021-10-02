import os
import asyncio
import re
import subprocess
import ffmpeg
from pytgcalls import GroupCall
from pyrogram import Client, filters
from pyrogram.types import Message
from signal import SIGINT
from youtube_dl import YoutubeDL
from config import API_ID, API_HASH, SESSION_NAME

app = Client(SESSION_NAME, API_ID, API_HASH)
ydl_opts = {
    "geo_bypass": True,
    "geo_bypass_country": "IN",
    "nocheckcertificate": True
    }
ydl = YoutubeDL(ydl_opts)

FFMPEG_PROCESSES = {}
RADIO_CALL = {}


@Client.on_message(filters.command("radio"))
async def stream(client, m: Message):
    if len(m.command) < 2:
        await m.reply_text('`🚫 You forgot to enter a Stream URL`')
        return
     
    query = m.command[1]
    input_filename = f'radio-{m.chat.id}.raw'
    radiostrt = await m.reply_text("`...`")
    
    # Checking and Stopping Already Running Processes in the Current Chat
    process = FFMPEG_PROCESSES.get(m.chat.id)
    if process:
        try:
            process.send_signal(SIGINT)
            await asyncio.sleep(1)
        except Exception as e:
            print(e)

    # To Filter out YT Live and Radio links
    regex = r"^(https?\:\/\/)?(www\.youtube\.com|youtu\.?be)\/.+"
    match = re.match(regex,query)
    if match:
        try:
            meta = ydl.extract_info(query, download=False)
            formats = meta.get('formats', [meta])
            for f in formats:
                ytstreamlink = f['url']
            station_stream_url = ytstreamlink
        except Exception as e:
            await message.reply_text(f'**⚠️ Error** \n{e}')
            print(e)
    else:
        station_stream_url = query
        print(station_stream_url)

    # Extracting audio to RAW FILE
    process = (
        ffmpeg.input(station_stream_url)
        .output(input_filename, format='s16le', acodec='pcm_s16le', ac=2, ar='48k')
        .overwrite_output()
        .run_async()
    )
    FFMPEG_PROCESSES[m.chat.id] = process

    # Starting Radio on Group Call
    chat_id = m.chat.id    
    if chat_id in RADIO_CALL:
        await asyncio.sleep(1)
        await radiostrt.edit(f'📻 Started **[Live Streaming]({query})** in `{chat_id}`', disable_web_page_preview=True)
    else:
        await radiostrt.edit(f'`📻 Radio is Starting...`')
        await asyncio.sleep(3)
        group_call = GroupCall(app, input_filename, path_to_log_file='')
        await group_call.start(chat_id)
        RADIO_CALL[chat_id] = group_call
        await radiostrt.edit(f'📻 Started **[Live Streaming]({query})** in `{chat_id}`', disable_web_page_preview=True)
    
        
@Client.on_message(filters.command("stop"))
async def stopradio(client, m: Message):
    chat_id = m.chat.id
    smsg = await m.reply_text(f'⏱️ Stopping...')
    process = FFMPEG_PROCESSES.get(m.chat.id)
    if process:
        try:
            process.send_signal(SIGINT)
            await asyncio.sleep(3)
        except Exception as e:
            print(e)
    if chat_id in RADIO_CALL:
        await RADIO_CALL[chat_id].stop()
        RADIO_CALL.pop(chat_id)
        await smsg.edit(f'**⏹ Stopped Streaming!**')
    else:
        await smsg.edit(f'`Nothing is Streaming!`')
