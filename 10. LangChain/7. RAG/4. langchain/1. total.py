# 표준 LCEL로 RAG 모델 구현

import os
from dotenv import load_dotenv
load_dotenv()

from langchain_openai import OpenAIEmbeddings
from langchain_community.document_loaders import TextLoader, PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

# Vector DB
DB_DIR = './file/chroma_db'
COLLECTION_NAME = 'my-rag'

embeddings = OpenAIEmbeddings(model='text-embedding-3-small')
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
store = Chroma(collection_name='unified', embedding_function=embeddings, persist_directory=DB_DIR)

if store._collection.count() == 0:
    docs = TextLoader('./file/nvme.txt', encoding='UTF-8').load() \
         + TextLoader('./file/hbm.txt', encoding='UTF-8').load() \
         + PyPDFLoader('./file/CISC_programBook_2024.pdf').load() \
         + PyPDFLoader('./file/CISC_programBook_2025.pdf').load()
    
    chunks = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100).split_documents(docs)
    for c in chunks:
        c.metadata['source'] = os.path.basename(c.metadata.get('source', '?'))
    store.add_documents(chunks)
retriever = store.as_retriever(search_kwargs={'k': 3})

# 2. LLM + Prompt
llm = ChatOpenAI(model='gpt-4o-mini', temperature=0)
prompt = ChatPromptTemplate.from_messages([
    ('system', '당신은 문서 기반 Q&A 시스템. 아래 문서만 참고하여 답변.'),
    ('user', '{question}')
])

# 3. Make a pipeline for Q&A
def format_docs(docs):
    return '\n\n'.join(doc.page_content for doc in docs)

chain = (
    RunnablePassthrough.assign(contest=lambda x: format_docs(retriever.invoke(x['question'])))
    | prompt
    | llm
    | StrOutputParser()
)

# 4. Question and Answer
print(chain.invoke({'question': '한국정보보호학회의 주최는?'}))