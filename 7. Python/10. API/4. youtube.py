import requests
import os

from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('YOUTUBE_API_KEY')
url = 'https://www.googleapis.com/youtube/v3/search'
search_query = 'Python Tutorial'

params = {
    'part': 'snippet',
    'q': search_query,
    'type': 'video',
    'maxResults': 50,
    'key': API_KEY
}

res = requests.get(url, params)
data = res.json()

if 'items' in data:
    for item in data['snippet']['items']:
        print(item)
        title = item['snippet']['title']
        video_id = item['id']['videoId']
        video_url = f'https://www.youtube.com/watch?v={video_id}'
        des = item['snippet']['description']

        print(f'{title:<50}, {video_url:<100}\n{des}')
        print('-' * 100)