import glob
import pickle

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

prev = []
with open("completed_videos.pkl", "rb") as f:
    prev = pickle.load(f)
with open("completed_videos.pkl", "wb") as f:
    pickle.dump(list(set(videos + prev)), f)

prev = []
with open("completed_channels.pkl", "rb") as f:
    prev = pickle.load(f)
with open("completed_channels.pkl", "wb") as f:
    pickle.dump(list(set(channels + prev)), f)
