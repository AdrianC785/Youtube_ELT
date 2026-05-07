import requests
import json

import os
from dotenv import load_dotenv

load_dotenv(dotenv_path="./.env")


API_KEY = os.getenv("API_KEY")
Channel_handle = "MrBeast"
maxResults = 50

url = f"https://youtube.googleapis.com/youtube/v3/channels?part=contentDetails&forHandle={Channel_handle}&key={API_KEY}"

def get_playlist_id():
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        # print(data["items"][0]["contentDetails"]["relatedPlaylists"]["uploads"])
        return data["items"][0]["contentDetails"]["relatedPlaylists"]["uploads"]
    except requests.RequestException as exc:
        print(f"Request failed: {exc}")
        return None
    except (KeyError, IndexError, ValueError) as exc:
        print(f"Response parsing failed: {exc}")
        return None
    

# baseURL = f'https://youtube.googleapis.com/youtube/v3/playlistItems?part=contentDetails&maxResults={maxResults}&playlistId=UUX6OQ3DkcsbYNE6H8uQQuVA&key={API_KEY}'

# playlist_id = get_playlist_id()

def get_video_ids(playlist_id):

    video_ids =[]

    pageToken = None

    baseURL = f'https://youtube.googleapis.com/youtube/v3/playlistItems?part=contentDetails&maxResults={maxResults}&playlistId={playlist_id}&key={API_KEY}'

    try:
        while True:
            url = baseURL
            if pageToken:
                url += f'&pageToken={pageToken}'
            
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            for item in data.get('items', []):
                video_id = item['contentDetails']['videoId']
                video_ids.append(video_id)

            pageToken = data.get('nextPageToken')

            if not pageToken:
                break
        
        return video_ids
    
    except requests.exceptions.RequestException as e:
        raise e



if __name__ == "__main__":
    playlist_id = get_playlist_id()
    print(get_video_ids(playlist_id))