class AnimalDados:
    def __init__(self, name: str):
        self.__name = name
    
    def get_name(self) -> str:
        return self.__name

class SalvamentoDados:
    def __init__(self, animal: AnimalDados):
        if isinstace(animal, AnimalDados):
            self.animal = animal

    def save(self) -> None:
        # salva 
        pass
