from dotenv import load_dotenv

# pip install langchain-anthropic
from langchain_anthropic import ChatAnthropic

load_dotenv()

llm = ChatAnthropic(model_name='claude-sonnet-4-6')

res = llm.invoke('인공지능에 대해 설명해줘')
print(res.content)