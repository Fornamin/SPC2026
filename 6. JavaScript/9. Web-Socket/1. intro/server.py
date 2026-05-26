import websockets
import asyncio

# 클라이언트가 요청 시 호출
async def handle_client(websocket):
    print('function called')
    await websocket.send('connected to server')

    try:
        async for msg in websocket:
            print('client msg:', msg)
            await websocket.send(f'server sent msg: {msg}')
    except websockets.exceptions.ConnectionClosed:
        print('client close to connection')

async def main():
    print('main')
    async with websockets.serve(handle_client, 'localhost', 8000):
        print('server opened')
        await asyncio.Future() # 요청이 올 때까지 기다림

asyncio.run(main())