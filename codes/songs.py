

import os
import aiohttp
import asyncio
import json
import sys
import time
from youtubesearchpython import SearchVideos
from pyrogram import filters, Client
from youtube_dl import YoutubeDL
from youtube_dl.utils import (
    ContentTooShortError,
    DownloadError,
    ExtractorError,
    GeoRestrictedError,
    MaxDownloadsReached,
    PostProcessingError,
    UnavailableVideoError,
    XAttrMetadataError,
)

@Client.on_message(filters.command("song") & ~filters.edited)
async def song(client, message):
    cap = "@JEBotZ"
    url = message.text.split(None, 1)[1]
    rkp = await message.reply("काम चल रहा है ...")
    if not url:
        await rkp.edit("**कौनसा गाना आप चाहते है **\nUsage`/song <song name>`")
    search = SearchVideos(url, offset=1, mode="json", max_results=1)
    test = search.result()
    p = json.loads(test)
    q = p.get("search_result")
    try:
        url = q[0]["link"]
    except BaseException:
        return await rkp.edit("ये गाना नही खोजा जा सका @crystalbots")
    type = "audio"
    if type == "audio":
        opts = {
            "format": "bestaudio",
            "addmetadata": True,
            "key": "FFmpegMetadata",
            "writethumbnail": True,
            "prefer_ffmpeg": True,
            "geo_bypass": True,
            "nocheckcertificate": True,
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "320",
                }
            ],
            "outtmpl": "%(id)s.mp3",
            "quiet": True,
            "logtostderr": False,
        }
        song = True
    try:
        await rkp.edit("कार्य किया जा रहा है ...")
        with YoutubeDL(opts) as rip:
            rip_data = rip.extract_info(url)
    except DownloadError as DE:
        await rkp.edit(f"`{str(DE)}`")
        return
    except ContentTooShortError:
        await rkp.edit("`ये गाना बहुत ही कम समय का था`")
        return
    except GeoRestrictedError:
        await rkp.edit(
            "`ये गाना आपके देश में नही मिल सकता @ShubhamMusics`"
        )
        return
    except MaxDownloadsReached:
        await rkp.edit("`ये अधिक बार हो चुका`")
        return
    except PostProcessingError:
        await rkp.edit("`कुछ गलत हुआ @ShubhamMusics`")
        return
    except UnavailableVideoError:
        await rkp.edit("`ये गाना के रूप में मौजूद नहीं है।`")
        return
    except XAttrMetadataError as XAME:
        await rkp.edit(f"`{XAME.code}: {XAME.msg}\n{XAME.reason}`")
        return
    except ExtractorError:
        await rkp.edit("`कुछ गलत हुआ ।`")
        return
    except Exception as e:
        await rkp.edit(f"{str(type(e)): {str(e)}}")
        return
    time.time()
    if song:
        await rkp.edit(" आपको दिया जा रहा है ।...") #ImJanindu
        lol = "./etc/thumb.jpg"
        lel = await message.reply_audio(
                 f"{rip_data['id']}.mp3",
                 duration=int(rip_data["duration"]),
                 title=str(rip_data["title"]),
                 performer=str(rip_data["uploader"]),
                 thumb=lol,
                 caption=cap)  #JEBotZ
        await rkp.delete()
