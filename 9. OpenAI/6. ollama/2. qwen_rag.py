import faiss
import numpy as np

import requests

from dotenv import load_dotenv
import os

from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

MODEL_NAME = 'qwen2.5:1.5b'

documents = [
    '한국 소프트웨어 저작권 협회는 SPC라는 약자를 가지고 있고 다양한 국내 기업의 SW라이선스와 저작권을 다루는 곳이다.',
    '홍길동은 2000년 01월 01일 강원도 설빙산에서 태어났고 그곳에서 호랑이를 잡아먹으며 성장했다.',
    'Python은 개발 언어 중 쉽다고 유명하지만 그렇게 쉽지만은 않다',
    '김민정은 파인애플을 싫어하고 망고를 좋아한다',
    '지금 이 교실에는 30명 가까이 사람들이 있다'
]

def get_embedding(text):
    res = client.embeddings.create(
        input=text,
        model="text-embedding-ada-002"
    )

    return np.array(res.data[0].embedding)

index = faiss.IndexFlatL2(1536) # OpenAI로 임베딩하면 1536차원
doc_embeddings = np.array([get_embedding(doc) for doc in documents])
index.add(doc_embeddings)

def rag_query(user_query):
    query_embedding = get_embedding(user_query)

    distances, indices = index.search(
        np.array([query_embedding]), 
        k=1
    )
    retrieved_index = indices[0][0]
    retrieved_distance = distances[0][0]
    retrieved_doc = documents[retrieved_index]

    true_distance = np.sqrt(distances[0][0])
    similarity_score = 1 / (1 + true_distance)

    print(f'검색된 문서: {retrieved_doc}')
    print(f'거리(L2 Distance): {retrieved_distance}')
    print(f'코사인 유사도: {similarity_score}')
    print('-' * 100)

    if (similarity_score < 0.6):
        return '적절한 답변을 찾을 수 없습니다'
    
    prompt = f'''
    아래 내용을 보고 한국어로 답변하시오.
    아래 질문과 관련 자료가 연관이 없으면 무시하세요.

    [사용자의 질문]
    {user_query}

    [관련 자료]
    {retrieved_doc}
    '''

    # Qwen
    return ask_qwen(prompt)

def ask_qwen(question):
    res = requests.post(
        'http://localhost:11434/api/generate',
        json={
            'model': MODEL_NAME,
            'prompt': question,
            'stream': False
        })
    data = res.json()
    return data['response']

query = '홍길동에 대해 아는 걸 말해줘'
print(rag_query(query))