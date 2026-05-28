from dotenv import load_dotenv

from langchain_openai import ChatOpenAI

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import (
    RunnableParallel,
    RunnableLambda,
    RunnablePassthrough,
)

load_dotenv()

llm = ChatOpenAI(model='gpt-4o-mini')

# ---------------------------------------------------
# 번역 프롬프트
# ---------------------------------------------------
translate_prompt = ChatPromptTemplate.from_template(
    '''
    아래 문장을 {language}로 번역해주세요.

    문장:
    {text}
    '''
)

translate_chain = (
    translate_prompt
    | llm
    | StrOutputParser()
)

# ---------------------------------------------------
# 요약 프롬프트
# ---------------------------------------------------
summary_prompt = ChatPromptTemplate.from_template(
    '''
    아래 내용을 한 문장으로 요약해주세요.

    내용:
    {content}
    '''
)

summary_chain = (
    summary_prompt
    | llm
    | StrOutputParser()
)

# ---------------------------------------------------
# 병렬 번역
# ---------------------------------------------------
parallel_translate = RunnableParallel(
    korean=RunnableLambda(
        lambda x: translate_chain.invoke({
            'language': '한국어',
            'text': x['text']
        })
    ),

    english=RunnableLambda(
        lambda x: translate_chain.invoke({
            'language': 'English',
            'text': x['text']
        })
    ),

    japanese=RunnableLambda(
        lambda x: translate_chain.invoke({
            'language': '日本語',
            'text': x['text']
        })
    ),
)

# ---------------------------------------------------
# 전체 파이프라인
# ---------------------------------------------------
pipeline = (
    RunnablePassthrough()

    # 1차: 병렬 번역 결과 추가
    | RunnableLambda(
        lambda x: {
            'original': x['text'],
            'translations': parallel_translate.invoke(x)
        }
    )

    # 2차: 각 번역본 요약
    | RunnableLambda(
        lambda x: {
            **x,

            'summaries': {
                lang: summary_chain.invoke({
                    'content': text
                })
                for lang, text in x['translations'].items()
            }
        }
    )
)

# ---------------------------------------------------
# 실행
# ---------------------------------------------------
result = pipeline.invoke({
    'text': '''
    인공지능은 다양한 산업에서 자동화와 생산성 향상을 이끌고 있으며,
    미래에는 인간과 협력하는 중요한 기술이 될 것이다.
    '''
})

# ---------------------------------------------------
# 출력
# ---------------------------------------------------
from pprint import pprint

pprint(result)