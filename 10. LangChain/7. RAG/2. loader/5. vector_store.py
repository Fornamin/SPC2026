# pip install chromadb
# pip install langchain-chroma

import os
from dotenv import load_dotenv

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings

from langchain_chroma import Chroma

load_dotenv()
DB_DIR = './file/chroma_db'
COLLECTION_NAME = 'memory'

embeddings = OpenAIEmbeddings(model='text-embedding-3-small')

def build_store():
    docs = TextLoader('./file/hbm.txt', encoding='utf-8').load()
    chunks = RecursiveCharacterTextSplitter(
        chunk_size=500, 
        chunk_overlap=100).split_documents(docs)
    store = Chroma.from_documents(
        chunks, embeddings,
        collection_name=COLLECTION_NAME,
        persist_directory=DB_DIR
    )
    return store

def load_store():
    store = Chroma(
        collection_name=COLLECTION_NAME,
        embedding_function=embeddings,
        persist_directory=DB_DIR
    )
    print(f'Loading DB is success - {store._collection.count()} chunks loaded')
    return store

if os.path.exists(DB_DIR) and os.listdir(DB_DIR):
    store = load_store()
else:
    store = build_store()

results = store.similarity_search('HBM이란 무엇인가요', k=2)
for item in results:
    print(f' -> {item.page_content} . . .')