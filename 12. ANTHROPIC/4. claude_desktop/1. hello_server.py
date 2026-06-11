from mcp.server.fastmcp import FastMCP
mcp = FastMCP('hello')

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

if __name__ == '__main__':
    mcp.run()