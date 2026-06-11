import asyncio

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def main():
    # 동작 구조: Client 실행 -> Server 실행 -> 응답/Server 종료 -> Client 종료
    server_params = StdioServerParameters(
        command='python', 
        args=['./12. ANTHROPIC/3. mcp/2. mcp_server.py'])
    
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            # 아래 코드를 통해서 서버/클라이언트 간 HandShake
            await session.initialize()

            # 서버에 호출하는 코드
            result = await session.call_tool('hello', {'name': 'John'})
            print(result.content[0].text)

if __name__ == '__main__':
    asyncio.run(main())