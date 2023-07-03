from animals import anfibio, antropodo, ave, celentereo, gusano, mamifero, molusco, pez, porifero, reptil
import validation


def add_animal_for_name(data_of_animals: list):
    """
    """
    all_data = validation.searching_animal(data_of_animals)
    if all_data[1] == "Anfibio":
        new_animal_we_need_is = anfibio.Anfibio()
        new_animal_we_need_is.set_basic_data(all_data)
        new_animal_we_need_is.set_additional_information_animal()
        new_animal_we_need_is.send_data_to_file_txt()
    elif all_data[1] == "Antropodo":
        new_animal_we_need_is = antropodo.Antropodo()
        new_animal_we_need_is.set_basic_data(all_data)
        new_animal_we_need_is.set_additional_information_animal()
        new_animal_we_need_is.send_data_to_file_txt()
    elif all_data[1] == "Ave":
        new_animal_we_need_is = ave.Ave()
        new_animal_we_need_is.set_basic_data(all_data)
        new_animal_we_need_is.set_additional_information_animal()
        new_animal_we_need_is.send_data_to_file_txt()
    elif all_data[1] == "Celentereo":
        new_celentereo = celentereo.Celentereo()
        new_celentereo.set_basic_data(all_data)
        new_celentereo.set_additional_information_animal()
        new_celentereo.send_data_to_file_txt()
    elif all_data[1] == "Gusano":
        new_animal_we_need_is = gusano.Gusano()
        new_animal_we_need_is.set_basic_data(all_data)
        new_animal_we_need_is.set_additional_information_animal()
        new_animal_we_need_is.send_data_to_file_txt()
    elif all_data[1] == "Mamifero":
        new_animal_we_need_is = mamifero.Mamifero()
        new_animal_we_need_is.set_basic_data(all_data)
        new_animal_we_need_is.set_additional_information_animal()
        new_animal_we_need_is.send_data_to_file_txt()
    elif all_data[1] == "Molusco":
        new_animal_we_need_is = molusco.Molusco()
        new_animal_we_need_is.set_basic_data(all_data)
        new_animal_we_need_is.set_additional_information_animal()
        new_animal_we_need_is.send_data_to_file_txt()
    elif all_data[1] == "Pez":
        new_animal_we_need_is = pez.Pez()
        new_animal_we_need_is.set_basic_data(all_data)
        new_animal_we_need_is.set_additional_information_animal()
        new_animal_we_need_is.send_data_to_file_txt()
    elif all_data[1] == "Porifero":
        new_porifero = porifero.Porifero()
        new_porifero.set_basic_data(all_data)
        new_porifero.set_additional_information_animal()
        new_porifero.send_data_to_file_txt()
    elif all_data[1] == "Reptil":
        new_animal_we_need_is = reptil.Reptil()
        new_animal_we_need_is.set_basic_data(all_data)
        new_animal_we_need_is.set_additional_information_animal()
        new_animal_we_need_is.send_data_to_file_txt()


    