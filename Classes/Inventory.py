from .Product import Product
from typing import Self
class Inventory:
    def __init__(self) -> None:
        self.__products: list[Product] = []

    def add(self, product: Product) -> Self:
        if self.find(name=product.name) is not None:
            raise ValueError(f"{product.name} already exists")
        self.__products.append(product)
        return self

    def find(self, name: str) -> Product | None:
        for product in self.__products:
            if product.name == name:
                return product
        return None

    def by_value(self) -> list[Product]:
        return sorted(self.__products, key=lambda p: p.total_value, reverse=True)

    @property
    def total_value(self) -> int | float:
        total = 0
        for product in self.__products:
            total += product.total_value
        return total