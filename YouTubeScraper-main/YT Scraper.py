# -*- coding: utf-8 -*-
#!/bin/env python3
# Telegram Group: http://t.me/cyberclans
# Please give me credits if you use any codes from here.


from apiclient.discovery import build
import pandas as pd

# Put api key with your own.
Api_Key = ""

youtube = build('youtube', 'v3', developerKey=Api_Key)

# Put Any YouTube video ID.
ID = "" 

List = [['Name', 'Comment','Likes', 'time', 'Reply Count']]

def scrape_all_with_replies():
    data = youtube.commentThreads().list(part='snippet', videoId=ID, maxResults='100', textFormat="plainText").execute()

    for i in data["items"]:

        name = i["snippet"]['topLevelComment']["snippet"]["authorDisplayName"]
        comment = i["snippet"]['topLevelComment']["snippet"]["textDisplay"]
        likes = i["snippet"]['topLevelComment']["snippet"]['likeCount']
        published_at = i["snippet"]['topLevelComment']["snippet"]['publishedAt'] 
        replies = i["snippet"]['TotalReplyCount']

        List.append([name, comment, likes, published_at, replies])

        TotalReplyCount = i["snippet"]['TotalReplyCount']

        if TotalReplyCount > 0:

            parent = i["snippet"]['topLevelComment']["id"]

            data2 = youtube.comments().list(part='snippet', maxResults='100', parentId=parent,
                                            textFormat="plainText").execute()

            for i in data2["items"]:
                name = i["snippet"]["authorDisplayName"]
                comment = i["snippet"]["textDisplay"]
                likes = i["snippet"]['likeCount']
                published_at = i["snippet"]['publishedAt']
                replies = ""

                List.append([name, comment, published_at, likes, replies])

    while ("nextPageToken" in data):

        data = youtube.commentThreads().list(part='snippet', videoId=ID, pageToken=data["nextPageToken"],
                                             maxResults='100', textFormat="plainText").execute()

        for i in data["items"]:
            name = i["snippet"]['topLevelComment']["snippet"]["authorDisplayName"]
            comment = i["snippet"]['topLevelComment']["snippet"]["textDisplay"]
            likes = i["snippet"]['topLevelComment']["snippet"]['likeCount']
            published_at = i["snippet"]['topLevelComment']["snippet"]['publishedAt']
            replies = i["snippet"]['TotalReplyCount']

            List.append([name, comment, likes, published_at, replies])

            TotalReplyCount = i["snippet"]['TotalReplyCount']

            if TotalReplyCount > 0:

                parent = i["snippet"]['topLevelComment']["id"]

                data2 = youtube.comments().list(part='snippet', maxResults='100', parentId=parent,
                                                textFormat="plainText").execute()

                for i in data2["items"]:
                    name = i["snippet"]["authorDisplayName"]
                    comment = i["snippet"]["textDisplay"]
                    likes = i["snippet"]['likeCount']
                    published_at = i["snippet"]['publishedAt']
                    replies = ''

                    List.append([name, comment, likes, published_at, replies])

    df = pd.DataFrame({'Name': [i[0] for i in List], 'Comment': [i[1] for i in List], 'Likes': [i[2] for i in List], 'Time': [i[3] for i in List],
                       'Reply Count': [i[4] for i in List]})

    df.to_csv('YT-Scrape-Result.csv', index=False, header=False)

    return "Successful! Check the CSV file that you have just created."


scrape_all_with_replies()
