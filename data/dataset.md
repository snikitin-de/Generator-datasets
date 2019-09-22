# Описание структуры конфига dataset.json

## variables

Настройка параметров генерации

* **row_count** — количество строк генерации;
* **file_dataset** — Путь к файлу в который запишется сгенерированный набор данных;
* **separator** — разделитель полей;
* **random_seed** — зерно для генерации.

## columns

Описание структуры полей для генерации

* **col1** — Максимальное значение для генерации (используется в типах полей float, int и datetime);
* **min_value** — Минимальное значение для генерации (используется в типах полей float, int и datetime);
* **max_value** — имя генерируемого поля;
* **type_value** — тип значений строк в поле (str, float, int, bool, datetime);
* **string_name** — Идентификатор строки к которому добавляется ее номер (используется для строкового типа поля);
* **round_value** — Количество знаков после запятой для вещественного типа поля.

## Пример структуры конфига dataset.json

```json
    {
        "variables" : {
            "row_count"   : 10,
            "file_dataset": "dataset.csv",
            "separator"   : ";",
            "random_seed" : "12345678"
        },
        "columns" : {
            "col1" : {  # Имя поля
                "min_value"   : null,
                "max_value"   : null,
                "type_value"  : "str",
                "string_name" : "Test",
                "round_value" : null
            },
            "col2" : {
                "min_value"   : 10000,
                "max_value"   : 150200,
                "type_value"  : "float",
                "string_name" : null,
                "round_value" : 2
            },
            "col3" : {
                "min_value"   : 1,
                "max_value"   : 32,
                "type_value"  : "int",
                "string_name" : null,
                "round_value" : null
            },
            "col4" : {
                "min_value"   : null,
                "max_value"   : null,
                "type_value"  : "bool",
                "string_name" : null,
                "round_value" : null
            },
            "col5" : {
                "min_value"   : "01.01.2017 00:00:00",
                "max_value"   : "01.01.2019 23:59:59",
                "type_value"  : "datetime",
                "string_name" : null,
                "round_value" : null
            }
        }
    }
```

>**Примечание**
>
>В данном примере приведены поля всех типов, все, что не *null* обязательно к заполнению.