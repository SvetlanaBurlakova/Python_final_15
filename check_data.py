"""
Вы работаете над разработкой программы для проверки корректности даты, введенной пользователем.
На вход будет подаваться дата в формате "день.месяц.год". Ваша задача - создать программу,
которая проверяет, является ли введенная дата корректной или нет.

Ваша программа должна предоставить ответ "True" (дата корректна) или "False" (дата некорректна) в зависимости
от результата проверки.
"""
import argparse

def is_leap_year(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    return False

def check_data(dat: str) -> bool:
    day, month, year = tuple(map(int, dat.split('.')))
    if 1 <= year <= 9999:
        if month in [1, 3, 5, 7, 8, 10, 12] and 1 <= day <= 31:
            return True
        elif month in [4, 6, 9, 11] and 1 <= day <= 30:
            return True
        elif month == 2 and 1 <= day <= 28 and is_leap_year(year) == False:
            return True
        elif month == 2 and 1 <= day <= 29 and is_leap_year(year):
            return True
    else:
        return False
    return False
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Check data')
    parser.add_argument('param', metavar='data', type=str,
                        nargs=1,
                        help='enter date in format DD.MM.YYYY')
    args = parser.parse_args()
    print(check_data(*args.param))

    #date_to_prove = '29.2.2020'
