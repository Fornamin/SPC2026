import requests
import os

import csv

from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('YOUTUBE_API_KEY')

search_url = 'https://www.googleapis.com/youtube/v3/search'
detail_url = 'https://www.googleapis.com/youtube/v3/videos'

search_query = 'Python Tutorial'
res = requests.get(search_url, {
        'part': 'snippet',
        'q': search_query,
        'type': 'video',
        'maxResults': 10,
        'key': API_KEY
    })

search_data = res.json()
search_results = []

table = []
table_header = ['index', 'title', 'view count', 'video url']

if 'items' in search_data:
    # CSV로 저장
    with open('search_result.csv', 'w', newline='', encoding='UTF-8') as file:
        writer = csv.writer(file)
        writer.writerow(['title','video_id', 'video_url', 'description'])

        for item in search_data['items']:
            title = item['snippet']['title']
            video_id = item['id']['videoId']
            video_url = f'https://www.youtube.com/watch?v={video_id}'
            des = item['snippet']['description']
            writer.writerow([title, video_id, video_url, des])

    for item in search_data['items']:
        title = item['snippet']['title']
        video_id = item['id']['videoId']
        video_url = f'https://www.youtube.com/watch?v={video_id}'
        des = item['snippet']['description']

        search_results.extend(search_data['items'])

        print(f'{title:<50}, {video_url:<100}\n{des}')
        print('-' * 100)

    for idx, result in enumerate(search_results, start=1):
        title = result['snippet']['title']
        video_id = item['id']['videoId']
        video_url = f'https://www.youtube.com/watch?v={video_id}'
        view_count = 'N/A'

        video_res = requests.get(
        'https://www.googleapis.com/youtube/v3/videos',
        params={
            'part': 'statistics',
            'id': video_id,
            'key': API_KEY
        })
        video_data = video_res.json()

        view_count = video_data['items'][0]['statistics'].get('viewCount', 'N/A')
        table.append([idx, title, view_count, video_url])
        print(f'{title:<40}, {video_url:<50}, View Count: {view_count}\n{des}')
        print('-' * 100)