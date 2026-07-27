#generate SHA1
import hashlib

text = input("Enter your message to create hash value: ")

SHA1_hash = hashlib.sha1(text.encode()).hexdigest()
print("SHA1_hash: ", SHA1_hash)
