class Animal:
    def __init__(self) -> None:
        """ Initializes the base Animal with empty name, color, kind and float weight. """
        self.name: str = ""
        self.weight = float
        self.color: str = ""
        self.kind: str = ""

    def set_basic_data(self, data_animal: list) -> None:
        """ Sets the name and kind of the animal from a data list.\n
        param list data_animal list with at least 2 elements [name, kind]\n
        return None """
        self.name = data_animal[0]
        self.kind = data_animal[1]

    def get_path_file(self) -> str:
        """ Builds and returns the file path for the animal's type file.\n
        return str path to the corresponding types_animals txt file """
        return f"./types_animals/{self.kind}.txt"

    def set_additional_information_animal(self):
        """ Asks the user for the specific attributes of the animal subtype.\n
        return None """
        pass

    def send_data_to_file_txt(self):
        """ Sends all animal data to the corresponding txt file.\n
        return None """
        pass

    def show_all_data(self):
        """ Displays all stored data of the animal.\n
        return None """
        pass

    def count_all_data(self):
        """ Counts and returns all records in the animal's data file.\n
        return None """
        pass

    def count(self):
        """ Returns the count of animals registered for this type.\n
        return None """
        pass
