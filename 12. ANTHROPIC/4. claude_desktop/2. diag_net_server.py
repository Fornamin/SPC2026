import asyncio, platform, socket, sys, logging
from mcp.server.fastmcp import FastMCP

mcp = FastMCP('simple-net-diag-server')

@mcp.tool()
async def ping_host(host:str, count:int=3, timeout_sec: int=3) -> str:
    '''지정한 Host로 ping을 하여 결과 반환
        - count: 1~5
        - timeout_sec: 1~5 (timeout sec per packet)
    '''
    host = (host or '').strip()

    if not host:
        raise ValueError('Enter a host')
    
    if platform.system() == 'Windows':
        cmd = ['ping', '-n', str(count), '-w', str(timeout_sec * 1000), host]
    else:
        cmd = ['ping', '-c', str(count), '-w', str(timeout_sec), host]

    proc = await asyncio.create_subprocess_exec(*cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
    out, err = await proc.communicate()
    text = out or err

    return text.decode('cp949', errors='ignore')

if __name__ == '__main__':
    mcp.run(transport='stdio')