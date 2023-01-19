import requests
import json
import pandas as pd
import pickle
from multiprocessing import Pool

api_key = "AIzaSyBOHtJiWW9K3kTj9co0PZQQV23CWgiyYc0"


def get_info(params):
    video_data = []
    channel_data = []
    video_id, channel_id = params[0], params[1]
    try:
        parts = "snippet,contentDetails,statistics,status"
        url = f"https://www.googleapis.com/youtube/v3/videos?part={parts}&id={video_id}&key={api_key}"
        response = requests.get(url)
        if response.status_code == 403:
            print("Requests getting blocked :( Bye!")
            return
        data = json.loads(response.text)
        video_data.append({'video_id': video_id,
                           'published_dt': data["items"][0]["snippet"]["publishedAt"],
                           'title': data["items"][0]["snippet"]["title"],
                           'description': data["items"][0]["snippet"]["description"],
                           'channel_title': data["items"][0]["snippet"]["channelTitle"],
                           'category': data["items"][0]["snippet"]["categoryId"],
                           'duration': data["items"][0]["contentDetails"]["duration"],
                           'definition': data["items"][0]["contentDetails"]["definition"],
                           'caption': data["items"][0]["contentDetails"]["caption"],
                           'licensed_content': data["items"][0]["contentDetails"]["licensedContent"],
                           'content_rating': data["items"][0]["contentDetails"]["contentRating"],
                           'view_cnt': data["items"][0]["statistics"]["viewCount"],
                           'like_cnt': data["items"][0]["statistics"]["likeCount"],
                           'comment_cnt': data["items"][0]["statistics"]["commentCount"],
                           'privacy_status': data["items"][0]["status"]["privacyStatus"],
                           'made_for_kids': data["items"][0]["status"]["madeForKids"]
                           })
        pd.DataFrame(video_data).to_csv(f"data/video_{video_id}.csv.gz", compression="gzip", index=False)
    except Exception:
        print("Error downloading video info: ", video_id)
    try:
        url = f"https://www.googleapis.com/youtube/v3/channels?part=snippet&id={channel_id}&key={api_key}"
        response = requests.get(url)
        data = json.loads(response.text)
        channel_data.append({
            'channel_id': channel_id,
            'channel_published_dt': data["items"][0]["snippet"]["publishedAt"],
            'channel_description': data["items"][0]["snippet"]["description"]
        })
        pd.DataFrame(channel_data).to_csv(f"data/channel_{channel_id}.csv.gz", compression="gzip", index=False)
    except Exception:
        print("Error downloading channel info: ", channel_id)


def get_chunks(seq, size):
    return (seq[pos: pos + size]
            for pos in range(0, len(seq), size))


finished_videos = []
with open("completed_videos.pkl", "rb") as f:
    finished_videos = pickle.load(f)

finished_channels = []
with open("completed_channels.pkl", "rb") as f:
    finished_channels = pickle.load(f)


def main():
    df = pd.read_csv("YouTubeDataset_withChannelElapsed.csv")
    values = [list(x) for x in zip(set(df.videoId.values) - set(finished_videos),
                                   set(df.channelId.values) - set(finished_channels))]
    for params_list in get_chunks(values, 10):
        pool = Pool(processes=len(params_list))
        pool.map(get_info, params_list)


if __name__ == '__main__':
    main()
