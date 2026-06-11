import asyncio
import sys

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def main():
    # 동작 구조: Client 실행 -> Server 실행 -> 응답/Server 종료 -> Client 종료
    server_params = StdioServerParameters(
        command='python', 
        args=['./12. ANTHROPIC/3. mcp/debug_proxy.py', './12. ANTHROPIC/3. mcp/4. mcp_server_debug.py'])
    
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            print(f'[CLIENT] Before Handshaking with the Server', file=sys.stderr)
            await session.initialize()
            print(f'[CLIENT] After Handshaking with the Server', file=sys.stderr)

            tools = (await session.list_tools()).tools
            print(f'[CLIENT] Getting tools that Server can use\n{tools}', file=sys.stderr)

            # 서버에 호출하는 코드
            result = await session.call_tool('hello', {'name': 'John'})
            print(result.content[0].text)

if __name__ == '__main__':
    print(f'[CLIENT] Client Started')
    asyncio.run(main())