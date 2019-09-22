"""
Генерация наборов данных по описанной в JSON структуре.
"""

import datetime
import json
import random
import time
import click


def str_to_datetime(string):
    """Преобразование строки в datetime"""
    return datetime.datetime.strptime(string, '%d.%m.%Y %H:%M:%S')


def random_date(start, end):
    """Генерация datetime между `start` и `end`"""
    return start + datetime.timedelta(
        seconds=random.randint(0, int((end - start).total_seconds()))
    )


@click.command()
@click.option(
    '--file-json', '-j',
    help='Путь к файлу с структурой датасета'
)
def main(file_json):
    """
    Генерация наборов данных по описанной в JSON структуре.
    """
    # Время начала выполнения
    start_time = time.time()

    # Загрузка структуры датасета из JSON
    with open(file_json) as f_json:
        dataset = json.load(f_json)

    file_dataset = dataset["variables"]["file_dataset"]
    separator = dataset["variables"]["separator"]
    row_count = dataset["variables"]["row_count"]
    random.seed(dataset["variables"]["random_seed"])

    file = open(file_dataset, 'w')

    col_index = 0  # Индекс поля

    # Заполнение имен полей в датасете
    for key in dataset["columns"].keys():
        # Для последнего поля разделитель не добавляется
        if col_index != len(dataset["columns"].keys()) - 1:
            file.write(str(key) + separator)
        else:
            file.write(str(key))
        col_index += 1
    file.write('\n')

    # Генерация датасета
    for row in range(0, row_count):
        values = []  # Хранимая строка

        for col in dataset["columns"].keys():

            min_value = dataset["columns"][col]["min_value"]
            max_value = dataset["columns"][col]["max_value"]
            type_value = dataset["columns"][col]["type_value"]
            string_name = dataset["columns"][col]["string_name"]
            round_value = dataset["columns"][col]["round_value"]

            # Генерация значений для целого и вещественного типа
            # Для строкового типа добавляется индекс к заданному имени строки
            if type_value == "int":
                values.append(str(random.randint(min_value, max_value)))
            elif type_value == "float":
                if 0 <= round_value <= 12:
                    values.append(str(round(random.uniform(min_value, max_value), round_value)))
                else:
                    values.append(str(random.uniform(min_value, max_value)))
            elif type_value == "str":
                values.append(string_name + str(row + 1))
            elif type_value == "bool":
                int_value = random.randint(0, 1)
                if int_value == 0:
                    bool_value = False
                else:
                    bool_value = True
                values.append(str(bool_value))
            elif type_value == "datetime":
                start = str_to_datetime(min_value)
                end = str_to_datetime(max_value)
                values.append(random_date(start, end).strftime('%d.%m.%Y %H:%M:%S'))

        file.write(separator.join(values))
        if row != row_count - 1:
            file.write('\n')

    file.close()

    # Время генерации датасета
    seconds = time.time() - start_time

    # Вывод времени генерации датасета
    print(f"{row_count} rows, {seconds} seconds")


if __name__ == "__main__":
    main()
