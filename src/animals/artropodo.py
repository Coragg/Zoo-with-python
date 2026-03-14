from . import animal
import files, validation


class Artropodo(animal.Animal):
    def __init__(self):
        """ Initializes Artropodo, inheriting Animal attributes and adding number_of_pairs_of_legs and antenas. """
        super().__init__()
        self.number_of_pairs_of_legs = int
        self.antenas = str

    def set_additional_information_animal(self) -> None:
        """ Asks the user for weight, color, pairs of legs and antennae presence specific to an arthropod.\n
        return None """
        self.weight = validation.input_number("Ingrese el peso del animal: ")
        self.color = input("Ingrese un color: ")
        self.number_of_pairs_of_legs = validation.input_number("Ingrese la cantida de pares de patas: ")
        self.antenas = input("Tiene antenas o no tiene: ")

    def send_data_to_file_txt(self) -> None:
        """ Writes the arthropod's name, weight, color and pairs of legs to its txt file.\n
        return None """
        files.write_new_datum_to_the_file(self.get_path_file(), self.name, self.weight, self.color, self.number_of_pairs_of_legs)
