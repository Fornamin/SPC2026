from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

loader = PyPDFLoader('./file/secure_coding_guide.pdf')
pages = loader.load()

splitter = RecursiveCharacterTextSplitter(
    chunk_size = 500,
    chunk_overlap = 100
)
chunks = splitter.split_documents(pages)
print(f'점검 후 문서 개수: {len(chunks)}')

first = chunks[0]
print(first.metadata)
print(first.page_content)
print('-' * 100)

first = chunks[100]
print(first.metadata)
print(first.page_content)
