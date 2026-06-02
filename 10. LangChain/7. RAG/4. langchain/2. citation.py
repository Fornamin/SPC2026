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
from langchain_core.runnables import RunnablePassthrough, RunnableLambda

# Vector DB
DB_DIR = './file/chroma_db'
COLLECTION_NAME = 'my-rag'

embeddings = OpenAIEmbeddings(model='text-embedding-3-small')
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
retriever = store.as_retriever(search_kwargs={'k': 10})

# 2. LLM + Prompt
llm = ChatOpenAI(model='gpt-4o-mini', temperature=0.2)
prompt = ChatPromptTemplate.from_messages([
    ('system', '당신은 문서 기반 Q&A 시스템. 아래 문서만 참고하여 답변.'),
    ('user', '{question}')
])

# 3. Make a pipeline for Q&A
def format_docs(docs):
    return '\n\n'.join(f'[(i)] {doc.page_content}' for i, doc in enumerate(docs, start=1))

def extract_sources(docs): # 소스 코드를 unique하게 출력
    seen, sources = set(), []
    for d in docs:
        src = d.metadata.get('source', 'N/A')
        if src not in seen:
            seen.add(src)
            sources.append(src)
    return sources

def retrieve_and_split(inputs):
    docs = retriever.invoke(inputs['question'])
    return { 
        'question': inputs['question'],
        'context': format_docs(docs),
        'sources': extract_sources(docs) }

def append_sources(d):
    src_lines = '\n'.join(f' - {s}' for s in d['sources'])
    return f'{d['answer']}\n\n Ref: \n{src_lines}'

chain = (
    RunnableLambda(retrieve_and_split)
    | RunnablePassthrough.assign(answer=(prompt | llm | StrOutputParser()))
    | RunnableLambda(append_sources))


# 4. Question and Answer
print(chain.invoke({'question': '2024년 한국정보보호학회 하계학술대회의 사전등록 마감일은?'}))