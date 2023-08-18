'''simple utility functions'''
import hashlib
import random

salt = 'p64q'


def clrscr():
    print(('\n' * 2) + ('-'*25) + ('\n' * 2))


def print_response(message):
    print('\n(!)', message)


def prompt_player(message="") -> str:
    print()
    if message != "":
        print(message)
    return input(">> ").strip()


def hash_text(textToHash):
    newText = textToHash + salt
    hashed = hashlib.md5(newText.encode())
    return hashed.hexdigest()


def check_hashed(textIn, textHashed):
    return hash_text(textIn) == textHashed


def dice(sides: int):
    return random.randint(1, sides)


def get_attribute_modifier(attrValue):
    if attrValue > 0:
        return (attrValue-10)//2
