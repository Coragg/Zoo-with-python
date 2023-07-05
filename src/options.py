from animals import anfibio, artropodo, ave, celentereo, gusano, mamifero, molusco, pez, porifero, reptil, equinodermo
import validation
import random
import files


def class_to_send_data(all_data):
    """we received the data, and with data, we'll know what kind of animal we send the information and what interface to
     use.\n
    param all_data list with three or two index """
    new_animal_we_need_is = None
    if all_data[1] == "Anfibio":
        new_animal_we_need_is = anfibio.Anfibio()

    elif all_data[1] == "Artropodo":
        new_animal_we_need_is = artropodo.Artropodo()

    elif all_data[1] == "Ave":
        new_animal_we_need_is = ave.Ave()

    elif all_data[1] == "Celentereo":
        new_animal_we_need_is = celentereo.Celentereo()

    elif all_data[1] == "Gusano":
        new_animal_we_need_is = gusano.Gusano()

    elif all_data[1] == "Mamifero":
        new_animal_we_need_is = mamifero.Mamifero()

    elif all_data[1] == "Molusco":
        new_animal_we_need_is = molusco.Molusco()

    elif all_data[1] == "Pez":
        new_animal_we_need_is = pez.Pez()

    elif all_data[1] == "Porifero":
        new_animal_we_need_is = porifero.Porifero()

    elif all_data[1] == "Reptil":
        new_animal_we_need_is = reptil.Reptil()

    elif all_data[1] == "Equinodermo":
        new_animal_we_need_is = equinodermo.Equinodermo()

    new_animal_we_need_is.set_basic_data(all_data)
    new_animal_we_need_is.set_additional_information_animal()
    new_animal_we_need_is.send_data_to_file_txt()


def add_animal_for_name(data_of_animals: list):
    """ ask the name in terminal, search the animal and send the data to a file \n
    param data_of_animals list
    """
    all_data = validation.searching_animal_on_csv(data_of_animals)
    class_to_send_data(all_data)
    print('\n')


def add_random_animal(data: list):
    """ generate a random animal in the list of animals and send thad animal to one file txt. \n
    param data list\n
    """
    number_the_new_animal = random.randint(0, 128)
    all_data_the_animal = data[number_the_new_animal]
    print(f"El animal es: {all_data_the_animal[0]}")
    class_to_send_data(all_data_the_animal)
    print('\n')


def show_for_kind():
    """show you all data of the kind animal.    """
    kind_animal = ["Anfibio", "Artropodo", "Ave", "Celentereo", "Gusano", "Mamifero", "Molusco", "Pez", "Porifero",
                   "Reptil",  "Equinodermo"]
    kind = False
    while not kind:
        searching = input("Ingrese el tipo de animal: ").capitalize()
        if searching in kind_animal:
            kind = searching
        else:
            print("Ingrese un tipo de animal valido. ")
    path_fila = f"./types_animals/{kind}.txt"
    print("\n")
    files.read_file_txt_and_show(path_fila)


def filter_data_by_animal_name(matrix_kind: list, name_to_search: str):
    """filter the animals to search and have a list\n
    param matrix_kind list\n
    name_to_search str\n
    return leaked_data list"""
    leaked_data = []
    for rows in matrix_kind:
        if name_to_search == rows[0]:
            leaked_data.append(rows)
    return leaked_data


def show_all_data_filter(lista_animals: list):
    """ show all the animals filter\n
    param lista_animals list     """
    for animal_information in lista_animals:
        data_to_show = ""
        traversed_indices = 1
        for columns in animal_information:
            if traversed_indices < len(animal_information):
                data_to_show += f'{columns}-'
            else:
                data_to_show += f'{columns}'
            traversed_indices += 1
        print(data_to_show)


def search_all_animal_with_same_name(data: list):
    """ find and count animals \n
    param data list"""
    name_animal_to_search = validation.searching_animal_on_csv(data)
    path_file = f"./types_animals/{name_animal_to_search[1]}.txt"
    matrix_of_all_animals = files.read_file_txt_and_have_matrix(path_file)
    filter_data = filter_data_by_animal_name(matrix_of_all_animals, name_animal_to_search[0])
    show_all_data_filter(filter_data)
    print(f"La cantidad de {name_animal_to_search[0].lower()} es {len(filter_data)}.\n")
