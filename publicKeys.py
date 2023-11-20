import rsa

publicKey, privateKey = rsa.newkeys(1024)

print(publicKey)
print(privateKey)

message = 'hello'
cipherText = rsa.encrypt(message.encode('ascii'), publicKey)

# print(cipherText)

# print('Original message: ', message)
# print('Encrypted message: ', cipherText)
#
# decryptedText = rsa.decrypt(cipherText, privateKey)
# print('Decrypted message: ', decryptedText.decode("utf-8") )


