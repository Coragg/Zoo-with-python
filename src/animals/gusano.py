from src.animals import animal
from src import files


class Gusano(animal.Animal):
    def __init__(self):
        super().__init__()
        self.tipo_cuerpo = bool