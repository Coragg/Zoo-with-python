def input_number(message_to_user: str):
    """ This function validate if the input is a number greater than zero.
    param str message_to_user
    return eval number """
    while True:
        try:
            number = eval(input(message_to_user))
            if number > 0:
                return number
        except ValueError:
            print("Recuerde que tiene que digitar un numero.")


