# Описание структуры конфига dataset.json

## variables

Настройка параметров генерации

* **row_count** — количество строк генерации;
* **file_dataset** — путь к файлу в который запишется сгенерированный набор данных;
* **separator** — разделитель полей;
* **random_seed** — зерно для генерации.

## columns

Описание структуры полей для генерации

* **col1** — имя генерируемого поля;
* **min_value** — минимальное значение для генерации (используется в типах полей `str`, `float`, `int` и `datetime`, в `str` означает максимальную длину генерируемой строки);
* **max_value** — максимальное значение для генерации (используется в типах полей `str`, `float`, `int` и `datetime`, в `str` означает минимальную длину генерируемой строки);
* **type_value** — тип значений строк в поле (`str`, `float`, `int`, `bool`, `datetime`);
* **string_random** — усли `True`, то строка будет случайно сгенерирована, если `False`, то к значению **string** добавится номер строки (используется для строкового типа поля);
* **string** — идентификатор строки к которому добавляется ее номер или набор для генерации случайной строки (зависит от значения **string_random**, используется для строкового типа поля);
* **round_value** — количество знаков после запятой для вещественного типа поля.

## Пример структуры конфига dataset.json

```json
{
    "variables" : {
	    "row_count"   : 1000,
        "file_dataset": "dataset.csv",
        "separator"   : ";",
	    "random_seed" : "12345678"
    },
    "columns" : {
		"col1" : {
			"min_value"     : 5,
			"max_value"     : 10,
			"type_value"    : "str",
			"string_random" : true,
			"string"        : "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz",
			"round_value"   : null
		},
		"col2" : {
			"min_value"     : 10000,
			"max_value"     : 150200,
			"type_value"    : "float",
			"string_random" : null,
			"string"        : null,
			"round_value"   : 2
		},
		"col3" : {
			"min_value"     : 1,
			"max_value"     : 32,
			"type_value"    : "int",
			"string_random" : null,
			"string"        : null,
			"round_value"   : null
		},
		"col4" : {
			"min_value"     : null,
			"max_value"     : null,
			"type_value"    : "bool",
			"string_random" : null,
			"string"        : null,
			"round_value"   : null
		},
		"col5" : {
			"min_value"     : "01.01.2017 00:00:00",
			"max_value"     : "01.01.2019 23:59:59",
			"type_value"    : "datetime",
			"string_random" : null,
			"string"        : null,
			"round_value"   : null
		}
    }
}
```

>**Примечание**
>
>В данном примере приведены поля всех типов, все, что не *null* обязательно к заполнению.
