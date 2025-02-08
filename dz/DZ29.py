import asyncio
import random
import aiofiles

# Завдання 1
# Сделано на уроке
#
# Завдання 2
# Напиши програму, яка запускає одночасно три асинхронні функції:
#
# download_file_1() чекає 3 секунди і друкує "File 1 downloaded"
# download_file_2() чекає 2 секунди і друкує "File 2 downloaded"
# download_file_3() чекає 1 секунду і друкує "File 3 downloaded"
# Запусти всі три функції одночасно за допомогою asyncio.gather()


async def download_file_1():
    await asyncio.sleep(3)
    print("Download 1 complete")
    return "File 1 downloaded!"


async def download_file_2():
    await asyncio.sleep(2)
    print("Download 2 complete")
    return "File 2 downloaded!"


async def download_file_3():
    await asyncio.sleep(1)
    print("Download 3 complete")
    return "File 3 downloaded!"


tasks = [download_file_1(), download_file_2(), download_file_3()]


async def main():
    result = await asyncio.gather(*tasks)
    print(*result)


# В данном случае принтом получаем, что загрузка завершена, а ретерном собираем в одну строку состояние, что успешно,
# как лог.
asyncio.run(main())

# Завдання 3
#
# Напиши функцію async_write_file(filename, text), яка асинхронно записує переданий текст у файл.
# Напиши функцію async_read_file(filename), яка асинхронно читає файл і виводить його вміст.
# Використай asyncio.gather(), щоб записати 3 різних файли одночасно, а потім їх прочитати.
#
# Треба використовувати aiofiles для роботи з файлами без блокування головного потоку.
filenames = ['DZ29-1.txt', 'DZ29-2.txt', 'DZ29-3.txt']
texts = ['Text 1', 'Text 2', 'Text 3']


async def async_write_file(filename, text):
    await asyncio.sleep(random.randint(1, 5))
    async with aiofiles.open(filename, 'w') as file:
        await file.write(text)
    print(f'File {filename} updated!')
    return f'Writing data to {filename} complete!'


async def async_read_file(filename):
    if filename:
        async with aiofiles.open(filename, 'r') as file:
            await asyncio.sleep(1)
            data = await file.read()
            print(f'Data from {filename}:', data)
        return f'Reading data from {filename} complete!'
    else:
        await asyncio.sleep(3)
        await async_read_file(filename)


async def main_2():
    gathered_tasks_w = []
    gathered_tasks_r = []
    for x in range(0, 3):
        gathered_tasks_w.append(async_write_file(filenames[x], texts[x]))
    results_w = await asyncio.gather(*gathered_tasks_w)
    print(*results_w)
    for x in range(0, 3):
        gathered_tasks_r.append(async_read_file(filenames[x]))
    results_r = await asyncio.gather(*gathered_tasks_r)
    print(*results_r)


asyncio.run(main_2())
