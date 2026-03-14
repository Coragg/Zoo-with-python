from . import animal
import validation, files


class Mamifero(animal.Animal):

    def __init__(self):
        """ Initializes Mamifero, inheriting Animal attributes and adding cantidad_patas. """
        super().__init__()
        self.cantidad_patas = int

    def set_additional_information_animal(self) -> None:
        """ Asks the user for weight, color and number of legs specific to a mammal.\n
        return None """
        self.weight = validation.input_number("Ingrese el peso del animal: ")
        self.color = input("Ingrese un color: ")
        self.cantidad_patas = validation.input_number("Ingrese la cantida de patas: ")

    def send_data_to_file_txt(self) -> None:
        """ Writes the mammal's name, weight, color and leg count to its txt file.\n
        return None """
        files.write_new_datum_to_the_file(self.get_path_file(), self.name, self.weight, self.color, self.cantidad_patas)
