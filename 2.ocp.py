from abc import ABC


class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Lion(Animal):
    def make_sound(self):
        print("ROAR")

class Mouse(Animal):
    def make_sound(self):
        print("I want cheese")


animals = [
    Lion(),
    Mouse()
]


def animal_sound(animals: list):
    for animal in animals:
        animal.make_sound()


animal_sound(animals)


class DescontoCliente:
    def __init__(self, price):
        self.__price = price

    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, price):
        self.__price = price

    @abstractmethod
    def give_discount(self):
        pass


class  DescontoFavorito:
    def __init__(self, price):
        super().__init__(price)
    
    def give_discount(self):
        return self.prcie * 0.2


class  DescontoVip:
    def __init__(self, price):
        super().__init__(price)
    
    def give_discount(self):
        return self.prcie * 0.4

