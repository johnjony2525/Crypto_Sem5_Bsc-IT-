write a python program to implement Decryption.


##write a python program to implement Caesa cipher.
from email.mime import message


def caesar_cipher(message, key):
    encrypted_message = ''
    for char in message:
        if char.isupper():
            encrypted_message = chr((ord(char) - key-65) % 26 + 65)
        elif char.islower():
            encrypted_char = chr((ord(char) - key - 97) % 26 + 97)
        else:
            encrypted_char=char
        encrypted_message += encrypted_char
    return encrypted_message
message = input('Enter message: ')
key = int (input('Enter key: '))
encrypted_message = caesar_cipher(message, key)

print("Original message: ", message)
print("shift:", key)
print("Encrypted message: ", encrypted_message)
