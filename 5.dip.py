class Player:
    def __init__(self, name, reporter: Reporter):
        self.__name = name
        self.__hp = 100
        self.__speed = 1
        self.__reporter = reporter

    @property
    def hp(self):
        return self.__hp

    @property
    def name(self):
        return self.__name


class Reporter(ABC):
    def __init__(self, char: Player):
        self.char = char

    @abstractmethod
    def report(self):
        pass

class StatsReporter(Reporter):
    def __init__(self, char: Player):
        super().__init__(char)

    def report(self):
        print(f'Name:{self.char.name()}')
        print(f'HP:{self.char.hp()}')
