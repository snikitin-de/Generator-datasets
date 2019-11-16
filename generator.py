"""
Набор функций для генерации случайных данных различных форматов
"""

import datetime
import random


def str_to_datetime(string, datetime_format):
    """
    Преобразование строки в datetime

    :param string: строка для преобразования в Дату/время
    :param datetime_format: формат даты в который необходимо преобразовать строку
    :return: возвращается преобразованная в datetime строка
    """
    return datetime.datetime.strptime(string, datetime_format)


def generate_datetime(min_date, max_date, datetime_format):
    """
    Генерация даты между заданными

    :param min_date: минимальная дата генерации
    :param max_date: максимальная дата генерации
    :param datetime_format: формат даты в который необходимо преобразовать строку
    :return: возвращается случайная дата между минимальной
    и максимальной датой генерации в заданном формате
    """
    start = str_to_datetime(min_date, datetime_format)
    end = str_to_datetime(max_date, datetime_format)
    date_time = start + datetime.timedelta(
        seconds=random.randint(0, int((end - start).total_seconds()))
    )

    return date_time


def generate_string(min_length, max_length, characters):
    """
    Генерация строки заданной длины с случайнми символами

    :param min_length: минимальная длина строки
    :param max_length: максимальная длина строки
    :param characters: строка символов для генерации
    :return: возвращается случайно сгенерированная
    строка заданной длины
    """
    # Для строки случайной длины выбирается
    # случайный символ из заданной строки
    return ''.join(
        characters[random.randint(0, len(characters) - 1)]
        for i in range(0, random.randint(min_length, max_length)))


def generate_bool():
    """
    Генерация случайного значения логического типа данных

    :return: возвращается логический тип с значением True или False
    """
    # Случайным образом генерируется 0 или 1,
    # если 0, то возвращается False, иначе True
    if random.randint(0, 1) == 0:
        bool_value = False
    else:
        bool_value = True

    return bool_value


def generate_float(min_value, max_value, round_value):
    """
    Генерация случайного вещественного числа

    :param min_value: минимальное число для генерации
    :param max_value: максимальное число для генерации
    :param round_value: количество знаков после запятой
    :return: возвращается случайное вещественное число
    из заданного диапазона значений
    """

    if 0 <= round_value <= 12:
        float_value = round(random.uniform(min_value, max_value), round_value)
    else:
        float_value = random.uniform(min_value, max_value)

    return float_value


def generate_int(min_value, max_value):
    """
    Генерация случайного целого числа

    :param min_value: минимальное число для генерации
    :param max_value: максимальное число для генерации
    :return: возвращается случайное целое число
    из заданного диапазона значений
    """
    return random.randint(min_value, max_value)
