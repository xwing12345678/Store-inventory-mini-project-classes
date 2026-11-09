


class Product:
    total_books:int = 0
    def __init__(self,name:str,price:int|float,quantity:int=0)->None|ValueError: # pyright: ignore[reportGeneralTypeIssues]
        self.__name = name
        self.__price = price
        self.__quantity = quantity

    @property
    def price(self)->int|float:
        return self.__price

    @price.setter
    def price(self, number:int|float):
        if number <= 0:
            raise ValueError("price must be positive")
        self.__price = number

    @property
    def quantity(self)->int:
        return self.__quantity

    def add_stock(self, amount:int)->None|ValueError:
        if amount <= 0:
            raise ValueError("amount must be positive")
        self.__quantity += amount

    def sell(self, amount:int)->None|ValueError:
        if amount > self.__quantity:
            raise ValueError("not enough " + self.__name)
        self.__quantity -= amount

    @property
    def total_value(self)->int|float:
        return self.__price * self.__quantity

    @property
    def name(self):
        return self.__name

    def __str__(self)->str:
        return (self.__name + ": " + str(self.__quantity) + " x " + str(self.__price)
                + " = " + str(self.total_value))