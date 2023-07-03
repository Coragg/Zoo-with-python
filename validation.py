def input_natural_number(message_to_user: str):
    while True:
        try:
            number = eval(input(message_to_user))
            if number >= 0.1:
                return number
        except ValueError:
            print("Recuerde que tiene que digitar un numero.")