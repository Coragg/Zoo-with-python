from animals import anfibio, antropodo, ave, celentereo, gusano, mamifero, molusco, pez, porifero, reptil
import validation
import os






def add_animal_for_name(data: list):
    """
    """
    all_data = validation.validation_search(data)
    if all_data[1] == "Anfibio":
        print("El animal es un anfibio.")
    elif all_data[1] == "Antropodo":
        print("El animal es un antropodo.")
    elif all_data[1] == "Ave":
        print("El animal es un ave.")
    elif all_data[1] == "Celentereo":
        print("El animal es un celentereo.")
    elif all_data[1] == "Gusano":
        print("El animal es un gusano.")
    elif all_data[1] == "Mamifero":
        print("El animal es un mamifero.")
    elif all_data[1] == "Molusco":
        print("El animal es un molusco.")
    elif all_data[1] == "Pez":
        print("El animal es un pez.")
    elif all_data[1] == "Porifero":
        print("El animal es un porifero.")
    elif all_data[1] == "Reptil":
        print("El animal es un reptil.")
    