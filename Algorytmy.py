import random
import time


def function_performance(func):
    times = []
    for i in range(100):
        start = time.perf_counter()
        func(numbers, 1)
        stop = time.perf_counter()
        x = stop - start
        times.append(x)

my_list = [1, 3, 5, 7, 9]


def wyszukiwanie_binarne(list, item):
    # który indeks ma liczba
    low = 0
    high = len(list) - 1

    while low <=high:
        mid = round((low + high) / 2)
        guess = list[mid]

        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1


# wyszukiwanie_binarne(my_list, 3)

numbers = [i for i in range(1, 1000000)]


def binarne_zadanie(list, item):
    max_num = len(list) - 1
    min_num = 0
    n = 0
    while min_num <= max_num:
        n = n + 1
        mid_num = round((min_num + max_num) /2)
        guess = list[mid_num]
        if guess == item:
            return print(f'znaleziona liczba {guess}, prób: {n}')
        elif guess > item:
            # print(f'liczba zgadywana{guess} > {item} ')
            max_num = mid_num - 1
        else:
            min_num = mid_num + 1
            # print(f'liczba zgadywana{guess} < {item} ')



# binarne_zadanie(numbers, 1)

function_performance(binarne_zadanie)