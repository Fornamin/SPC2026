# FastAPI랑 유사
import sys

from mcp.server.fastmcp import FastMCP

mcp = FastMCP('HelloWorld')

@mcp.tool()
def hello(name: str) -> str:
    print(f'[SERVER] Hello Function Called / Name: {name}', file=sys.stderr)
    return f'Hello, {name}'

if __name__ == '__main__':
    print(f'[SERVER] Server Started', file=sys.stderr)
    mcp.run()