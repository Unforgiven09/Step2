from concurrent.futures import ThreadPoolExecutor
import time
import requests
import threading
import os
import asyncio

# urls = [
#     'http://itstep.org',
#     'http://github.com',
#     'http://example.com',
#     'http://stackoverflow.com',
#     'http://python.org',
# ]
#
#
# def fetch_url(url):
#     start = time.time()
#     response = requests.get(url)
#     duration = time.time() - start
#     return f'{url} was downloading for {duration:.2f} sec. status code {response.status_code}'
#
#
# start = time.time()
# # one thread way
# # for url in urls:
# #     print(fetch_url(url))
#
# with ThreadPoolExecutor(max_workers=5) as executor:
#     result = executor.map(fetch_url, urls)
#
# for x in result:
#     print(x)
#
# total_duration = time.time() - start
# print("Total time", total_duration)
#
#
# def monitor_folder(folder):
#     while True:
#         files = os.listdir(folder)
#         print('Files in dir: ', files)
#         time.sleep(5)
#
#
# print('start')
# # monitor_folder('D:\\Python\\Step2\\lessons\\LES25')
# monitor_thread = threading.Thread(target=monitor_folder,
#                                   args=('D:\\Python\\Step2\\lessons\\LES25', ), daemon=True)
# monitor_thread.start()
# input('enter some data \n')
# print('finish')


# async def print1():
#     print(1)
#
#
# async def print2():
#     await asyncio.sleep(5)
#     print(2)
#
#
# async def print3():
#     print(3)
#
#
# async def main():
#     task1 = asyncio.create_task(print1())
#     task2 = asyncio.create_task(print2())
#     task3 = asyncio.create_task(print3())
#
#     await asyncio.gather(task1, task2, task3)
#
#
# asyncio.run(main())

async def some_task(sec):
    await asyncio.sleep(sec)
    print('add task', sec)


async def print1(sec):
    await asyncio.sleep(sec)
    print(sec)
    await some_task(sec)


async def main(n):
    async with asyncio.TaskGroup() as tg:
        for x in range(1, n + 1):
            tg.create_task(print1(x))


start = time.time()
asyncio.run(main(10))
print(time.time() - start)
