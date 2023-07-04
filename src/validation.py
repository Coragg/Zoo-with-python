def input_number(message_to_user: str):
    """ This function validate if the input is a number greater than zero.\n
    param str message_to_user\n
    return eval number """
    while True:
        try:
            number = float(input(message_to_user))
            if number > 0:
                return number
        except ValueError:
            print("Recuerde que tiene que digitar un numero.")


def search_animal_name(data: list):
    """ search a name in the data on the matrix, the search is doing in the first index.\n
    param data list 3xN str\n
    return false or a list"""
    name = input("Ingrese el nombre del animal: ").capitalize()
    for animal in data:
        if name == animal[0]:
            return animal
    return False


def searching_animal_on_csv(data: list):
    """search a name in the matrix, and if the name is not find, the function asks you again for another name in the
    matrix \n
    param data list 3xN str\n
    return a list """
    search = False
    while not search:
        search = search_animal_name(data)
        if not search:
            print("El animal no se encuentra en el censo. Por favor, intente de nuevo.")
    return search
