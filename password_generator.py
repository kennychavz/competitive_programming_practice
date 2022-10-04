from string import ascii_lowercase


import random
import string


def password_generator(size):
    "Generate a random password based on the size given"
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(size))


print(password_generator(5))
