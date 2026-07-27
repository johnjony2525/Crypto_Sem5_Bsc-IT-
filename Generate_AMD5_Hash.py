import hashlib

text = input("Enter your message to create hash value: ")

md5_hash = hashlib.md5(text.encode()).hexdigest()
print("md5_hash: ", md5_hash)
