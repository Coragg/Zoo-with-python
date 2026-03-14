from . import animal
import files, validation


class Pez(animal.Animal):

    def __init__(self):
        """ Initializes Pez, inheriting Animal attributes and adding scales. """
        super().__init__()
        self.scales = bool

    def set_additional_information_animal(self) -> None:
        """ Asks the user for weight, color and scale count specific to a fish.\n
        return None """
        self.weight = validation.input_number("Ingrese el peso del animal: ")
        self.color = input("Ingrese un color: ")
        self.scales = validation.input_number("Numero de escamas: ")

    def send_data_to_file_txt(self) -> None:
        """ Writes the fish's name, weight, color and scale count to its txt file.\n
        return None """
        files.write_new_datum_to_the_file(self.get_path_file(), self.name, self.weight, self.color, self.scales)
