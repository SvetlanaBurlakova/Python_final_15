"""
У вас есть банковская карта с начальным балансом равным 0 у.е. Вы хотите управлять этой картой,
выполняя следующие операции, для выполнения которых необходимо написать следующие функции:

check_multiplicity(amount): Проверка кратности суммы при пополнении и снятии.
deposit(amount): Пополнение счёта.
withdraw(amount): Снятие денег.
exit(): Завершение работы и вывод итоговой информации о состоянии счета и проведенных операциях.

Пополнение счета:
Функция deposit(amount) позволяет клиенту пополнять свой счет на определенную сумму.
Пополнение счета возможно только на сумму, которая кратна MULTIPLICITY.

Снятие средств:
Функция withdraw(amount) позволяет клиенту снимать средства со счета.
Сумма снятия также должна быть кратной MULTIPLICITY.
При снятии средств начисляется комиссия в процентах от снимаемой суммы,
которая может варьироваться от MIN_REMOVAL до MAX_REMOVAL.

Завершение работы:
Функция exit() завершает работу с банковским счетом. Перед завершением, если на счету больше RICHNESS_SUM,
начисляется налог на богатство в размере RICHNESS_PERCENT процентов.

Проверка кратности суммы:
Функция check_multiplicity(amount) проверяет, кратна ли сумма amount заданному множителю MULTIPLICITY.
Реализуйте программу для управления банковским счетом, используя библиотеку decimal для точных вычислений.
"""
import decimal
from functools import wraps
import logging
from logging.handlers import RotatingFileHandler
import argparse


MULTIPLICITY = 50
PERCENT_REMOVAL = decimal.Decimal(15) / decimal.Decimal(1000)
MIN_REMOVAL = decimal.Decimal(30)
MAX_REMOVAL = decimal.Decimal(600)
PERCENT_DEPOSIT = decimal.Decimal(3) / decimal.Decimal(100)
COUNTER4PERCENTAGES = 3
RICHNESS_PERCENT = decimal.Decimal(10) / decimal.Decimal(100)
RICHNESS_SUM = decimal.Decimal(10_000_000)

ERROR_LOG_FILE_NAME = 'errors.log'
INFO_LOG_FILE_NAME = 'info.log'
FORMAT = '%(levelname)s: %(asctime)s: %(message)s:'
logging.basicConfig(level=logging.DEBUG, format=FORMAT)
logger = logging.getLogger(__name__)

handler_error = RotatingFileHandler(ERROR_LOG_FILE_NAME, encoding='utf-8', maxBytes=10000, backupCount=3)
handler_error.setFormatter(logging.Formatter(FORMAT))
handler_error.setLevel(logging.WARNING)
logger.addHandler(handler_error)

handler_info = RotatingFileHandler(INFO_LOG_FILE_NAME, encoding='utf-8', maxBytes=10000, backupCount=3)
handler_info.setFormatter(logging.Formatter(FORMAT))
handler_info.setLevel(logging.INFO)
logger.addHandler(handler_info)




def logging_decorator(func):
    @wraps(func)
    def inner(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
        except Exception as e:
            logger.critical(f'Результатом выполнения операции {func.__name__} с атрибутами {args} = {e}')
            raise e
        else:
            logger.info(f'Результатом выполнения функции {func.__name__} с атрибутами {args} = {operations[-1]}')
        return result

    return inner

def check_multiplicity(amount):
    if amount % MULTIPLICITY == 0:
        return True
    return False

@logging_decorator
def deposit(amount):
    global bank_account
    global operations
    try:
        if check_multiplicity(amount):
            bank_account += decimal.Decimal(amount)
            operations.append(f'Пополнение карты на {amount} у.е. Итого {bank_account} у.е.')
        else:
            operations.append(f'Сумма должна быть кратной {MULTIPLICITY} у.е.')
    except:
        raise TypeError('Недопустимое значение для снятия')

@logging_decorator
def withdraw(amount):
    global bank_account
    global operations
    try:
        if check_multiplicity(amount):
            percent1 = amount * PERCENT_REMOVAL
            if percent1 < MIN_REMOVAL:
                percent1 = MIN_REMOVAL
            elif percent1 > MAX_REMOVAL:
                percent1 = MAX_REMOVAL
            withdraw_sum1 = amount + percent1
            if bank_account >= withdraw_sum1:
                bank_account -= withdraw_sum1
                operations.append(f'Снятие с карты {amount} у.е. Процент за снятие {int(percent1)} у.е.. Итого {int(bank_account)} у.е.')
            else:
                operations.append(f'Недостаточно средств. Сумма с комиссией {withdraw_sum1} у.е. На карте {bank_account} у.е.')
        else:
            operations.append(f'Сумма должна быть кратной {MULTIPLICITY} у.е.')
    except:
        raise TypeError('Недопустимое значение для снятия')

@logging_decorator
def exit():
    global bank_account
    if bank_account > RICHNESS_SUM:
        nalog = bank_account * RICHNESS_PERCENT
        bank_account -= nalog
        operations.append(f'Вычтен налог на богатство {RICHNESS_PERCENT}% в сумме {nalog} у.е. Итого {bank_account} у.е.')
    operations.append(f'Возьмите карту на которой {bank_account} у.е.')

def parser_date():
    parser = argparse.ArgumentParser(description='My first argument parser')
    parser.add_argument('inp', type=str, nargs='*')
    return parser.parse_args()

if __name__ == '__main__':
    bank_account = decimal.Decimal(0)
    count = 0
    operations = []
    #deposit('1000')
    deposit(1000)
    withdraw(125)
    withdraw(200)
    exit()





