import requests
import json
import pandas as pd
import glob
from multiprocessing import Pool

api_key = "API-KEY"


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


videos = glob.glob("data/video*.csv.gz")
videos = [video[11:-7] for video in videos]
channels = glob.glob("data/channel*.csv.gz")
channels = [channel[13:-7] for channel in channels]

with open("logs/not_found", "r") as f:
    not_found = f.read()

not_found = not_found.split("\n")
for line in not_found:
    if "video" in line:
        videos.append(line.split()[-1])
    elif "channel" in line:
        channels.append(line.split()[-1])


def main():
    df = pd.read_csv("YouTubeDataset_withChannelElapsed.csv")
    values = [list(x) for x in zip(set(df.videoId.values) - set(videos), set(df.channelId.values) - set(channels))]
    for params_list in get_chunks(values, 10):
        pool = Pool(processes=len(params_list))
        pool.map(get_info, params_list)


if __name__ == '__main__':
    main()
