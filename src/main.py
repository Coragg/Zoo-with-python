import options as application
import files
import os


def presentation():
    print("Bienvenido a CENSO ZOO\n----------------------\nA continuacion las opciones que ofrecemos:\n\n")
    print("1- Mostrar cantidad por tipo \n2- Mostrar vertebrados e invertebrados\n3- Porcentaje de vertebrados e invertebrados\n4- Porcentaje de cada tipo o grupo de animales en el Zoo\n5- Mostrar la lista de animales almacenados por tipo\n6- Busqueda animal y cantidad por tipo o grupo\n7- Agregar informacion Animal aleatorio\n8- Agregar animal y sus caracteristicas\n9- Cerrar programa")


def close_program():
    print("Cerrando programa...")
    os.system("cls")
    os.system("pause")
    exit(0)


def option_not_allowed():
    print("Recuerde digitar entre [1-9].")


def menu(options: int, data: list):
    if options == 1:
        pass
    elif options == 2:
        pass
    elif options == 3:
        pass
    elif options == 4:
        pass
    elif options == 5:
        pass
    elif options == 6:
        pass
    elif options == 7:
        pass
    elif options == 8:
        application.add_animal_for_name(data)
    elif options == 9:
        close_program()
    else:
        option_not_allowed()


def input_to_menu(data: list):
    try:
        number = int(input("Ingrese una de las opciones validas: "))
        if number > 0:
            menu(number, data)    
        else:
            option_not_allowed()
    except ValueError:
        print("Recuerde que tiene que digitar un numero.")


def main():
    data = files.read_file_csv("information_animals.csv")
    presentation()
    while True:
        input_to_menu(data)


if __name__ == '__main__':
    main()