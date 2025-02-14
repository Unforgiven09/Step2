# Реалізуйте клієнт-серверний додаток, який дозволяє користувачам спілкуватися в одному чаті. Кожен користувач входить
# у чат під своїм логіном та паролем. Повідомлення, надіслане в чат, видно всім користувачам чату.

import asyncio

users = {'admin': "admin", "guest": "", }


async def user_authorization():
    pass


async def handle_client(reader, writer):
    addr = writer.get_extra_info('peername')
    print(f"Новое подключение от {addr}")

    # Отправляем сообщение пользователю
    message = "Добро пожаловать на сервер!\n"
    writer.write(message.encode())
    await writer.drain()  # Убеждаемся, что данные отправлены

    # Читаем данные от клиента (если нужно)
    while True:
        data = await reader.read(100)
        print(data.decode())
        if not data:
            continue
        # writer.write(data.encode())
        # print(f"Получено от {addr}: {data.decode()}")

    print(f"Закрываем соединение с {addr}")
    writer.close()
    await writer.wait_closed()


async def main():
    server = await asyncio.start_server(handle_client, '127.0.0.1', 8888)

    addr = server.sockets[0].getsockname()
    print(f"Сервер запущен на {addr}")

    async with server:
        await server.serve_forever()

asyncio.run(main())

