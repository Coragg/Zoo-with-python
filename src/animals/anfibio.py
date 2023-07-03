from src.animals import animal
from src import validation, files


class Anfibio(animal.Animal):
    def __init__(self):
        super().__init__()
        self.piel = bool

    def set_additional_information_animal(self):
        self.weight = validation.input_number("Ingrese el peso del animal: ")
        self.color = input("Ingrese un color: ")
        self.piel = input("Ingrese el tipo de piel: ")

    def send_data_to_file_txt(self):
        files.send_data_to_file(self.get_path_file(), self.name, self.weight, self.color, self.piel)

        