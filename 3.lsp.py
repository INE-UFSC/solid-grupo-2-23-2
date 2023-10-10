"""
Liskov Substitution Principle

Uma subclasse deve ser substituível pela sua superclasse 
"""
class AnimalSemPernas:
    def __init__(self, name: str):
        self.__name = name
    
    def get_name(self) -> str:
        return self.__name


class AnimalComPernas:
    def __init__(self, name: str):
        self.__name = name
    
    def get_name(self) -> str:
        return self.__name

    @abstractmethod
    def leg_count(self):
        pass


class Lion(AnimalComPernas):
    def __init__(self, name: str):
        super().__init__(name)

    def leg_count(self):
        return 4


class Snake(AnimalSemPernas):
    def __init__(self, name: str):
        super().__init__(name)

def animal_leg_count(animals: list):
    count = 0
    for animal in animals:
        if isinstance(animal, AnimalComPernas):
            count += animal.leg_count()
    return count



