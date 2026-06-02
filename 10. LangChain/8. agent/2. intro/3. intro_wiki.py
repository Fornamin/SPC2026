from dotenv import load_dotenv
from langchain.tools import tool
from langchain_openai import ChatOpenAI
from langchain.agents import create_agent

import requests

load_dotenv()

@tool
def wikipedia_search(query: str) -> str:
    """Search Wikipedia."""

    headers = {
        "User-Agent": "SPC2026Bot/1.0"
    }

    params = {
        "action": "query",
        "list": "search",
        "srsearch": query,
        "format": "json"
    }

    r = requests.get(
        "https://en.wikipedia.org/w/api.php",
        params=params,
        headers=headers,
        timeout=10
    )

    data = r.json()

    results = []

    for item in data["query"]["search"][:5]:
        results.append(
            f"""
Title: {item['title']}
Snippet: {item['snippet']}
"""
        )

    return "\n".join(results)


llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)

agent = create_agent(
    model=llm,
    tools=[wikipedia_search]
)

response = agent.invoke(
    {
        "messages": [
            {
                "role": "user",
                "content": "Who created Python?"
            }
        ]
    }
)

print(response)