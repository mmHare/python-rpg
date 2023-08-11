from cryptography.fernet import Fernet

def clrscr():
    print('\n' * 5)

def encrypt_text(textToEncrypt):
    key = Fernet.generate_key()
    f = Fernet(key)
    encrypted_string = f.encrypt(textToEncrypt.encode())
    return [encrypted_string, key]

def decrypt_text(textToDecrypt, key):
    f = Fernet(key)
    decrypted_string = f.decrypt(textToDecrypt)
    return decrypted_string.decode()