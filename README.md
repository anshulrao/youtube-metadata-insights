# YouTube Metadata

## Data

```
In [1]: df  = pd.read_csv("YouTubeDataset_withChannelElapsed.csv")
In [2]: df.columns
Out[2]: 
Index(['totalviews/channelelapsedtime', 'channelId',
       'videoCategoryId', 'channelViewCount', 'likes/subscriber',
       'views/subscribers', 'videoCount', 'subscriberCount', 'videoId',
       'dislikes/views', 'channelelapsedtime', 'comments/subscriber',
       'likes/views', 'channelCommentCount', 'videoViewCount',
       'likes/dislikes', 'comments/views', 'totvideos/videocount',
       'elapsedtime', 'videoLikeCount', 'videoDislikeCount',
       'dislikes/subscriber', 'totviews/totsubs', 'views/elapsedtime',
       'videoPublished', 'VideoCommentCount'],
      dtype='object')

In [3]: df = pd.read_csv("YouTubeAppendedMetadata.csv.gz")
In [4]: df.columns
Out[4]: 
Index(['totalviews/channelelapsedtime', 'channelId',
       'videoCategoryId', 'channelViewCount', 'likes/subscriber',
       'views/subscribers', 'videoCount', 'subscriberCount', 'videoId',
       'dislikes/views', 'channelelapsedtime', 'comments/subscriber',
       'likes/views', 'channelCommentCount', 'videoViewCount',
       'likes/dislikes', 'comments/views', 'totvideos/videocount',
       'elapsedtime', 'videoLikeCount', 'videoDislikeCount',
       'dislikes/subscriber', 'totviews/totsubs', 'views/elapsedtime',
       'videoPublished', 'VideoCommentCount', 'published_dt', 'title',
       'description', 'channel_title', 'category', 'duration', 'definition',
       'caption', 'licensed_content', 'content_rating', 'view_cnt', 'like_cnt',
       'comment_cnt', 'privacy_status', 'made_for_kids',
       'channel_published_dt', 'channel_description'],
      dtype='object')
```


**Extra Columns Appended to Original Data:**

```
'published_dt', 
'title',
'description', 
'channel_title', 
'category', 
'duration', 
'definition',
'caption', 
'licensed_content',
'content_rating',
'view_cnt', 'like_cnt',
'comment_cnt',
'privacy_status',
'made_for_kids',
'channel_published_dt',
'channel_description'
```


## Observations
* Both the videoId and channelId are unique in the dataset (can be key-ed) meaning no 
two videos are from the same channel.

* Not all the videos in the dataset are live as of today, some of them have been removed. 
For example, video id = **--_I8vffnIw** (https://www.youtube.com/watch?v=--_I8vffnIw)

Links
* [Kaggle Dataset](https://www.kaggle.com/datasets/thedevastator/revealing-insights-from-youtube-video-and-channe)


## 
