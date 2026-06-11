import asyncio

from mcp import ClientSession, StdioServerParameters
from mcp.client.streamable_http import streamable_http_client

URL = 'http://localhost:8000/mcp'

async def main():
    async with streamable_http_client(URL) as (read, write, _):
        async with ClientSession(read, write) as session:
            await session.initialize()

            # Custom Code
            tools = (await session.list_tools()).tools
            print('[TOOLS]', {t.name for t in tools})

if __name__ == '__main__':
    asyncio.run(main())