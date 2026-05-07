import requests
import json

import os
from dotenv import load_dotenv

load_dotenv(dotenv_path="./.env")


API_KEY = os.getenv("API_KEY")
Channel_handle = "MrBeast"

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
    

if __name__ == "__main__":
    get_playlist_id()