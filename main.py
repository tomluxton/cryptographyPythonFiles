import cryptography
from cryptography.fernet import Fernet

message = b'Hello World'

print(message)

key = Fernet.generate_key()
cipher = Fernet(key)
encrypted_message = cipher.encrypt(message)

print('Original message: ', message)
print('Encrypted message: ', encrypted_message)

decrypted_message = cipher.decrypt(encrypted_message)


print('Decrypted message: ', decrypted_message)

