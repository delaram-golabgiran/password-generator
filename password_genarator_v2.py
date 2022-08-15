from termcolor import colored
import string
import random

symbol = "()[]{}.,!@#$%^&*_-+=|\?/<>"
characters = list(string.ascii_letters + string.digits + symbol)

while True:
    try:
        length = input("Enter password length: ")
        if length.isnumeric():
            random.shuffle(characters)
            password = []
            password.append(random.choice(characters))

            for i in range(1, int(length)):
                password.append(random.choice(characters))

            random.shuffle(password)
            print(colored("".join(password), "blue", attrs=['bold']))

        else:
            print("Wrong, Input digit")

    except ValueError:
        pass
