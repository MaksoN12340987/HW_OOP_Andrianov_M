# Class Product
class Product:

    model: str
    characteristics: str
    cost: int
    number: int

    def __init__(self, model, characteristics, cost, number):
        self.name = model
        self.description = characteristics
        self.price = cost
        self.quantity = number


class Category:

    category: str
    description: str
    products_list: list
    category_count = 0
    product_count = 0

    def __init__(self, category, description, products_list):
        self.name = category
        self.description = description
        self.products = products_list
        Category.category_count += 1
        Category.product_count += len(products_list)
