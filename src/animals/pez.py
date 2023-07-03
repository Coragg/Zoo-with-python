from src.animals import animal
from src import files


class Pez(animal.Animal):

    def __init__(self):
        super().__init__()
        self.cantidad_alas = int