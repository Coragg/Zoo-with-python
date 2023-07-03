def input_number(message_to_user: str):
    """ This function validate if the input is a number greater than zero.
    param str message_to_user
    return eval number """
    while True:
        try:
            number = eval(input(message_to_user))
            if number > 0:
                return number
        except ValueError:
            print("Recuerde que tiene que digitar un numero.")


def search_animal_name(data: list):
    """
    """
    name = input("Ingrese el nombre del animal: ").capitalize()
    for animal in data:
        if name == animal[0]:
            return animal
    return False


def validation_search(data: list):
    """
    """
    search = False
    while search == False:
        search = search_animal_name(data)
        if search == False:
            print("El animal no se encuentra en el censo. Por favor, intente de nuevo.")
    return search