import options as application
import files
import os


def presentation() -> None:
    """instructions of the program for the user"""
    print("Bienvenido a CENSO ZOO\n----------------------\nA continuacion las opciones que ofrecemos:\n\n")
    print("1- Mostrar cantidad por tipo \n2- Mostrar vertebrados e invertebrados\n"
          "3- Porcentaje de vertebrados e invertebrados\n4- Porcentaje de cada tipo o grupo de animales en el Zoo\n"
          "5- Mostrar la lista de animales almacenados por tipo\n6- Busqueda animal y cantidad por tipo o grupo\n"
          "7- Agregar informacion Animal aleatorio\n8- Agregar animal y sus caracteristicas\n9- Cerrar programa")


def close_program() -> None:
    """Close the app and show a notification of the end and one pause."""
    os.system("clear") # for unix systems
    print("Cerrando programa...")
    os.system("sleep 0.5")
    exit(0)


def option_not_allowed() -> None:
    print("Recuerde digitar entre [1-9].")


def menu(options: int, data: list, kind_animal: list) -> None:
    """Aplication of menu"""
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
    """ ask you one option valid and call the function menu for make that you want to do
    param data: list of animals """
    try:
        number = int(input("Digite su opcion: "))
        if number > 0:
            menu(number, data, kind_animal)    
        else:
            option_not_allowed()
    except ValueError:
        print("Recuerde que tiene que digitar un numero.")


def main() -> None:
    data = files.read_file_csv("information_animals.csv")
    kind_animal = ["Anfibio", "Artropodo", "Ave", "Celentereo", "Gusano", "Mamifero", "Molusco", "Pez", "Porifero",
                   "Reptil",  "Equinodermo"]
    presentation()
    while True:
        input_to_menu(data, kind_animal)


if __name__ == '__main__':
    main()
