# Class 
class Category:
    """Accepts 3 required properties and returns data using 3 methods
    name - returns category name
    description - returns product description
    products - returns product list
    Has 2 attributes:
    category_count - returns number of categories
    product_count - returns number of products

    """

    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(products)

    def add_product(self, new_item=[]):
        self.__products = [new_item]
    
    @property.getter
    def products(self):
        return self.__products
