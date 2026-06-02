import os
from dotenv import load_dotenv
load_dotenv()

from langchain_openai import OpenAIEmbeddings
from langchain_community.document_loaders import TextLoader, PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma

DB_DIR = './file/chroma_db'

embeddings = OpenAIEmbeddings(model='text-embedding-3-small')
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)

FILES = [
    './file/nvme.txt',
    './file/hbm.txt',
    './file/CISC_programBook_2024.pdf'
]

def load_any_docs(path):
    if path.lower().endswith('.pdf'):
        return PyPDFLoader(path).load()
    if path.lower().endswith('.txt'):
        return TextLoader(path, encoding='UTF-8').load()

def build_document():
    chunks = []
    for path in FILES:
        part = splitter.split_documents(load_any_docs(path))
        for c in part:
            c.metadata['source'] = os.path.basename(path)
        chunks += part
    return Chroma.from_documents(chunks, embeddings, collection_name='unified', persist_directory=DB_DIR)

store = Chroma(collection_name='unified', embedding_function=embeddings, persist_directory=DB_DIR)
if store._collection.count() == 0:
    store = build_document()
print(f'Collection\'s Name: unified, Counts of Chunks: {store._collection.count()}')

query = '저렴한 햄버거 세트 추천'
for d in store.similarity_search(query, k=2):
    print(f'\nQuestion: {query}')
    print(f'[{d.metadata.get('source')}] {d.page_content}')
    
query = '저장 장치 인터페이스의 속도는?'
for d in store.similarity_search(query, k=2):
    print(f'\nQuestion: {query}')
    print(f'[{d.metadata.get('source')}] {d.page_content}')

# 특정 메타 데이터만을 기반으로 필터링
results = store.similarity_search(query, k=2, filter={'source': 'hbm.txt'})
for d in results:
    print(f'\n--\n{d.page_content}')