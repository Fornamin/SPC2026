# 1. 네이버 뉴스를 가져온다
# 2. 구글 검색으로 해당 기업 개요/최근 정보를 조회
# 3. 환율 조회
# 4. 주가를 조회

from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from langchain_core.tools import tool
from langchain_core.messages import AIMessage
from langgraph.checkpoint.memory import MemorySaver

@tool
def get_news(keyword):
    '''검색어를 받아 네이버에서 키워드와 관련된 뉴스를 검색'''
    import os
    import sys
    import urllib.request

    client_id = ''
    client_secret = ''

    encText = urllib.parse.quote(keyword)
    url = "https://openapi.naver.com/v1/search/blog?query=" + encText # JSON 결과
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        return(response_body.decode('utf-8'))
    else:
        return("Error Code:" + rescode)

@tool
def get_company_info(company):
    '''검색받은 회사명을 네이버에 검색해 결과를 조회한다'''
    import os
    import sys
    import urllib.request

    client_id = ''
    client_secret = ''

    encText = urllib.parse.quote(company + '회사 정보')
    url = "https://openapi.naver.com/v1/search/webkr?query=" + encText # JSON 결과
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()

    if(rescode==200):
        response_body = response.read()
        return response_body.decode('utf-8')

@tool
def get_exchange_rate(nation):
    '''
    국가를 입력받아서 1 달러당 해당 국가의 환율을 조회한다
    예시: KRW, USD, JPY
    '''
    # https://open.er-api.com/v6/latest/usd
    import requests
    return requests.get(f'https://open.er-api.com/v6/latest').json()['rates'][nation.upper()]

@tool
def get_stock_price(ticker):
    '''
    yfinance로 다양한 기업의 주가를 가져온다 
    애플('AAPL')과 삼성전자('005930.KS')의 주가 데이터를 가져온다
    '''
    # pip install yfinance
    import yfinance as yf
    data = yf.Ticker(ticker).history(period='1d')
    return data

TOOLS = [
    get_news, get_company_info, get_exchange_rate, get_stock_price
]
