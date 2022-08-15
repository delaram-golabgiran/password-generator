from termcolor import colored
import string
import random

symbol = "()[]{}.,!@#$%^&*_-+=|\?/<>"
characters = list(string.ascii_letters + string.digits + symbol)
while True:
    try:
        length = input("Enter password length: ")
        if length.isnumeric():

            if int(length) < 8:
                print(colored("<Enter greater than 8>", "red"))
            else:
                random.shuffle(characters)
                password = []
                password.append(random.choice(characters))

                for i in range(1, int(length)):
                    password.append(random.choice(characters))

                random.shuffle(password)
                print(colored("".join(password), "blue", attrs=['bold']))

        else:
            print(colored("<Wrong, Input digit>", "red"))

    except ValueError:
        pass
