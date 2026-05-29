# Retrieval Augmented Generation: 증강 검색 생성
import numpy as np

from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings

load_dotenv()

# OpenAI의 임베딩을 해주는 모델 -> 보편적
embeddings = OpenAIEmbeddings(model='text-embedding-3-small')
text = '고양이가 쇼파 위에서 잔다'
vector = embeddings.embed_query(text) # 위의 문장으로 하나의 점을 찍음
# print(len(vector)) -> 1536차원

sentences = [
    '책상 위에는 컵이 있다',
    '강아지가 침대 위에서 잔다',
    '파이썬은 인기 있는 프로그래밍 언어다',
    'Plastic Tree의 보컬 하세가와 류타로는 1973년 생이다',
    'TMGE의 Drop은 영화 우울한 청춘에 삽입곡으로 쓰였다',
    '오늘 저녁에는 매콤한 떡볶이를 먹을 예정이다',
    '내일 전국적으로 많은 비가 내리겠습니다',
    '지구는 태양계를 공전하는 세 번째 행성이다',
    'NVMe는 SSD의 인터페이스 규격으로 PCIe를 사용한다',
    'SATA SSD는 NVMe보다 속도가 느리다',
    'HDD는 회전 디스크 기반이라 I/O가 느린 편이다'
]
vectors = embeddings.embed_documents(sentences)

def cosine_similarity(a, b):
    a, b = np.array(a), np.array(b)
    return float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b)))

print('=== 문장 간 유사도 (1일 수록 유사함) ===')
for i, a in enumerate(sentences):
    for j, b in enumerate(sentences):
        # if i < j:
            sim = cosine_similarity(vectors[i], vectors[j])
            print(f'{sim:4f} {a} ↔ {b}')