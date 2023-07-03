class Animal():
    def __init__(self):
        self.name = str
        self.weight = float
        self.color = str
        self.kind = ""

    def set_basic_data(self, data_animal: list):
        self.name = data_animal[0]
        self.kind = data_animal[1]

    def get_path_file(self):
        return f"./types_animals/{self.kind}.txt"
    
    def send_data_to_file_txt(self):
        pass

    def show_all_data(self):
        pass

    def count_all_data(self):
        pass

    def count(self):
        pass
        
    