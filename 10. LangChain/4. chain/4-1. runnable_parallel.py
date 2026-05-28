from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel

load_dotenv()

llm = ChatOpenAI(model='gpt-4o-mini')

prompt = ChatPromptTemplate.from_template(
    '''
    다음 질문에 {language}로 답변해주세요.

    질문:
    {question}
    '''
)

# 기본 체인
chain = prompt | llm | StrOutputParser()

# 병렬 실행
parallel_chain = RunnableParallel(
    korean=lambda x: chain.invoke({
        'language': '한국어',
        'question': x['question']
    }),
    
    english=lambda x: chain.invoke({
        'language': 'English',
        'question': x['question']
    }),

    japanese=lambda x: chain.invoke({
        'language': '日本語',
        'question': x['question']
    }),
)

# 실행
result = parallel_chain.invoke({
    'question': 'AI의 장점을 설명해줘'
})

print(result)