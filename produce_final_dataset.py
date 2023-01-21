import glob
import pandas as pd

df = pd.read_csv("YouTubeDataset_withChannelElapsed.csv")

tbls = []
for f in glob.glob("channel_data*.csv.gz"):
    try:
        tbls.append(pd.read_csv(f))
    except Exception:
        pass
c = pd.concat(tbls)
c = c.rename(columns={"channel_id": "channelId"})
df = df.merge(c, how="outer", on="channelId")

tbls = []
for f in glob.glob("video_data_*.csv.gz"):
    try:
        tbls.append(pd.read_csv(f))
    except Exception:
        pass
v = pd.concat(tbls)
v = v.rename(columns={"video_id": "videoId"})
df = df.merge(v, how="outer", on="videoId")

duplicate_cols = ['view_cnt', 'like_cnt', 'channel_title_y', 'category', 'comment_cnt', 'published_dt']

df = df.drop(columns=duplicate_cols)

df = df.rename(columns={'VideoCommentCount': 'videoCommentCount',
                        'videoPublished': 'videoPublishedDate',
                        'channel_published_dt': 'channelPublishedDate',
                        'channel_title_x': 'channelTitle',
                        'title': 'videoTitle',
                        'channel_description': 'channelDescription',
                        'description': 'videoDescription',
                        })

df = df.set_index(["videoId", "channelId"])
df = df.drop(columns=["index"])

df.to_csv("YouTubeDataset_withChannelElapsedAppended.csv.gz", compression="gzip")
