import json
import requests
import urllib.request
import sys

def youtube_thumb(api_key, channel_name, image_path):
    channel_id = get_channel_id(api_key, channel_name)
    url = latest_video_thumb(api_key, channel_id)
    download_image(url, image_path)

def get_channel_id(api_key, channel_name):
    payload = {'part': 'id,snippet', 'key': api_key,'type':'channel','q':channel_name}
    r = requests.get("https://www.googleapis.com/youtube/v3/search", params=payload)
    cid = parse_channel_id(r.text)
    return cid

def parse_channel_id(json_string):
    parsed = json.loads(json_string)
    result = parsed["items"][0]["id"]["channelId"]
    return result

def latest_video_thumb(api_key, channel_id):
    payload = {'part': 'id,snippet', 'key': api_key,'channelId':channel_id,'maxResults':1,'order':'date'}
    r = requests.get("https://www.googleapis.com/youtube/v3/search", params=payload)
    url = parse_latest_video(r.text)
    return url


def parse_latest_video(json_string):
    parsed = json.loads(json_string)
    result = parsed["items"][0]["snippet"]["thumbnails"]["high"]["url"] # TODO
    return result

def download_image(url, save):
    with urllib.request.urlopen(url) as f:        
        contents = f.read()
    with open(save, 'wb') as g:
        g.write(contents)

if __name__ == "__main__":
    api_key = sys.argv[1]
    channel_name = sys.argv[2]
    save_path = sys.argv[3]
    youtube_thumb(api_key, channel_name, save_path)
