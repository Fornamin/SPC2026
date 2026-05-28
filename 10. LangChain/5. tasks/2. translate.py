from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableBranch, RunnableLambda

load_dotenv()

llm = ChatOpenAI(model='gpt-4o-mini', temperature=0.3, max_tokens=1000)

def detect_language(x):
    text = x["text"]
    if any("가" <= c <= "힣" for c in text):
        return "ko"
    if any("\u3040" <= c <= "\u30ff" for c in text):
        return "ja"
    if any("\u4e00" <= c <= "\u9fff" for c in text):
        return "zh"
    return "en"

translate_prompt_ko = ChatPromptTemplate.from_template("다음 문장을 한국어로 번역해줘:\n\n{text}")
translate_prompt_en = ChatPromptTemplate.from_template("Translate the following sentence into English:\n\n{text}")
translate_prompt_ja = ChatPromptTemplate.from_template("次の文を日本語に翻訳してください:\n\n{text}")
translate_prompt_zh = ChatPromptTemplate.from_template("将以下句子翻译成中文：\n\n{text}")

translate_chain_ko = translate_prompt_ko | llm | StrOutputParser()
translate_chain_en = translate_prompt_en | llm | StrOutputParser()
translate_chain_ja = translate_prompt_ja | llm | StrOutputParser()
translate_chain_zh = translate_prompt_zh | llm | StrOutputParser()

def add_language(x):
    return {"text": x["text"], "lang": detect_language(x)}

branch = RunnableBranch(
    (lambda x: x["lang"] == "en", RunnableLambda(lambda x: translate_chain_ko.invoke(x))),
    (lambda x: x["lang"] == "ko", RunnableLambda(lambda x: x["text"])),  # 한국어면 그대로
    (lambda x: x["lang"] == "ja", RunnableLambda(lambda x: translate_chain_ko.invoke(x))),
    (lambda x: x["lang"] == "zh", RunnableLambda(lambda x: translate_chain_ko.invoke(x))),
    RunnableLambda(lambda x: x["text"])  # fallback
)

chain = RunnableLambda(add_language) | branch

# 테스트
tests = [
    {"text": "Schedule a meeting for next week about product strategy."},  
    {"text": "다음 주 제품 전략 회의를 잡아줘."},                          
    {"text": "来週の製品戦略会議をスケジュールしてください。"},            
    {"text": "请安排下周的产品战略会议。"},                                
]

for test in tests:
    result = chain.invoke(test)
    print(f"입력: {test['text']}")
    print(f"결과: {result}\n")