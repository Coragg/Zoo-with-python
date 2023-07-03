from animals import anfibio, antropodo, ave, celentereo, gusano, mamifero, molusco, pez, porifero, reptil
import validation


def add_animal_for_name(data_of_animals: list):
    """
    """
    all_data = validation.searching_animal(data_of_animals)
    new_animal_we_need_is = None
    if all_data[1] == "Anfibio":
        new_animal_we_need_is = anfibio.Anfibio()

    elif all_data[1] == "Antropodo":
        new_animal_we_need_is = antropodo.Antropodo()

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

    new_animal_we_need_is.set_basic_data(all_data)
    new_animal_we_need_is.set_additional_information_animal()
    new_animal_we_need_is.send_data_to_file_txt()


    