from . import animal
import files, validation


class Ave(animal.Animal):
    def __init__(self):
        super().__init__()
        self.number_of_wings = int

    def set_additional_information_animal(self):
        self.weight = validation.input_number("Ingrese el peso del animal: ")
        self.color = input("Ingrese un color: ")
        self.number_of_wings = validation.input_number("Ingrese la cantida de alas: ")

    def send_data_to_file_txt(self):
        files.write_new_datum_to_the_file(self.get_path_file(), self.name, self.weight, self.color, self.number_of_wings)
