from src.animals import animal
from src import files


class Celentereo(animal.Animal):
    def __init__(self):
        super().__init__()
        self.tenteculos = str