message = 'babe'

def caesarsEncryption(message, key):
    encrypted_message = ''

    alphabet = 'abcdefghijklmnopqrstuvwxyz'


    for letter in message:
        encrypted_letter = alphabet[(alphabet.index(letter) + key) % 26]
        encrypted_message = encrypted_message + encrypted_letter

    return encrypted_message

print(caesarsEncryption(message, 4))


# print('Original message: ', message)
# print('Encrypted message: ', encrypted_message)
# print('Decrypted message: ', decrypted_message)