from typing import Protocol
class ProductProtocol(Protocol):
    name: str
    total_value: int | float

class Inventory:
    def __init__(self) -> None:
        self.__products: list[ProductProtocol] = []

    def add(self, product: ProductProtocol) -> None:
        if self.find(name=product.name) is not None:
            raise ValueError(f"{product.name} already exists")
        self.__products.append(product)

    def find(self, name: str) -> ProductProtocol | None:
        for product in self.__products:
            if product.name == name:
                return product
        return None

    def by_value(self) -> list[ProductProtocol]:
        return sorted(self.__products, key=lambda p: p.total_value, reverse=True)

    @property
    def total_value(self) -> int | float:
        total = 0
        for product in self.__products:
            total += product.total_value
        return total