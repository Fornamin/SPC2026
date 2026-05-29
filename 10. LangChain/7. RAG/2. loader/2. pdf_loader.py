# pip install pypdf
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('./file/secure_coding_guide.pdf')
pages = loader.load()

print(f'[PDF] {pages} pages')

for p in pages:
    if p.page_content.strip():
        print(f'- metadata\n{p.metadata}')
        print(f'- content\n{p.page_content[:50]}')
        break