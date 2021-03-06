from .progress import humanbytes
from .formats import yaml_format


async def mediadata(e_media):
    d3vil = ""
    if e_media.file.name:
        d3vil += f"π π½π°πΌπ΄ :  {e_media.file.name}<br>"
    if e_media.file.mime_type:
        d3vil += f"π πΌπΈπΌπ΄ πππΎπ΄ :  {e_media.file.mime_type}<br>"
    if e_media.file.size:
        d3vil += f"π ππΈππ΄ :  {humanbytes(e_media.file.size)}<br>"
    if e_media.date:
        d3vil += f"π π³π°ππ΄ :  {yaml_format(e_media.date)}<br>"
    if e_media.file.id:
        d3vil += f"π πΈπ³ :  {e_media.file.id}<br>"
    if e_media.file.ext:
        d3vil += f"π π΄πππ΄π½ππΈπΎπ½ :  '{e_media.file.ext}'<br>"
    if e_media.file.emoji:
        d3vil += f"π π΄πΌπΎπΉπΈ :  {e_media.file.emoji}<br>"
    if e_media.file.title:
        d3vil += f"π£ ππΈππ»π΄ :  {e_media.file.title}<br>"
    if e_media.file.performer:
        d3vil += f"π£ πΏπ΄ππ΅πΈππΌπ΄π :  {e_media.file.performer}<br>"
    if e_media.file.duration:
        d3vil += f"π£ π³πππ°ππΈπΎπ½ :  {e_media.file.duration} seconds<br>"
    if e_media.file.height:
        d3vil += f"π£ π·π΄πΈπΆπ·π :  {e_media.file.height}<br>"
    if e_media.file.width:
        d3vil += f"π£ ππΈπ³ππ· :  {e_media.file.width}<br>"
    if e_media.file.sticker_set:
        d3vil += f"π£ πππΈπ²πΊπ΄π ππ΄π :\
            \n {yaml_format(e_media.file.sticker_set)}<br>"
    try:
        if e_media.media.document.thumbs:
            d3vil += f"π£ ππ·ππΌπ±  :\
                \n {yaml_format(e_media.media.document.thumbs[-1])}<br>"
    except Exception as e:
        LOGS.info(str(e))
    return d3vil


def media_type(message):
    if message and message.photo:
        return "Photo"
    if message and message.audio:
        return "Audio"
    if message and message.voice:
        return "Voice"
    if message and message.video_note:
        return "Round Video"
    if message and message.gif:
        return "Gif"
    if message and message.sticker:
        return "Sticker"
    if message and message.video:
        return "Video"
    if message and message.document:
        return "Document"
    return None
