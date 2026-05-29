from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter, RecursiveCharacterTextSplitter

loader = TextLoader('./file/hbm.txt', encoding='utf-8')
documents = loader.load()

contents = documents[0].page_content
print(f'원본 글자수: {len(contents)}')

# 일반적으로 1000:200 / 1500:300 / 2000:500
char_splitter = CharacterTextSplitter(
    separator = '\n\n', 
    chunk_size = 500, # 위를 기준으로 자르는데 이 사이즈가 작으면 최대 500개가 될 때까지 합침
    chunk_overlap = 100, # 문장이 중간에 잘리면 의미가 사라지니 겹치게 자름
)

chunk_char = char_splitter.split_documents(documents)
print(f'[Char Splitter] {len(chunk_char)}')
print(f'Number of First Chunk: {len(chunk_char[0].page_content)}')

recursive_splitter = RecursiveCharacterTextSplitter(
    chunk_size = 500,
    chunk_overlap = 100
)

chunks_recur = recursive_splitter.split_documents(documents)
print(f'[Recursive Splitter] {len(chunk_char)}')
print(f'Number of First Chunk: {len(chunk_char[0].page_content)}')