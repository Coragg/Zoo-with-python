from . import animal
import files, validation


class Celentereo(animal.Animal):
    def __init__(self):
        super().__init__()
        self.tentacles = int

    def set_additional_information_animal(self):
        self.weight = validation.input_number("Ingrese el peso del animal: ")
        self.color = input("Ingrese un color: ")
        self.tentacles = validation.input_number("Ingrese la cantidad de tentaculos. ")

    def send_data_to_file_txt(self):
        files.send_data_to_file(self.get_path_file(), self.name, self.weight, self.color, self.tentacles)