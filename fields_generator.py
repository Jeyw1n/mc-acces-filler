import random
from random import choice as rc


def func_dict() -> dict:
    return {
        "user": get_rand_user,
        "address": get_rand_address,
        "phone": get_rand_phone,
        "pasport": get_rand_passport,
        "date": get_rand_date,
        "skip": get_skip,
    }


def get_skip() -> str:
    return '-'


def get_rand_user() -> str:
    """Случайная генерация ФИО"""

    gender = rc(['female', 'male'])

    with open(f'wordlists/{gender}/names.txt', 'r', encoding='utf-8') as f:
        name_list: list = f.read().split('\n')
    with open(f'wordlists/{gender}/second_names.txt', 'r', encoding='utf-8') as f:
        second_name_list: list = f.read().split('\n')
    with open(f'wordlists/{gender}/father_names.txt', 'r', encoding='utf-8') as f:
        father_name_list: list = f.read().split('\n')

    return str(rc(name_list) + ' ' + rc(second_name_list) + ' ' + rc(father_name_list))


def get_rand_address() -> str:
    """Случайный адрес из списка"""

    with open(f'wordlists/address.txt', 'r', encoding='utf-8') as f:
        address_list: list = f.read().split('\n')

    return random.choice(address_list)


def get_rand_phone() -> str:
    """Получаем номер телефона, начинающийся с +7."""

    number = "+7"
    for i in range(11):
        number += str(random.randint(0, 9))
    return number


def get_rand_passport() -> str:
    """Номер паспорта - 0000 000000"""

    passport_data: str = ''
    for i in range(4):
        passport_data += str(random.randint(0, 9))
    passport_data += " "
    for i in range(6):
        passport_data += str(random.randint(0, 9))

    return passport_data


def get_rand_date() -> str:
    """Случайная дата в диапозоне от 2000 до 2030"""

    day = random.randint(1, 31)
    month = random.randint(1, 12)
    year = random.randint(2000, 2030)
    date = f"{day}.{month}.{year}"
    return date
