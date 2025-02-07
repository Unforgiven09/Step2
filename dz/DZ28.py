import random
import threading
# Завдання 1
# Користувач вводить з клавіатури значення у список. Після чого запускаються два потоки.
# Перший потік знаходить максимум у списку.
# Другий потік знаходить мінімум у списку. Результати обчислень виведіть на екран.

data_list = []


def fill_data_list():
    value = input('Enter num to fill data list or anything else to quit: ')
    try:
        if int(value):
            data_list.append(int(value))
            fill_data_list()
    except ValueError:
        print('Exit')


def find_max():
    print('Max value =', max(data_list))


def find_min():
    print('Min value =', min(data_list))


# fill_data_list()
#
# thread1 = threading.Thread(target=find_max)
# thread2 = threading.Thread(target=find_min)
#
# thread1.start()
# thread2.start()
#
# thread1.join()
# thread2.join()

# Завдання 2
# Користувач вводить з клавіатури шлях до файлу, що містить набір чисел. Після чого запускаються два потоки.
# Перший потік створює новий файл, в який запише лише парні елементи списку.
# Другий потік створює новий файл, в який запише лише непарні елементи списку.
# Кількість парних і непарних елементів виводиться на екран.

def find_even(data):
    count_even = 0
    for x in data:
        try:
            if int(x) % 2 == 0:
                count_even += 1
        except ValueError:
            continue
    print(count_even)


def find_odd(data):
    count_odd = 0
    for x in data:
        try:
            if int(x) % 2 != 0:
                count_odd += 1
        except ValueError:
            continue
    print(count_odd)


def open_file():
    file_name = input('Enter file name (DZ28-2.txt):')
    with open(file_name) as file:
        data = file.readlines()

        thread3 = threading.Thread(target=find_even(data))
        thread4 = threading.Thread(target=find_odd(data))

        thread3.start()
        thread4.start()

        thread3.join()
        thread4.join()


# open_file()

# Завдання 3
# Користувач вводить з клавіатури шлях до файлу та слово для пошуку. Після чого запускається потік для пошуку
# цього слова у файлі. Результат пошуку виведіть на екран.

def find_word(data, word):
    flag = False
    for x in data:
        if word in x:
            flag = True
            print(f'Word {word} is in file!')
    if not flag:
        print(f'Word {word} is not in file!')


def open_file2():
    file_name = input('Enter file name (DZ28-2.txt):')
    word_to_find = input('Enter word to find (apple):')
    with open(file_name) as file:
        data = file.readlines()
        thread5 = threading.Thread(target=find_word(data, word_to_find))
        thread5.start()
        thread5.join()


# open_file2()

# Завдання 4
# При старті додатку запускаються три потоки. Перший потік заповнює список випадковими числами.
# Два інші потоки очікують на заповнення. Коли перелік заповнений, обидва потоки запускаються.
# Перший потік знаходить суму елементів списку, другий потік знаходить середнє арифметичне значення у списку.
# Отриманий список, сума та середнє арифметичне виводяться на екран.

random_nums = []


def fill_random_nums():
    for x in range(random.randint(100, 200)):
        random_nums.append(random.randint(1, 1000))
    print('Filling list completed! ')
    print(random_nums)


def find_sum():
    print("sum =", sum(random_nums))


def find_avg():
    print("avg =", sum(random_nums) / len(random_nums))


thread6 = threading.Thread(target=fill_random_nums)
thread7 = threading.Thread(target=find_sum)
thread8 = threading.Thread(target=find_avg)

thread6.start()
thread6.join()


thread7.start()
thread8.start()

thread7.join()
thread8.join()
print('Happy End!')
