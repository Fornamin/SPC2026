from dotenv import load_dotenv

from langchain_core.prompts import (
    PromptTemplate,
    FewShotPromptTemplate
)
from langchain_core.prompts import ChatPromptTemplate 
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI

load_dotenv()

examples = [
    {'sentence': '오늘 정말 최고의 하루였어', 'result': '감정: 긍정 / 점수: 9'},
    {'sentence': '진짜 너무 행복하고 기분 좋다', 'result': '감정: 긍정 / 점수: 10'},
    {'sentence': '그냥 평범한 하루였네', 'result': '감정: 중립 / 점수: 5'},
    {'sentence': '오늘은 좀 우울하고 힘들었어', 'result': '감정: 부정 / 점수: 2'},
    {'sentence': '시험 망해서 너무 속상하다', 'result': '감정: 부정 / 점수: 1'},
    {'sentence': '친구들이랑 맛있는 거 먹어서 좋았어', 'result': '감정: 긍정 / 점수: 8'},
    {'sentence': '피곤하긴 한데 그래도 괜찮아', 'result': '감정: 중립 / 점수: 6'}
]

example_prompt = PromptTemplate(
    input_variables=['sentence', 'result'],
    template='문장: {sentence}\n분석: {result}'
)

fewshot_prompt = FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
    prefix='다음은 문장의 감정을 분석한 예시. 같은 형식으로 다음 문장을 분석.\n=== 예시 ===',
    suffix='=== 새로 분석할 문장 ===\n문장: {sentence}',
    input_variables=['sentence'],
    example_separator = '\n---------------------------------------\n'
)

chat_prompt = ChatPromptTemplate.from_messages([
    ('system', '당신은 한국어 감정 분석가. 예시와 같은 형태로 답변'),
    ('user', '{fewshot_text}')
])

llm = ChatOpenAI(model='gpt-4o-mini')
chain = chat_prompt | llm | StrOutputParser()

target = '오랜만에 만난 친구랑 좋은 시간을 보냈다. 다음에 또 보고싶다.'
fewshot_text = fewshot_prompt.format(sentence=target)
result = chain.invoke({'fewshot_text': fewshot_text})

print(result)

# few-shot을 사용하지 않았다면?
plain_chain = (
    ChatPromptTemplate.from_messages([
        ('system', '당신은 한국어 감정 분석가.'),
        ('user', '다음 문장의 감정을 분석: {sentence}')
    ]) 
    | llm 
    | StrOutputParser()
)

print(plain_chain.invoke({'sentence': target}))

