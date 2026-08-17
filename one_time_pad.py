import onetimepad


cipher=onetimepad.encrypt('vivek','random')
print("Cipher text is:-",cipher)


print(" ----decryption----")

plaintext=onetimepad.decrypt(cipher,'random')

print("plain text is :-",plaintext)
