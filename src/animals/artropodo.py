from . import animal
import files, validation


class Artropodo(animal.Animal):
    def __init__(self):
        super().__init__()
        self.number_of_pairs_of_legs = int
        self.antenas = str

    def set_additional_information_animal(self):
        self.weight = validation.input_number("Ingrese el peso del animal: ")
        self.color = input("Ingrese un color: ")
        self.number_of_pairs_of_legs = validation.input_number("Ingrese la cantida de pares de patas: ")
        self.antenas = input("Tiene antenas o no tiene: ")

    def send_data_to_file_txt(self):
        files.send_data_to_file(self.get_path_file(), self.name, self.weight, self.color, self.number_of_pairs_of_legs)

            