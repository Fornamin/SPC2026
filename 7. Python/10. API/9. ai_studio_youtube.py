import os
import csv
from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv('GEMINI_API_KEY'))
videos = []

with open('video_stats.csv', 'r', encoding='UTF-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        videos.append({
            'title': row['title'],
            'like_count': row['like count'],
            'view_count': row['view count'],
            'comment_count': row['comment count']
        })
prompt = f'''
다음 유튜브 영상({videos}을 분석 ->

1. 가장 인기 있는 영상
2. 인기 있는 이유
3. 어떤 주제가 반응이 좋은 지
4. 내가 유튜브 채널을 운영한다면 어떠한 전략이 좋을 지

작성한 뒤 html로 formatting
'''
res = client.models.generate_content(
    model='gemini-2.5-flash',
    contents=prompt
)

print(res.text)