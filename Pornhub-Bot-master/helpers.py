from pyrogram.errors.exceptions import MessageNotModified, FloodWait
import asyncio
import threading

def humanbytes(size):
    """Convert Bytes To Bytes So That Human Can Read It"""
    if not size:
        return ""
    power = 2 ** 10
    raised_to_pow = 0
    dict_power_n = {0: "", 1: "Ki", 2: "Mi", 3: "Gi", 4: "Ti"}
    while size > power:
        size /= power
        raised_to_pow += 1
    return str(round(size, 2)) + " " + dict_power_n[raised_to_pow] + "B"


def edit_msg(client, message, to_edit):
    try:
        client.loop.create_task(message.edit(to_edit))
    except MessageNotModified:
        pass
    except FloodWait as e:
        client.loop.create_task(asyncio.sleep(e.x))
    except TypeError:
        pass


def download_progress_hook(d, message, client):
    if d['status'] == 'downloading':
        current = d.get("_downloaded_bytes_str") or humanbytes(int(d.get("downloaded_bytes", 1)))
        total = d.get("_total_bytes_str") or d.get("_total_bytes_estimate_str")
        file_name = d.get("filename")
        eta = d.get('_eta_str', "N/A")
        percent = d.get("_percent_str", "N/A")
        speed = d.get("_speed_str", "N/A")
        to_edit = f"<b><u>Downloading File</b></u> \n<b>File Name :</b> <code>{file_name}</code> \n<b>File Size :</b> <code>{total}</code> \n<b>Speed :</b> <code>{speed}</code> \n<b>ETA :</b> <code>{eta}</code> \n<i>Downloaded {current} out of {total}</i> (__{percent}__)"
        threading.Thread(target=edit_msg, args=(client, message, to_edit)).start()