# from cryptography.fernet import Fernet
import hashlib


def clrscr():
    print('\n' * 5)


# def encrypt_text(textToEncrypt, key):
#     f = Fernet(key)
#     encrypted_string = f.encrypt(textToEncrypt.encode())
#     return [encrypted_string, key]


# def decrypt_text(textToDecrypt, key):
#     f = Fernet(key)
#     decrypted_string = f.decrypt(textToDecrypt)
#     return decrypted_string.decode()


def hash_text(textToHash):
    salt = 'p64q'
    newText = textToHash + salt
    hashed = hashlib.md5(newText.encode())
    return hashed.hexdigest()


def check_hashed(textIn, textHashed):
    return hash_text(textIn) == textHashed
