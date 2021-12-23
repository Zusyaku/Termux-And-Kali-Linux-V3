import json

import requests


def parse_player_info(video_id):
    player_params = {"key": "AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8"}
    data = {
        "videoId": video_id,
        "context": {
            "client": {
                "clientName": "WEB_EMBEDDED_PLAYER",
                "clientVersion": "1.20211019.01.00",
            },
        },
    }
    response = requests.post(
        "https://www.youtube-nocookie.com/youtubei/v1/player",
        params=player_params,
        data=json.dumps(data),
    )
    return response.json()


def get_transcript(video_id):
    sentences = []
    player_info = parse_player_info(video_id)
    if (
        "captions" not in player_info
        or "playerCaptionsTracklistRenderer" not in player_info["captions"]
    ):
        return sentences
    caption_tracks = player_info["captions"]["playerCaptionsTracklistRenderer"][
        "captionTracks"
    ]
    json3_url = None
    for cap in caption_tracks:
        if "kind" in cap and cap["kind"] == "asr" and cap["languageCode"] == "en":
            json3_url = "https://www.youtube.com" + cap["baseUrl"] + "&fmt=json3"
            break
    if json3_url is None:
        return sentences
    r = requests.get(json3_url)
    for event in r.json()["events"]:
        if "segs" not in event:
            continue
        segs = event["segs"]
        start_ms = event["tStartMs"]
        for seg in segs:
            if "tOffsetMs" in seg:
                seg_ms = start_ms + seg["tOffsetMs"]
            else:
                seg_ms = start_ms
            sentences.append({"text": seg["utf8"], "show_s": seg_ms / 1000})
    return sentences


if __name__ == "__main__":
    # API limit test
    import multiprocessing

    video_id = "-wJOUAuKZm8"
    video_ids = [video_id] * 1_000
    pool = multiprocessing.Pool(processes=4)
    results = pool.map(get_transcript, video_ids)
