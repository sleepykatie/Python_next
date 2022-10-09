"""
Задание 4.

Для этой задачи:
1) придумайте 2-3 решения (обязательно с различной сложностью)
2) оцените сложность каждого выражения в этих решениях в нотации О-большое
3) оцените итоговую сложность каждого решения в нотации О-большое
4) сделайте вывод, какое решение эффективнее и почему

Сама задача:
Пользователи веб-ресурса проходят аутентификацию.
В системе хранятся логин, пароль и отметка об активации учетной записи.

Нужно реализовать проверку, может ли пользователь быть допущен к ресурсу.
При этом его учетка должна быть активирована.
А если нет, то польз-лю нужно предложить ее пройти.

Приложение должно давать ответы на эти вопросы
 и быть реализовано в виде функции.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, применить словарь.

Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
"""

user_data_l = [{'login': 'login01', 'password': 'xxxx', 'act': True},
             {'login': 'login02', 'password': 'xxxxxx', 'act': True},
            {'login': 'login03', 'password': 'xxx', 'act': False}]

user_data_d = {'alex': ['xxxxx', True],
                'mary': ['xxx', False],
                'john': ['xxxxxx', True],
               'smith': ['xxxxx', False]}


def check01(login, pswd):         # O(n)
    for user in user_data_l:      # O(n)
        if user['login'] == login and user['act'] == True:    # O(n) + O(1)
            if user['password'] == pswd:          # O(n)
                return 'Great success'            # O(1)
            return 'Wrong password!'              # O(1)
        elif user['login'] == login and user['act'] == False:  # O(n)
            return 'Please, activate your login'               # O(1)
    return 'Login error'     # O(1)


def check03(login, pswd):
    for user in user_data_l:



def check02(login, pswd):                         # O(n)
    if login in user_data_d:                      # O(n)
        value = user_data_d[login]                # O(1)
        if value[1]:                              # O(n)
            if value[0] == pswd:          # O(n)
                return 'Great success'            # O(1)
            return 'Wrong password!'              # O(1)
        return 'Please, activate your login'      # O(1)
    return 'Login error'  # O(1)


if __name__ == "__main__":
    print(check01('login02', 'xxxxxx'))
    print(check01('login03', 'xxx'))
    print(check02('mary', 'xxx'))
    print(check02('john', 'xxxxxx'))