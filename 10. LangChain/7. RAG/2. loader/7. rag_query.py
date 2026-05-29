import os
from dotenv import load_dotenv

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_core.runnables import RunnablePassthrough
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from langchain_openai import OpenAIEmbeddings
from langchain_openai import ChatOpenAI

from langchain_chroma import Chroma

load_dotenv()

DB_DIR = './file/chroma_db'
COLLECTION_NAME = 'memory'

# 임베딩 모델
embeddings = OpenAIEmbeddings(
    model='text-embedding-3-small'
)

# Chroma DB 생성
def build_store():
    docs = TextLoader(
        './file/nvme.txt',
        encoding='utf-8'
    ).load()

    chunks = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    ).split_documents(docs)

    store = Chroma.from_documents(
        chunks,
        embeddings,
        collection_name=COLLECTION_NAME,
        persist_directory=DB_DIR
    )
    return store

# 기존 DB 로드
def load_store():
    store = Chroma(
        collection_name=COLLECTION_NAME,
        embedding_function=embeddings,
        persist_directory=DB_DIR
    )

    print(
        f'Loading DB Success - '
        f'{store._collection.count()} chunks loaded'
    )

    return store

# DB 존재 여부 확인
if os.path.exists(DB_DIR) and os.listdir(DB_DIR):
    store = load_store()
else:
    store = build_store()

# Retriever 생성
retriever = store.as_retriever(
    search_kwargs={'k': 3}
)

# 문서 포맷 함수
def format_docs(docs):
    return '\n\n'.join(
        d.page_content for d in docs
    )

# Prompt
prompt = ChatPromptTemplate.from_messages([
    (
        'system',
        '''
당신은 문서 기반 Q&A 시스템입니다.

반드시 제공된 문서만 참고해서 답변하세요.
문서에 없는 내용은 "모르겠습니다"라고 답변하세요.

문서:
{context}
'''
    ),
    (
        'user',
        '{question}'
    )
])

# LLM
llm = ChatOpenAI(
    model='gpt-4o-mini',
    temperature=0
)

# Chain
chain = (
    {
        'context': (
            retriever
            | format_docs
        ),
        'question': RunnablePassthrough()
    }
    | prompt
    | llm
    | StrOutputParser()
)

# 실행
result = chain.invoke(
    'HBM의 성능은 어떤가요?'
)

print(result)