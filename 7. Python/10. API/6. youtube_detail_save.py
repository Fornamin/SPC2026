import requests
import os

import csv

from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('YOUTUBE_API_KEY')

video_api_url = 'https://www.googleapis.com/youtube/v3/videos'
video_ids = []

# 파일 열어서 csv 읽기
with open('search_result.csv', 'r', encoding='UTF-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        video_ids.append(row['video_id'])

# 최종 결과
table = []
table_header = ['index', 'title', 'like count', 'view count', 'comment count']

res = requests.get(video_api_url, {
    'part': 'snippet,statistics',
    'id': ','.join(video_ids),
    'key': API_KEY
})
data = res.json()
print(data)
 
with open('video_stats.csv', 'w', newline='', encoding='UTF-8') as file:
    writer = csv.writer(file)
    writer.writerow(table_header)

    for item in data['items']:
        video_id = item['id']
        title = item['snippet']['title']
        stats = item['statistics']
        like_count = stats.get('likeCount', 0)
        view_count = stats.get('viewCount', 0)
        comment_count = stats.get('commentCount', 0)

        writer.writerow([video_id, title, like_count, view_count, comment_count])