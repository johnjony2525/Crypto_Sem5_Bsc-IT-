import hashlib

# Input message
text = input("Enter your message to create hash value: ")

# Generate SHA-256 hash
SHA256_hash = hashlib.sha256(text.encode()).hexdigest()

# Display the hash value
print("SHA-256 Hash:", SHA256_hash)
