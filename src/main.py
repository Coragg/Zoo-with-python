import options as application
import files
import os


def presentation() -> None:
    """ Prints the welcome message and the list of available menu options to the user.\n
    return None """
    print("Bienvenido a CENSO ZOO\n----------------------\nA continuacion las opciones que ofrecemos:\n\n")
    print("1- Mostrar cantidad por tipo \n2- Mostrar vertebrados e invertebrados\n"
          "3- Porcentaje de vertebrados e invertebrados\n4- Porcentaje de cada tipo o grupo de animales en el Zoo\n"
          "5- Mostrar la lista de animales almacenados por tipo\n6- Busqueda animal y cantidad por tipo o grupo\n"
          "7- Agregar informacion Animal aleatorio\n8- Agregar animal y sus caracteristicas\n9- Cerrar programa")


def close_program() -> None:
    """ Clears the screen, prints a closing message and exits the program.\n
    return None """
    os.system("clear") # for unix systems
    print("Cerrando programa...")
    os.system("sleep 0.5")
    exit(0)


def option_not_allowed() -> None:
    """ Prints a warning message when the user enters an option outside the valid range [1-9].\n
    return None """
    print("Recuerde digitar entre [1-9].")


def menu(options: int, data: list, kind_animal: list) -> None:
    """ Routes the user's selected option to the corresponding application function.\n
    param int options number between 1 and 9 representing the chosen menu action\n
    param list data list of animals loaded from the csv file\n
    param list kind_animal list of animal type names\n
    return None """
    match options:
        case 1:
            application.have_count_of_animals(kind_animal)
        case 2:
            application.show_invertebrado_and_vertebrado()
        case 3:
            application.show_percentage_of_invertebrado_and_vertebrado(kind_animal)
        case 4:
            application.show_percentage_of_each_type_of_animal(kind_animal)
        case 5:
            application.show_for_kind(kind_animal)
        case 6:
            application.search_all_animal_with_same_name(data)
        case 7:
            application.add_random_animal(data)
        case 8:
            application.add_animal_for_name(data)
        case 9:
            close_program()
        case _:
            option_not_allowed()


def input_to_menu(data: list, kind_animal: list) -> None:
    """ Reads a menu option from the user and calls menu() if it is a valid positive integer.\n
    param list data list of animals loaded from the csv file\n
    param list kind_animal list of animal type names\n
    return None """
    try:
        number_entered_by_the_user = int(input("Digite su opcion: "))
        if number_entered_by_the_user > 0:
            menu(number_entered_by_the_user, data, kind_animal)
        else:
            option_not_allowed()
    except ValueError:
        print("Recuerde que tiene que digitar un numero.")


def main() -> None:
    """ Entry point of the program. Loads the animal dataset, defines the animal types and starts the menu loop.\n
    return None """
    dataset_of_animals = files.read_file_csv("information_animals.csv")
    kind_animal = ["Anfibio", "Artropodo", "Ave", "Celentereo", "Gusano", "Mamifero", "Molusco", "Pez", "Porifero",
                   "Reptil",  "Equinodermo"]
    presentation()
    while True:
        input_to_menu(dataset_of_animals, kind_animal)


if __name__ == '__main__':
    main()
