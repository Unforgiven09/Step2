import asyncio


async def receive_messages(reader):
    while True:
        data = await reader.read(100)
        if not data:
            continue
        print(data.decode().strip())


async def client():
    reader, writer = await asyncio.open_connection('127.0.0.1', 8888)
    asyncio.create_task(receive_messages(reader))
    print(f'Client connected! Exit for finish.')
    while True:

        message = input()
        writer.write((message + '\n').encode())
        if message.lower() == 'exit':
            break
    writer.close()
    await writer.wait_closed()


asyncio.run(client())
