# YouTube Metadata

## Data

```
In [1]: import pandas as pd

In [2]: df = pd.read_csv("YouTubeDataset_withChannelElapsedAppended.csv.gz")

In [3]: df.head()
Out[3]: 
       videoId                 channelId  totalviews/channelelapsedtime  ...  content_rating  privacy_status  made_for_kids
0  --DwgB78t-c  UCdzU3DSGzyWzN2118yd9X9g                       0.165199  ...              {}          public          False
1  --NZRkXBV7k  UC0UnhAG47DRyVZGVcbhAXhQ                       1.133820  ...              {}          public          False
2  --hoQ2sGG4M  UCXjtAvK5P3wXBGh0vbGylzg                       0.668120  ...              {}          public          False
3  --sBoaqBlzA  UCeKHMeUlcLNPLCLUfZUQI2w                      25.653505  ...             NaN             NaN            NaN
4  R7BGibTDwUU  UCeKHMeUlcLNPLCLUfZUQI2w                      25.889071  ...             NaN             NaN            NaN

[5 rows x 38 columns]

In [4]: df.columns
Out[4]: 
Index(['videoId', 'channelId', 'totalviews/channelelapsedtime',
       'videoCategoryId', 'channelViewCount', 'likes/subscriber',
       'views/subscribers', 'videoCount', 'subscriberCount', 'dislikes/views',
       'channelelapsedtime', 'comments/subscriber', 'likes/views',
       'channelCommentCount', 'videoViewCount', 'likes/dislikes',
       'comments/views', 'totvideos/videocount', 'elapsedtime',
       'videoLikeCount', 'videoDislikeCount', 'dislikes/subscriber',
       'totviews/totsubs', 'views/elapsedtime', 'videoPublishedDate',
       'videoCommentCount', 'channelPublishedDate', 'channelDescription',
       'channelTitle', 'videoTitle', 'videoDescription', 'duration',
       'definition', 'caption', 'licensed_content', 'content_rating',
       'privacy_status', 'made_for_kids'],
      dtype='object')
```

**Original fields:**

```
videoId                                                                --pQCGgGjE8
channelId                                                 UCDUi7yW7tJ7QWJZgK8sRLLQ
totalviews/channelelapsedtime                                            75.169324
videoCategoryId                                                                 20
channelViewCount                                                           6449528
likes/subscriber                                                          0.002532
views/subscribers                                                         0.240101
videoCount                                                                    1010
subscriberCount                                                               4344
dislikes/views                                                                 0.0
channelelapsedtime                                                           85800
comments/subscriber                                                       0.000921
likes/views                                                               0.010547
channelCommentCount                                                           3654
videoViewCount                                                                1043
likes/dislikes                                                                -2.0
comments/views                                                            0.003835
totvideos/videocount                                                   6385.671287
elapsedtime                                                                  75048
videoLikeCount                                                                  11
videoDislikeCount                                                                0
dislikes/subscriber                                                            0.0
totviews/totsubs                                                       1484.697974
views/elapsedtime                                                         0.013898
videoPublishedDate                                        2009-03-14T13:14:06.000Z
videoCommentCount                                                                4
```

**Fields extracted using YouTube API:**

```
channelPublishedDate                                          2007-12-23T16:33:13Z
channelDescription               Literally a place to play games I like just to...
channelTitle                                                             AvielNova
videoTitle                                       Kingdom Hearts- Behemoth (Expert)
videoDescription                 Using Strike Raid to avoid it's attacks is gen...
duration                                                                   PT3M32S
definition                                                                      sd
caption                                                                      False
licensed_content                                                             False
content_rating                                                                  {}
privacy_status                                                              public
made_for_kids                                                                False
```

## Observations
* Not all the videos in the dataset are live as of today, some of them have been removed. 
For example, video id = [--_I8vffnIw](https://www.youtube.com/watch?v=--_I8vffnIw)

* Some description and titles are in languages other than English like Chinese.

## Links
* [Kaggle Dataset](https://www.kaggle.com/datasets/thedevastator/revealing-insights-from-youtube-video-and-channe)
* [Complete Dataset](https://drive.google.com/drive/u/3/folders/1Bd2BMxADMkqq1JFwL5D-52XtAOt25Fdq)
