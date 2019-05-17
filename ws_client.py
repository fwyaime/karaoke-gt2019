import asyncio
import websockets

async def hello():
    async with websockets.connect('ws://localhost:8080') as websocket:
        while True:
            name = await websocket.recv()
            print(name)

asyncio.get_event_loop().run_until_complete(hello())