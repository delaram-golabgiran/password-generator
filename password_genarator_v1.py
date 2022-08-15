import string
import random

symbol = "()[]{}.,!@#$%^&*_-+=|\?/<>"
characters = list(string.ascii_letters + string.digits + symbol)

def generate_random_password():
    length = int(input("Enter password length: "))
    random.shuffle(characters)

    password = []
    for i in range(length):
        password.append(random.choice(characters))

    random.shuffle(password)
    print("".join(password))

generate_random_password()