"""
Задание 3.

Для этой задачи
1) придумайте 2-3 решения (обязательно с различной сложностью)
2) оцените сложность каждого выражения в этих решениях в нотации О-большое
3) оцените итоговую сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

Сама задача:
Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат.

Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
"""

data_company = {'Company01': 138000,
                'Company02': 208000,
                'Company03': 23700,
                'Company04': 12980,
                'Company05': 578003,
                'Company06': 2304547,
                'Company07': 1000350,
                'Company08': 763000,
                'Company09': 990687,
                'Company10': 2498}


def three_max_profit01(data):     # O(n^2)
    profit_list = []      # O(1)
    result = []           # O(1)
    for key in data:                  # O(n)
        profit_list.append(data[key])  # O(1)
    profit_list.sort()                 # O(N lig N)
    max_profit = [profit_list[len(profit_list) - 1],
                  profit_list[len(profit_list) - 2],
                  profit_list[len(profit_list) - 3]]
    for el in max_profit:                        # O(n)
        for key, value in data.items():          # O(n)
            if el == value:                      # O(n)
                result.append([key, value])      # O(1)
    return result                                # O(1)


def three_max_profit02(data):   # O(n log n)
    result = []
    data_sort = sorted(data.items(), key=lambda item: item[1])    # O(n log n) +  O(1)
    result.append(data_sort[-1])    # O(1)
    result.append(data_sort[-2])    # O(1)
    result.append(data_sort[-3])    # O(1)

    return result


if __name__ == "__main__":
    print(three_max_profit01(data_company))
    print(three_max_profit02(data_company))

# функция three_max_profit02 лучше, т.л. O(n log n) < O(n^2). Код для нее короче и не содержит циклов.