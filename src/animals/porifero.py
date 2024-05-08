from . import animal
import files, validation


class Porifero(animal.Animal):

    def __init__(self):
        super()

    def set_additional_information_animal(self):
        self.weight = validation.input_number("Ingrese el peso del animal: ")
        self.color = input("Ingrese un color: ")

    def send_data_to_file_txt(self):
        files.write_new_datum_to_the_file(self.get_path_file(), self.name, self.weight, self.color)

