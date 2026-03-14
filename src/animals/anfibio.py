from . import animal
import validation, files


class Anfibio(animal.Animal):
    def __init__(self):
        """ Initializes Anfibio, inheriting Animal attributes and adding piel. """
        super().__init__()
        self.piel = bool

    def set_additional_information_animal(self) -> None:
        """ Asks the user for weight, color and skin type specific to an amphibian.\n
        return None """
        self.weight = validation.input_number("Ingrese el peso del animal: ")
        self.color = input("Ingrese un color: ")
        self.piel = input("Ingrese el tipo de piel: ")

    def send_data_to_file_txt(self) -> None:
        """ Writes the amphibian's name, weight, color and skin type to its txt file.\n
        return None """
        files.write_new_datum_to_the_file(self.get_path_file(), self.name, self.weight, self.color, self.piel)
