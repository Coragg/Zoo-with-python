from . import animal
import files, validation


class Molusco(animal.Animal):
    def __init__(self):
        super().__init__()
        self.tipo_estrella_erizo = str

    def set_additional_information_animal(self):
        self.weight = validation.input_number("Ingrese el peso del animal: ")
        self.color = input("Ingrese un color: ")
        self.tipo_estrella_erizo = input("Diganos si es erizo o estrella: ")

    def send_data_to_file_txt(self):
        files.send_data_to_file(self.get_path_file(), self.name, self.weight, self.color, self.tipo_estrella_erizo)
        