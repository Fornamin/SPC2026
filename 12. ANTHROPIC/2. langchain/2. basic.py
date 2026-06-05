from dotenv import load_dotenv

# pip install langchain-anthropic
from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate

load_dotenv()

llm = ChatAnthropic(model_name='claude-sonnet-4-6')
template = PromptTemplate.from_template('다음 주제에 대해 설명: {topic}')

formatted_prompt = template.format(topic='기니피그')
res = llm.invoke(formatted_prompt)
print(res.content)

#######################################################################

chat_template = ChatPromptTemplate.from_messages([
    ('system', '당신은 {role} 전문가입니다. 질문에 자세히 답변해주세요'),
    ('human', '다음에 대해 설명해주세요: {concept}')
])

chain = chat_template | llm
res = chain.invoke({'role': '동물', 'concept': '토끼'})
print(res.content)