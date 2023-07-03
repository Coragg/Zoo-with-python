import files
import os


def close_program():
    print("Cerrar programa...")
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
        pass
    elif options == 9:
        close_program()
    else:
        option_not_allowed()


def input_to_menu():
    try:
        number = int(input("Ingrese una de las opciones validas: "))
        if number > 0:
            menu(number)
        else:
            option_not_allowed()
    except ValueError:
        print("Recuerde que tiene que digitar un numero.")


def main():
    data = files.read_file_csv("information_animals.csv")
    while True:
        option = input_to_menu()
        menu(option, data)    

if __name__ == '__main__':
    main()