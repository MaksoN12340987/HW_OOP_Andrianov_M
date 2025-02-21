import pytest
from src.classes import Product, Category


@pytest.fixture
def product1():
    return Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )


@pytest.fixture
def product2():
    return Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)


@pytest.fixture
def category1():
    return Category(
        "Смартфоны",
        (
"Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
        ),
        [
            Product(
                "Samsung Galaxy S23 Ultra",
                "256GB, Серый цвет, 200MP камера",
                180000.0,
                5,
            ),
            Product("Iphone 15", "512GB, Gray space", 210000.0, 8),
            Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14),
        ],
    )


@pytest.fixture
def category2():
    return Category(
        "Телевизоры",
        (
"Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником"
        ),
        [Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)],
    )
