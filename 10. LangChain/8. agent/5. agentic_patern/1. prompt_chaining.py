from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()
llm = ChatOpenAI(model='gpt-4o-mini')
parser = StrOutputParser()

# [1. Research]
# 다음 주제에 대해 핵심 사실 5가지를 간결하게 정리
research_prompt = ChatPromptTemplate.from_template(
    '다음 주제에 대해 핵심 사실 5가지를 간결하게 정리\n'
    '주제: {topic}'
)
research_chain = research_prompt | llm | parser

# [2. Gate Review]
# 다음 리서치 결과가 적합한 지 평가
# - 리서치 결과: {}
# - 평가 기준
#   1. 5가지의 사실이 올바르게 포함되어 있는가?
#   2. 각 사실이 구체적이고 검증 가능한가?
#   3. 주제와 관련이 있는가?
# - PASS 또는 FAIL로만 답하고, PASS일 경우 아무런 설명도 없이 PASS만 출력하시고 FAIL일 경우 실패인 이유를 한 줄로 출력
gate_prompt = ChatPromptTemplate.from_template(
    '다음 리서치 결과가 적합한 지 평가\n'
    '- 리서치 결과: {research}\n'
    '- 평가 기준\n'
    '\t1. 5가지의 사실이 올바르게 포함되어 있는가?\n'
    '\t2. 각 사실이 구체적이고 검증 가능한가?\n'
    '\t3. 주제와 관련이 있는가?\n'
    '- PASS 또는 FAIL로만 답하고, PASS일 경우 아무런 설명도 없이 PASS만 출력하시고 FAIL일 경우 실패인 이유를 한 줄로 출력'
)
gate_chain = gate_prompt | llm | parser

# [3. Conduct an analysis]
# 다음 리서치 결과를 바탕으로 심층 분석 내용을 작성
# - 리서치 결과: {}
# 다음 내용을 포함하시오: 핵심 트렌드 혹은 패턴 / 시사점 / 향후 전망
analysis_prompt = ChatPromptTemplate.from_template(
    '다음 리서치 결과를 바탕으로 심층 분석 내용을 작성\n'
    '\t- 리서치 결과: {research}\n'
    '다음 내용을 포함하시오: 핵심 트렌드 혹은 패턴 / 시사점 / 향후 전망'
)
analysis_chain = analysis_prompt | llm | parser

# [4. Generate an analysis]
# 다음 리서치와 분석된 내용을 바탕으로 간결한 보고서를 작성
# - 타겟: 실무자가 팀장에게 보고
# - 리서치: {}/ 분석: {}
# - 출력형식:
#   1. 제목
#   2. 요약(3줄 이내)
#   3. 핵심 발견 사항
#   4. 결론
report_prompt = ChatPromptTemplate.from_template(
    '다음 리서치와 분석된 내용을 바탕으로 간결한 보고서를 작성'
    '- 타겟: 실무자가 팀장에게 보고'
    '- 리서치: {research}/ 분석: {analysis}'
    '- 출력형식:'
    '\t1. 제목'
    '\t2. 요약(3줄 이내)'
    '\t3. 핵심 발견 사항'
    '\t4. 심층 분석 내용'
    '\t5. 결론 '
)
report_chain = report_prompt | llm | parser

def run_chaining_pipeline(topic):
    # [1. Research]
    research = research_chain.invoke({'topic': topic})

    # [2. Gate Review]
    gate_result = gate_chain.invoke({'research': research})
    if gate_result != 'PASS':
        return gate_result

    # [3. Conduct an analysis]
    analysis = analysis_chain.invoke({'research': research})

    # [4. Generate an analysis]
    report = report_chain.invoke({'research': research, 'analysis': analysis})

    return report

topic = '2025년도의 주요 해킹 사례와 보안 기술 동향' # Question
result = run_chaining_pipeline(topic)
print(result)