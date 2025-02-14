import asyncio

clients = set()


async def handle_client(reader, writer):
    addr = writer.get_extra_info('peername')
    print(f'Client {addr} connected!')
    clients.add(writer)

    while True:
        try:
            data = await reader.read(1024)
            message = data.decode().strip()
            if not message or message.lower() == "exit":
                break
            print(f'{addr}: {message}')
            for client in clients:
                if client != writer:
                    client.write(f'{addr}: {message}\n'.encode())
                    await client.drain()
        except:
            break
    print(f'Client {addr} disconnecter')
    clients.remove(writer)
    writer.close()
    await writer.wait_closed()


async def main():
    server = await asyncio.start_server(handle_client, '127.0.0.1', 12345)
    print("Server start working at '127.0.0.1', 12345")
    async with server:
        await server.serve_forever()


asyncio.run(main())
