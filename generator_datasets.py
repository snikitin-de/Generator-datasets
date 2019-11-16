"""
Генерация наборов данных по описанной в JSON структуре
"""
# pylint: disable=no-value-for-parameter
import json
import time
import click
import generator


@click.command()
@click.option(
    '--file-json', '-j',
    help='Путь к файлу с структурой датасета'
)
def main(file_json):
    """
    Генерация наборов данных по описанной в JSON структуре

    :param file_json: путь к файлу JSON
    """
    # Время начала выполнения
    start_time = time.time()

    # Загрузка структуры датасета из JSON
    with open(file_json) as f_json:
        dataset = json.load(f_json)

    file = open(dataset["variables"]["file_dataset"], 'w')

    col_index = 0  # Индекс поля

    # Заполнение имен полей в датасете
    for key in dataset["columns"].keys():
        # Для последнего поля разделитель не добавляется
        if col_index != len(dataset["columns"].keys()) - 1:
            file.write(str(key) + dataset["variables"]["separator"])
        else:
            file.write(str(key))
        col_index += 1
    file.write('\n')

    # Генерация датасета
    for row in range(0, dataset["variables"]["row_count"]):
        values = []  # Хранимая строка

        for col in dataset["columns"].keys():

            min_value = dataset["columns"][col]["min_value"]
            max_value = dataset["columns"][col]["max_value"]
            type_value = dataset["columns"][col]["type_value"]

            value = None

            if type_value == "int":
                value = generator.generate_int(min_value, max_value)
            elif type_value == "float":
                value = generator.generate_float(min_value,
                                                 max_value,
                                                 dataset["columns"][col]["round_value"])
            elif type_value == "str":
                value = generator.generate_string(min_value,
                                                  max_value,
                                                  dataset["columns"][col]["string"])
            elif type_value == "bool":
                value = generator.generate_bool()
            elif type_value == "datetime":
                value = generator.generate_datetime(min_value,
                                                    max_value,
                                                    dataset["columns"][col]["datetime_format"])

            values.append(str(value))

        file.write(dataset["variables"]["separator"].join(values))
        if row != dataset["variables"]["row_count"] - 1:
            file.write('\n')

    file.close()

    # Время генерации датасета
    seconds = time.time() - start_time

    # Вывод времени генерации датасета
    print("{} rows, {} seconds".format(dataset["variables"]["row_count"], seconds))


if __name__ == "__main__":
    main()
