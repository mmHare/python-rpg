import hashlib

salt = 'p64q'


def clrscr():
    print('\n' * 5)


def hash_text(textToHash):
    newText = textToHash + salt
    hashed = hashlib.md5(newText.encode())
    return hashed.hexdigest()


def check_hashed(textIn, textHashed):
    return hash_text(textIn) == textHashed
