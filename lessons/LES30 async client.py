import asyncio


async def receive_messages(reader):
    while True:
        try:
            data = await reader.readline()
            if not data:
                break
            print(data.decode().strip())
        except:
            break


async def client():
    reader, writer = await asyncio.open_connection('127.0.0.1', 12345)

    print(f'Client connected! Exit for finish.')
    while True:
        asyncio.create_task(receive_messages(reader))
        message = input()
        writer.write((message + '\n').encode())
        if message.lower() == 'exit':
            break
    writer.close()
    await writer.wait_closed()


asyncio.run(client())
