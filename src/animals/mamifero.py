from animals import animal
from .. import files

class Mamifero(animal.Animal):
    
    def __init__(self):
        super()
        self.cantidad_patas = int

    def set_addtional_information_animal(self):
        return 

    def send_data_to_file_txt(self):
        print(self.get_path_file())
        # files.send_data_to_file(self.get_path_file())
