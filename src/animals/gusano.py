from . import animal
import files, validation


class Gusano(animal.Animal):
    def __init__(self):
        """ Initializes Gusano, inheriting Animal attributes and adding kind_body. """
        super().__init__()
        self.kind_body = str

    def set_additional_information_animal(self) -> None:
        """ Asks the user for weight, color and body type specific to a worm.\n
        return None """
        self.weight = validation.input_number("Ingrese el peso del animal: ")
        self.color = input("Ingrese un color: ")
        self.kind_body = input("Tipo de cuerpo: ")

    def send_data_to_file_txt(self) -> None:
        """ Writes the worm's name, weight, color and body type to its txt file.\n
        return None """
        files.write_new_datum_to_the_file(self.get_path_file(), self.name, self.weight, self.color, self.kind_body)
