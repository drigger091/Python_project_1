import requests
from googleapiclient.discovery import build
import pandas as pd
import seaborn as sns


#extracting channel details and 

api_key = 'AIzaSyARYKh3fUVOQ2QLoBtGz0TUpaXGSrzvs_o'
channel_id = 'UCVsV-ig8JH6Gj_tb2Rnax9w'

youtube = build("youtube","V3",developerKey= api_key)

#extract the channel details

## funnction to get channel statistics

def get_channel_stats(youtube,channel_id):

    request = youtube.channels().list(
                part ='snippet,contentDetails,statistics',
                id = channel_id)
    try:
        response = request.execute()
    except:
        print("An exception occurred") 

    

    #data = data = dict(channel_name=response['items'][0]['snippet']['title'],
               # Subscribers =response['items'][0]['statistics']['subscriberCount'],
                #Viwes = response['items'][0]['statistics']['viewCount'],
                #Total_videos = response['items'][0]['statistics']['videoCount'])

    #print(response)
    return response


#calling the function

print(get_channel_stats(youtube,channel_id))



