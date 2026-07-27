
import hashlib

# Input message
text = input("Enter your message to create hash value: ")

SHA512_hash = hashlib.sha512(text.encode()).hexdigest()

print("SHA-512 Hash:", SHA512_hash)
