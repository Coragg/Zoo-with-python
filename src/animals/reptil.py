from src.animals import animal
from src import files

class Reptil(animal.Animal):

    def __init__(self):
        super().__init__()
        self.tierra_mar = bool