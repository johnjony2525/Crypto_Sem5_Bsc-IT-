from pycipher import Railfece

plaintext=(input("Enter the message to rails: "))
rails = int(input("Enter the number of rails: "))

ciphertext = cipher.encrypt(plaintext, rails)

print(ciphertext)

decrypted_text = cipher.decrypt(ciphertext, rails)
print(decrypted_text)
