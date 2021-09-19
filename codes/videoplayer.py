# codes by Zaid vc video player!
# Imported by public demand , if you seems that this is wrong contact us!
# but stop some codes are imported and some are created by us!!

# © @shubham-king 
# if you kang this then give us credit with zaid! 


import os
import asyncio
import subprocess
from pytgcalls import idle
from pytgcalls import PyTgCalls
from pytgcalls import StreamType
from pytgcalls.types.input_stream import AudioParameters
from pytgcalls.types.input_stream import InputAudioStream
from pytgcalls.types.input_stream import InputVideoStream
from pytgcalls.types.input_stream import VideoParameters

from pyrogram import Client, filters
from pyrogram.types import Message
from config import SESSION_NAME, API_ID, API_HASH, BOT_USERNAME
from helpers.decorators import authorized_users_only
from helpers.filters import command
from youtube_dl import YoutubeDL
from youtube_dl.utils import ExtractorError

SIGINT: int = 2

app = Client(SESSION_NAME, API_ID, API_HASH)
call_py = PyTgCalls(app)
FFMPEG_PROCESS = {}

def raw_converter(dl, song, video):
    return subprocess.Popen(
        ['ffmpeg', '-i', dl, '-f', 's16le', '-ac', '1', '-ar', '48000', song, '-y', '-f', 'rawvideo', '-r', '20', '-pix_fmt', 'yuv420p', '-vf', 'scale=854:480', video, '-y'],
        stdin=None,
        stdout=None,
        stderr=None,
        cwd=None,
    )

def youtube(url: str):
    try:
        params = {"format": "best[height=?480]/best", "noplaylist": True}
        yt = YoutubeDL(params)
        info = yt.extract_info(url, download=False)
        return info['url']
    except ExtractorError: 
        return 
    except Exception:
        return


@Client.on_message(command(["splay", f"splay@{BOT_USERNAME}"]) & filters.group & ~filters.edited)
@authorized_users_only
async def startvideo(client, m: Message):
    replied = m.reply_to_message
    if not replied:
        if len(m.command) < 2:
            await m.reply("        video/livestream  URL    stream  ")
        else:
            livelink = m.text.split(None, 1)[1]
            chat_id = m.chat.id
            try:
                livelink = await asyncio.wait_for(
                    app.loop.run_in_executor(
                        None,
                        lambda : youtube(livelink)
                    ),
                    timeout=None 
                )
            except asyncio.TimeoutError:
                await m.reply("         ")
                return
            if not livelink:
                await m.reply("       ")
                return
            process = raw_converter(livelink, f'audio{chat_id}.raw', f'video{chat_id}.raw')
            FFMPEG_PROCESS[chat_id] = process
            msg = await m.reply("**Streaming     ...**")
            await asyncio.sleep(10)
            try:
                audio_file = f'audio{chat_id}.raw'
                video_file = f'video{chat_id}.raw'
                while not os.path.exists(audio_file) or \
                        not os.path.exists(video_file):
                    await asyncio.sleep(2)
                await call_py.join_group_call(
                    chat_id,
                    InputAudioStream(
                        audio_file,
                        AudioParameters(
                            bitrate=48000,
                        ),
                    ),
                    InputVideoStream(
                        video_file,
                        VideoParameters(
                            width=854,
                            height=480,
                            frame_rate=20,
                        ),
                    ),
                    stream_type=StreamType().local_stream,
                )
                await msg.edit("Streaming      \n\n Streaming:- On\n Assistance:- Working\n Join:- @ShubhamMusics.**")
                await idle()
            except Exception as e:
                await msg.edit(f"**error** | `{e}`")
   
    elif replied.video or replied.document:
        msg = await m.reply("   ...")
        video = await client.download_media(m.reply_to_message)
        chat_id = m.chat.id
        await msg.edit("**  ...**")
        os.system(f"ffmpeg -i '{video}' -f s16le -ac 1 -ar 48000 'audio{chat_id}.raw' -y -f rawvideo -r 20 -pix_fmt yuv420p -vf scale=640:360 'video{chat_id}.raw' -y")
        try:
            audio_file = f'audio{chat_id}.raw'
            video_file = f'video{chat_id}.raw'
            while not os.path.exists(audio_file) or \
                    not os.path.exists(video_file):
                await asyncio.sleep(2)
            await call_py.join_group_call(
                chat_id,
                InputAudioStream(
                    audio_file,
                    AudioParameters(
                        bitrate=48000,
                    ),
                ),
                InputVideoStream(
                    video_file,
                    VideoParameters(
                        width=640,
                        height=360,
                        frame_rate=20,
                    ),
                ),
                stream_type=StreamType().local_stream,
            )
            await msg.edit("**Streaming      \n\n Streaming:- On\n Assistance:- Working\n Join:- @ShubhamMusics**")
        except Exception as e:
            await msg.edit(f"**error** | `{e}`")
            await idle()
    else:
        await m.reply("  video   ")


@Client.on_message(command(["sleft", f"sleft@{BOT_USERNAME}"]) & filters.group & ~filters.edited)
@authorized_users_only
async def stopvideo(client, m: Message):
    chat_id = m.chat.id
    try:
        process = FFMPEG_PROCESS.get(chat_id)
        if process:
            try:
                process.send_signal(SIGINT)
                await asyncio.sleep(3)
            except Exception as e:
                print(e)
        await call_py.leave_group_call(chat_id)
        await m.reply("**streaming     !**")
    except Exception as e:
        await m.reply(f"**   ** | `{e}`")
