import asyncio

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def main():
    params = StdioServerParameters(
        command='python', 
        args=['./12. ANTHROPIC/3. mcp/6. mcp_server_tools.py'])
    
    async with stdio_client(params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            tools = (await session.list_tools()).tools
            for tool in tools:
                print(tool.name)

            res = (await session.call_tool('add', {'x': 4, 'y': 6}))
            print(res.content[0].text)
            res = (await session.call_tool('multiple', {'x': 4, 'y': 6}))
            print(res.content[0].text)
            res = (await session.call_tool('word_count', {'text': '나 오늘 일찍 일어났어'}))
            print(res.content[0].text)

if __name__ == '__main__':
    asyncio.run(main())