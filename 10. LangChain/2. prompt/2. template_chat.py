from langchain_core.prompts import PromptTemplate
from langchain_core.prompts import ChatPromptTemplate 

template = '당신은 작명가입니다. 다음 상품을 만드는 회사의 이름을 지어주세요. (상품: {product})'
prompt = ChatPromptTemplate.from_messages([
    ('system', '당신은 작명가입니다'),
    ('user', '다음 상품을 만드는 회사의 이름을 지어주세요. (상품: {product})')
])

test_products = [
    '로봇 장난감',
    '가방',
    '신발',
    '영어 교육 플랫폼',
    '전기 자전거'
]

for product in test_products:
    final_prompt = prompt.format_messages(product=product)
    print(f'[{product}]{final_prompt}')