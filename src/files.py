import os


def send_data_to_file(path_and_name_file: str, name:str, weight: eval, color: str, first_data = False, second_data = False):
    """
    """
    try: 
        with open(path_and_name_file, "a") as file:
            if first_data == False and second_data == False:
                file.write(f"{name}-{weight}-{color}\n")
            elif first_data != False and second_data == False:
                file.write(f"{name}-{weight}-{color}-{first_data}\n")
            else:
                file.write(f"{name}-{weight}-{color}-{first_data}-{second_data}\n")
    except:
        os.system("color 4")
        print(f"Error in the process to send data in {path_and_name_file}")


def read_file_txt(path_file: str):
    """
    """
    try:
        with open(path_file, "r", encoding="UTF-8") as file:
            print(file.read())
    except FileNotFoundError:
        os.system("color 4")
        print(f"The file {path_file} is not found. ")


def read_file_csv(path_file: str):
    """
    """
    try:
        data_to_show = []
        with open(path_file, "r", encoding="UTF-8") as file:
            for text_line in file:
                line_reading = text_line.replace('\n', "").split(sep=",")
                data_to_show.append(line_reading)
        return data_to_show
                
    except FileNotFoundError:
        os.system("color 4")
        print(f"The file {path_file} is not found. ")
        
