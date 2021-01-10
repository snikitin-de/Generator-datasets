# Generator datasets

Генерация наборов данных по описанной в JSON структуре.

Доступны 5 типов полей для генерации:

* **str** — строковый;
* **float** — вещественный;
* **int** — целый;
* **datetime** — дата/время;
* **bool** — логический.

## Установка

Для работы программы требуется библиотека `click`.

Установить ее можно либо через PIP командой:

`pip install click`, либо через Anaconda командой `conda install -c anaconda click`.

Также необходимую библиотеку можно установить командой `pip install -r requirements.txt`.

## Использование

Для выполнения программы неоходимо в терминал ввести команду:

`python generator_datasets.py -j data\dataset.json` или ее полный вариант `python generator_datasets.py --file-json data\dataset.json`.

## Описание формата конфигурации датасета

### Блок variables

Настройка параметров генерации

* **row_count** — количество строк генерации;
* **file_dataset** — путь к файлу в который запишется сгенерированный набор данных;
* **separator** — разделитель полей.

### Блок columns

Описание структуры полей для генерации

* **col1** — имя генерируемого поля;
* **min_value** — минимальное значение для генерации (используется в типах полей `str`, `float`, `int` и `datetime`, в `str` означает минимальную длину генерируемой строки);
* **max_value** — максимальное значение для генерации (используется в типах полей `str`, `float`, `int` и `datetime`, в `str` означает максимальную длину генерируемой строки);
* **type_value** — тип значений строк в поле (`str`, `float`, `int`, `bool`, `datetime`);
* **string** — набор символов для генерации случайной строки (используется в типах полей `str`);
* **round_value** — количество знаков после запятой для вещественного типа поля;
* **datetime_format** — задает формат даты для генерации (используется в типах полей `datetime`).

### Пример структуры конфига dataset.json

```json
{
    "variables" : {
	"row_count"   : 1000,
        "file_dataset": "dataset.csv",
        "separator"   : ";"
    },
    "columns" : {
	"col1" : {
	    "min_value"       : 5,
	    "max_value"       : 10,
	    "type_value"      : "str",
	    "string"          : "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz",
	    "round_value"     : null,
	    "datetime_format" : null
	},
	"col2" : {
	    "min_value"       : 10000,
	    "max_value"       : 150200,
	    "type_value"      : "float",
	    "string"          : null,
	    "round_value"     : 2,
	    "datetime_format" : null
	},
	"col3" : {
	    "min_value"       : 1,
	    "max_value"       : 32,
	    "type_value"      : "int",
	    "string"          : null,
	    "round_value"     : null,
	    "datetime_format" : null
	},
	"col4" : {
	    "min_value"       : null,
	    "max_value"       : null,
	    "type_value"      : "bool",
	    "string"          : null,
	    "round_value"     : null,
	    "datetime_format" : null
	},
	"col5" : {
	    "min_value"       : "01.01.2017 00:00:00",
	    "max_value"       : "01.01.2019 23:59:59",
	    "type_value"      : "datetime",
	    "string"          : null,
	    "round_value"     : null,
	    "datetime_format" : "%d.%m.%Y %H:%M:%S"
	}
    }
}
```

>**Примечание**
>
>В данном примере приведены поля всех типов, все, что не *null* обязательно к заполнению.
