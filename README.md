# HW_OOP_Andrianov_M
# Проект домашней работы "введение в Object Oriented Programming"



## Запуск проекта
Запустите следующую команду в терминале, находясь в корневой дирректории проекта, чтобы увидеть результат работы всех функций:
```
python .\__main__.py
```

### Требование для запуска:
- python - v3.13


## Пакет src:
Модуль "classes.py" имеет 2 класса:

- Product
Принимает 4 обязательных свойства и возвращает данные с помощью 4х методов:
    name - возвращает название категори
    description - возвращает описание товара
    price - возвращает цену товара
    quantity - возвращает колличество товара

- Category
Принимает 3 обязательных свойства и возвращает данные с помощью 3х методов
    ame - возвращает название категории
    description - возвращает описание товара
    products - возвращает список товаров
Имеет 2 атрибута:
    category_count - вернёт колличество категорий
    product_count - вернёт колличество товаров


## Тестирование 
Для запуска тестов потребуется:
pytest = "^8.3.4"
pytest-cov = "^6.0.0"

Далее в терминале нужно запустить команду:
```
pytest
```


******************************************************************************************************************

# Homework project on implementing functionality for working with banking data

## Running the project
Run the following command in the terminal, being in the root directory of the project, to see the result all functions:
```
python .\__main__.py
```

### Requirement for running:
- python - v3.13

## Package src:

- Product
Accepts 4 required properties and returns data using 4 methods:
    name - returns the name
    description - returns the product description
    price - returns the product price
    quantity - returns the product quantity

- Category
Accepts 3 required properties and returns data using 3 methods
    name - returns category name
    description - returns product description
    products - returns product list
Has 2 attributes:
    category_count - returns number of categories
    product_count - returns number of products


## Testing
To run tests you will need:
pytest = "^8.3.4"
pytest-cov = "^6.0.0"

Next, you need to run the command in the terminal:
```
pytest
```
