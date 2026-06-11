from mcp.server.fastmcp import FastMCP

mcp = FastMCP('my-http-mcp-server')

@mcp.tool()
def hello(name: str) -> str:
    '''
    사용자에게 인삿말을 생성하는 도구

    매개 변수
     - name(str): 인사할 대상의 이름

    반환값
        - str: 'Hello, {name}!'
    '''
    return f'Hello, {name}!'

@mcp.tool()
def add(x: int, y: int) -> int:
    '''두 정수로 덧셈을 수행'''
    return x + y

@mcp.tool()
def now():
    from datetime import datetime
    return datetime.now().strftime('지금 시간은 %Y-%m-%d %H:%M:%S입니다.')

if __name__ == '__main__':
    mcp.run(transport='streamable-http')