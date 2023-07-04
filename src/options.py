from animals import anfibio, artropodo, ave, celentereo, gusano, mamifero, molusco, pez, porifero, reptil, equinodermo
import validation
import files
import random


def class_to_send_data(all_data):
    """we received the data, and with data, we'll know what kind of animal we send the information and what interface to
     use.\n
    paramm all_data list with three or two index
    """
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
    print('\n')
    all_data = validation.searching_animal_on_csv(data_of_animals)
    class_to_send_data(all_data)
    print('\n')


def add_random_animal(data: list):
    """ generate a random animal in the list of animals and send thad animal to one file txt. \n
    param data list\n
    """
    number_the_new_animal = random.randint(0, 128)
    all_data_the_animal = data[number_the_new_animal]
    print(f"El animal es: {all_data_the_animal}")
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
    files.read_file_txt(path_fila)
