"""
Задание 2.

Реализуйте два алгоритма.

Оба должны обеспечивать поиск минимального значения для списка.

Сложность первого алгоритма должна быть O(n^2) - квадратичная.

Сложность второго алгоритма должна быть O(n) - линейная.


Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
-- нельзя использовать встроенные функции min() и sort()
-- каждый из двух алгоритмов нужно оформить в виде отдельной ф-ции
-- проставьте сложности каждого выражения в двух ваших алгоритмах
"""

import random

my_list = []
for i in range(0, 10):
    my_list.append(random.randint(0, 1000))

# O(n)


def search_min_lin(start_list):
    el_min = start_list[0]    #  O(1)
    for el in start_list:     #  O(n)
        if el < el_min:       #  O(n)
            el_min = el       #  const
    return el_min             #  O(1)

# O(n^2)


def search_min_sq(start_list):
    swap = False                                     # O(1)
    for i in range(len(start_list)-1):               # O(n) + O(1)
        for j in range(0, len(start_list)-i-1):      # O(n) + O(1)
            if start_list[j] > start_list[j+1]:      # O(n) + 2 * O(1)
                swap = True                          # O(1)
                swap1 = start_list[j]                # O(1)
                swap2 = start_list[j + 1]            # O(1)
                start_list[j + 1] = swap1            # O(1)
                start_list[j] = swap2                # O(1)
        if not swap:                                 # O(n)
            return start_list[0]                     # O(1)
    return start_list[0]                             # O(1)


if __name__ == "__main__":
    print(my_list)
    print(search_min_lin(my_list))
    print(search_min_sq(my_list))
