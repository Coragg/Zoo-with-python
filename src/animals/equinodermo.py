from src.animals import animal
from src import files, validation


class Equinodermo(animal.Animal):
    def __init__(self):
        super().__init__()
        self.tipo_estrella_erizo = str

    def set_additional_information_animal(self):
        self.weight = validation.input_number("Ingrese el peso del animal: ")
        self.color = input("Ingrese un color: ")
        self.tipo_estrella_erizo = input("Ingrese si es tipo estrella o erizo: ")

    def send_data_to_file_txt(self):
        files.send_data_to_file(self.get_path_file(), self.name, self.weight, self.color, self.tipo_estrella_erizo)
