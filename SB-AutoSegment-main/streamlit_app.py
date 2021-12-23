import datetime
import math

import streamlit as st
from flair.data import Sentence
from flair.models import SequenceTagger

import transcript_api


@st.cache(allow_output_mutation=True)
def load_model():
    return SequenceTagger.load("final-model.pt")


@st.cache()
def get_segment(video_id):
    tagger = load_model()
    transcript = transcript_api.get_transcript(video_id)
    transcript = [
        {"text": ts["text"].strip().split()[0], "show_s": ts["show_s"]}
        for ts in transcript
        if ts["text"].strip() != "" and "[" not in ts["text"]
    ]
    concat_sentence = " ".join(x["text"] for x in transcript)
    sentence = Sentence(concat_sentence)
    tagger.predict(sentence)

    # Align transcript word to prediction
    i_ts = 0
    dict_tagger = sentence.to_dict("is_sponsor")
    for entity in dict_tagger["entities"]:
        if concat_sentence[entity["start_pos"] - 1] == " " or i_ts == 0:
            transcript[i_ts]["label"] = entity["labels"][0].value
            transcript[i_ts]["score"] = entity["labels"][0].score
            i_ts += 1

    # Find time of sponsor
    sponsor_time = []
    label_sponsor = False
    for ts in transcript:
        if "SPONSOR" == ts["label"] and ts["score"] > 0.7:
            if label_sponsor:
                sponsor_time[-1][1] = ts["show_s"]
            else:
                sponsor_time.append([ts["show_s"], 0])
            label_sponsor = True
        else:
            label_sponsor = False
    return sponsor_time


def main():
    st.title("SponsorBlock AutoSeg")
    video_id = st.text_input("YouTube Video ID")
    if not video_id:
        return
    sponsor_time = get_segment(video_id)
    print(sponsor_time)
    st.markdown(
        """<style>.videoWrapper {
		position: relative;
		padding-bottom: 56.25%; /* 16:9 */
		padding-top: 25px;
		height: 0;
	}
	.videoWrapper iframe {
		position: absolute;
		top: 0;
		left: 0;
		width: 100%;
		height: 100%;
	}</style>""",
        unsafe_allow_html=True,
    )
    for i, sponsor in enumerate(sponsor_time, 1):
        start_time = math.floor(sponsor[0])
        end_time = math.floor(sponsor[1])
        if end_time == 0:
            continue
        with st.expander(
            f"#{i} Sponsor {datetime.timedelta(seconds=start_time)} to {datetime.timedelta(seconds=end_time)}"
        ):
            st.markdown(
                f'<div class="videoWrapper"><iframe src="https://www.youtube-nocookie.com/embed/{video_id}?start={start_time}&end={end_time}"></iframe></div>',
                unsafe_allow_html=True,
            )


if __name__ == "__main__":
    main()
