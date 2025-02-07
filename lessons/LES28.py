import random
import threading
import time
from queue import Queue
import multiprocessing


def print_nums():
    for x in range(6):
        print(f'Num{x}')
        time.sleep(1)


def print_letters():
    for x in "qwerty":
        print(f'Letter {x}')
        time.sleep(1)


# thread1 = threading.Thread(target=print_nums)
# thread2 = threading.Thread(target=print_letters)
#
# thread1.start()
# thread2.start()
#
# print(threading.active_count())
# print(threading.enumerate())
#
# for x in range(20):
#     print('x = ', x)
#     time.sleep(1)
#
# thread1.join()
# thread2.join()
# print('finish')

queue = Queue()
lock = threading.Lock()
event = threading.Event()


def producer():
    for x in range(5):
        with lock:
            queue.put(x)
            print(f'Add ', x)
            time.sleep(1)
    event.set()


def consumer():
    while not event.is_set() or queue.empty():
        item = queue.get()
        print('get ', item)
        time.sleep(1.5)


# producer_thread = threading.Thread(target=producer)
# consumer_thread = threading.Thread(target=consumer)
#
# producer_thread.start()
# consumer_thread.start()
#
# producer_thread.join()
# consumer_thread.join()
# print('finish')


# counter = 0
# main_lock = threading.Lock()
#
#
# def increment(a):
#     global counter
#     # print('a = ', a)
#     for x in range(100):
#         with main_lock:
#             counter += a
#             print(counter)
#
#
# threads = [threading.Thread(target=increment, args=(random.randint(1, 5), )) for _ in range(5)]
#
# for t in threads:
#     t.start()
#
# for t in threads:
#     t.join()
#
# print(counter)


def cpu_task(_):
    count = 0
    for x in range(10**8):
        count += 1


# if __name__ == '__main__':
#     start_time = time.time()
#     with multiprocessing.Pool(processes=4) as pool:
#         pool.map(cpu_task, range(4))
#     print('time = ', time.time() - start_time)

# threads = [threading.Thread(target=cpu_task) for x in range(5)]
# for t in threads:
#     t.start()
#
# for t in threads:
#     t.join()

# print('time = ', time.time() - start_time)
