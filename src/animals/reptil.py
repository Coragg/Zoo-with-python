from . import animal
import files, validation


class Reptil(animal.Animal):

    def __init__(self):
        """ Initializes Reptil, inheriting Animal attributes and adding tierra_mar. """
        super().__init__()
        self.tierra_mar = str

    def set_additional_information_animal(self) -> None:
        """ Asks the user for weight, color and habitat (land or sea) specific to a reptile.\n
        return None """
        self.weight = validation.input_number("Ingrese el peso del animal: ")
        self.color = input("Ingrese un color: ")
        self.tierra_mar = input("El animal es de tierra o mar: ")

    def send_data_to_file_txt(self) -> None:
        """ Writes the reptile's name, weight, color and habitat to its txt file.\n
        return None """
        files.write_new_datum_to_the_file(self.get_path_file(), self.name, self.weight, self.color, self.tierra_mar)
