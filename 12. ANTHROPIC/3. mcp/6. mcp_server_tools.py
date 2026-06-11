import sys

from mcp.server.fastmcp import FastMCP

mcp = FastMCP('my-more-tool-server')

# 원하는 툴 추가
@mcp.tool()
def add(x: int, y: int) -> int:
    '''두 정수 x와 y를 합한 결과값을 반환'''
    return x + y

@mcp.tool()
def multiple(x:int, y: int) -> int:
    '''두 정수 x와 y를 곱한 결과값을 반환'''
    return x * y

@mcp.tool()
def word_count(text: str) -> int:
    '''주어진 문장에서 단어 갯수를 계산하여 이를 반환'''
    return len(text.split())

if __name__ == '__main__':
    mcp.run()