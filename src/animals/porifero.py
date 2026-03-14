from . import animal
import files, validation


class Porifero(animal.Animal):

    def __init__(self):
        """ Initializes Porifero, inheriting Animal base attributes (name, weight, color, kind). """
        super().__init__()

    def set_additional_information_animal(self) -> None:
        """ Asks the user for weight and color specific to a porifera (sponge).\n
        return None """
        self.weight = validation.input_number("Ingrese el peso del animal: ")
        self.color = input("Ingrese un color: ")

    def send_data_to_file_txt(self) -> None:
        """ Writes the porifera's name, weight and color to its txt file.\n
        return None """
        files.write_new_datum_to_the_file(self.get_path_file(), self.name, self.weight, self.color)
