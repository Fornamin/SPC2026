from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel

load_dotenv()
parser = StrOutputParser()

# ==================================================
# Models
# ==================================================

llm_x = ChatOpenAI(model="gpt-4o-mini", temperature=0.0)
llm_y = ChatOpenAI(model="gpt-4o-mini", temperature=0.5)
llm_z = ChatOpenAI(model="gpt-4o-mini", temperature=1.0)

# ==================================================
# Translator Prompt
# ==================================================

translate_prompt = ChatPromptTemplate.from_template(
    """
다음 문장을 자연스럽고 정확한 한국어로 번역하세요.

원문:
{original}
"""
)

translate1 = translate_prompt | llm_x | parser
translate2 = translate_prompt | llm_y | parser
translate3 = translate_prompt | llm_z | parser

translator_chain = RunnableParallel(
    candidate1=translate1,
    candidate2=translate2,
    candidate3=translate3,
)

# ==================================================
# Judge Prompt
# ==================================================

judge_prompt = ChatPromptTemplate.from_template(
    """
당신은 전문 번역 심사위원입니다.

원문:
{original}

번역 후보 1:
{candidate1}

번역 후보 2:
{candidate2}

번역 후보 3:
{candidate3}

평가 기준:
1. 의미 보존
2. 자연스러움
3. 문법 정확성
4. 가독성

반드시 아래 형식으로 답변하세요.

winner: 1|2|3
reason: 선택 이유
"""
)

judge = judge_prompt | llm_x | parser

# ==================================================
# Pipeline
# ==================================================

def ensemble_translate(text: str):
    translations = translator_chain.invoke({"original": text})
    judge_result = judge.invoke({"original": text, **translations})

    return {
        "translations": translations,
        "judge": judge_result
    }


# ==================================================
# Run
# ==================================================

result = ensemble_translate(
    """
When I was in the army, my instructors would show up in
my barracks room, and the first thing they would inspect
was our bed. It was a simple task, but every morning we
were required to make our bed to perfection. It seemed a
little ridiculous at the time, but the wisdom of this simple
act has been proven to me many times over. If you make
your bed every morning, you will have accomplished the
first task of the day. It will give you a small sense of pride
and it will encourage you to do another task and another. By
the end of the day, that one task completed will have turned
into many tasks completed. If you can’t do little things right,
you will never do the big things right.
    """
)

print("=== TRANSLATIONS ===")
for k, v in result["translations"].items():
    print(f"\n{k}")
    print(v)

print("\n=== JUDGE ===")
print(result["judge"])