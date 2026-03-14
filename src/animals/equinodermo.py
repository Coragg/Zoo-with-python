from . import animal
import files, validation


class Equinodermo(animal.Animal):
    def __init__(self):
        """ Initializes Equinodermo, inheriting Animal attributes and adding tipo_estrella_erizo. """
        super().__init__()
        self.tipo_estrella_erizo = str

    def set_additional_information_animal(self) -> None:
        """ Asks the user for weight, color and subtype (estrella or erizo) specific to an echinoderm.\n
        return None """
        self.weight = validation.input_number("Ingrese el peso del animal: ")
        self.color = input("Ingrese un color: ")
        self.tipo_estrella_erizo = input("Ingrese si es tipo estrella o erizo: ")

    def send_data_to_file_txt(self) -> None:
        """ Writes the echinoderm's name, weight, color and subtype to its txt file.\n
        return None """
        files.write_new_datum_to_the_file(self.get_path_file(), self.name, self.weight, self.color, self.tipo_estrella_erizo)
