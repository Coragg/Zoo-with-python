import options as application
import files
import os


def presentation():
    """show how we can use the program with these instructions"""
    print("Bienvenido a CENSO ZOO\n----------------------\nA continuacion las opciones que ofrecemos:\n\n")
    print("1- Mostrar cantidad por tipo \n2- Mostrar vertebrados e invertebrados\n"
          "3- Porcentaje de vertebrados e invertebrados\n4- Porcentaje de cada tipo o grupo de animales en el Zoo\n"
          "5- Mostrar la lista de animales almacenados por tipo\n6- Busqueda animal y cantidad por tipo o grupo\n"
          "7- Agregar informacion Animal aleatorio\n8- Agregar animal y sus caracteristicas\n9- Cerrar programa")


def close_program():
    """Close the app and show a notification of the end and one pause."""
    os.system("cls")
    print("Cerrando programa...")
    os.system("pause")
    exit(0)


def option_not_allowed():
    print("Recuerde digitar entre [1-9].")


def menu(options: int, data: list, kind_animal: list):
    """call the function that you want to use in the program"""
    if options == 1:
        application.have_count_of_animals(kind_animal)
    elif options == 2:
        application.mostrar_invertebrado_vertebrado()
    elif options == 3:
        application.show_percentage_of_invertebrado_and_vertebrado(kind_animal)
    elif options == 4:
        application.show_percentage_of_each_type_of_animal(kind_animal)
    elif options == 5:
        application.show_for_kind(kind_animal)
    elif options == 6:
        application.search_all_animal_with_same_name(data)
    elif options == 7:
        application.add_random_animal(data)
    elif options == 8:
        application.add_animal_for_name(data)
    elif options == 9:
        close_program()
    else:
        option_not_allowed()


def input_to_menu(data: list, kind_animal: list):
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


def main():
    data = files.read_file_csv("information_animals.csv")
    kind_animal = ["Anfibio", "Artropodo", "Ave", "Celentereo", "Gusano", "Mamifero", "Molusco", "Pez", "Porifero",
                   "Reptil",  "Equinodermo"]
    presentation()
    while True:
        input_to_menu(data, kind_animal)


if __name__ == '__main__':
    main()
