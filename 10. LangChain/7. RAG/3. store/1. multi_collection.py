import os
from dotenv import load_dotenv
load_dotenv()

from langchain_openai import OpenAIEmbeddings
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma

DB_DIR = './file/chroma_db'

embeddings = OpenAIEmbeddings(model='text-embedding-3-small')
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)

def build_document(file_path, collection):
    store = Chroma(collection_name=collection, embedding_function=embeddings, persist_directory=DB_DIR)
    if store._collection.count() > 0:
        return store
    
    docs = TextLoader(file_path, encoding='utf-8').load()
    chunks = splitter.split_documents(docs)

    for c in chunks:
        c.metadata['source'] = os.path.basename(file_path)

    return Chroma.from_documents(chunks, embeddings, collection_name=collection, persist_directory=DB_DIR)

# 1. Collection prepared
collections = {
    'nvme': build_document('./file/nvme.txt', 'nvme'),
    'hbm': build_document('./file/hbm.txt', 'hbm')
}

for name, store in collections.items():
    print(f'Collection: {name}, Counts of Chunk: {store._collection.count()}')

# 2. Search in Collection
def search_in(name, query, k = 2):
    return collections[name].similarity_search(query, k=k)

def search_all(query, k_per = 2):
    results = []
    for name, store in collections.items():
        for doc in store.similarity_search(query, k=k_per):
            doc.metadata['collection'] = name
            results.append(doc)
    return results

query = 'PCIe 인터페이스의 속도는?'
print('\n=== NVMe Collection ===')
for d in search_in('nvme', query):
    print(f'-> {d.page_content[:50]}...')


print('\n=== NVMe & HBM Collection ===')
for d in search_all(query):
    print(f'-> [{d.metadata['collection']}] {d.page_content[:50]}...')