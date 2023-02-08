import glob
import pandas as pd
import datetime

tbls = []
for f in glob.glob("data/channel_*.csv.gz"):
    try:
        tbls.append(pd.read_csv(f))
    except Exception:
        pass
c = pd.concat(tbls)
c = c.rename(columns={"channel_id": "channelId"})

tbls = []
for f in glob.glob("data/video_*.csv.gz"):
    try:
        tbls.append(pd.read_csv(f))
    except Exception:
        pass
v = pd.concat(tbls)
v = v.rename(columns={"video_id": "videoId"})

c.to_csv(f"channel_data_{datetime.datetime.now().strftime('%Y_%m_%d-%I_%M_%S_%p')}.csv.gz", compression="gzip",
         index=False)
v.to_csv(f"video_data_{datetime.datetime.now().strftime('%Y_%m_%d-%I_%M_%S_%p')}.csv.gz", compression="gzip",
         index=False)
