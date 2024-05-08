import os


def write_new_datum_to_the_file(path_and_name_file: str, name: str, weight: eval, color: str, 
                                first_datum=None, second_datum=None):
    """ create or add data to a file with the path, name and extension of the file
    param path_and_name_file str
    param name str
    param weight eval
    param color str
    param first_datum str or eval or None
    param second_datum str or eval or None"""
    try:
        with open(path_and_name_file, "a") as file:
            if first_datum is None and second_datum is None:
                file.write(f"{name}-{weight}-{color}\n")
            elif first_datum is not None and second_datum is None:
                file.write(f"{name}-{weight}-{color}-{first_datum}\n")
            else:
                file.write(f"{name}-{weight}-{color}-{first_datum}-{second_datum}\n")
    except FileExistsError:
        os.system("color 4")
        print(f"Error in the process to send data in {path_and_name_file}")


def read_file_txt_and_show(path_file: str):
    """ Reading a file txt and show the data of the file. 
    param path_file: path and name of the file txt"""
    try:
        with open(path_file, "r", encoding="UTF-8") as file:
            print(file.read())
    except FileNotFoundError:
        os.system("color 4")
        print(f"The file in {path_file} is not found. ")


def read_file_csv(the_path_of_file_and_name: str):
    """ Reading a file csv and return a list with the data of the file. 
    param path_file: path and name of the file csv
    return: list with the data of the file csv """
    try:
        data_to_show = []
        with open(the_path_of_file_and_name, "r", encoding="UTF-8") as file:
            for text_line in file:
                line_reading = text_line.replace('\n', "").split(sep=",")
                data_to_show.append(line_reading)
        return data_to_show
    except FileNotFoundError:
        os.system("color 4")
        print(f"The file {the_path_of_file_and_name} is not found. ")


def read_file_txt_and_have_matrix(the_path_of_file_and_name: str):
    """ Reading a file txt and return a list with the data of the file. 
    param path_file: path and name of the file csv
    return: list with the data of the file csv   """
    try:
        data_file = []
        with open(the_path_of_file_and_name, "r") as file:
            for text_line in file:
                the_line_read = text_line.replace("\n", "").split(sep="-")
                data_file.append(the_line_read)
        return data_file
    except FileNotFoundError:
        os.system("color 4")
        print(f"The file in {the_path_of_file_and_name} is not found.")
