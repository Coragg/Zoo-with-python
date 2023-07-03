from src.animals import animal
from src import files


class Antropodo(animal.Animal):
    def __init__(self):
        super()
        self.cantidad_pares_patas = int
        self.antenas = bool

            