# Select two prime no's. Suppose P = 11 and Q = 13.
# Now First part of the Public key  : n = P*Q = 143.
#  We also need a small exponent say e :
# But e Must be
# An integer.
# Not be a factor of Φ(n) (also called phi) which is (P-1) * (Q-1) = 10 * 12 = 120
# 1 < e < Φ(n),
# Let us now consider it (e) to be equal to 7.
#     Our Public Key is made of n and e or 143 and 7

# Now calculate Private Key, d :
# d = ( k * Φ(n) + 1 ) / e, for some integer k
# Let use k = 6,
# value of d is = (6 * 120 + 1) / 7 = 103

# we have a message 'hi'
# use the ord() function to convert each letter to a number
# so ord("h") = 104 , and ord("i") = 105
# Convert letters to numbers : h  = 104 and i = 105
    # FOR H
        # Encrypted Data c = (m^e)mod n = (104^7) mod 143 = 91
    # FOR I
        # Encrypted Data c = (m^e)mod n = (105^7) mod 143 = 118
#

# Now we will decrypt c = 91, and c = 118 :
    # H
        # Decrypted Data = (c^d)mod n =  (91^103) mod 143 = 104
    # I
        # Decrypted Data = (c^d)mod n =  (118^103) mod 143 = 105



# Using chr() which converts the ords number into a character chr(104) = h and chr(105) = i
# i.e. "hi".

# So lets do this in code

public_key = None
private_key = None
n = None

def setKeys():
    global public_key, private_key, n

    prime1 = 11
    prime2 = 13

    n = prime1 * prime2

    e = 7

    phi = (prime1 - 1) * (prime2 - 1)

    public_key = e

    k = 6
    d = (k * phi + 1) / e

    private_key = d

    return

def encode(message, key):
    encoded_message = []

    for letter in message:
        # print(letter)
        # print(ord(letter))
        encoded_letter = (ord(letter) ** key) % n
        encoded_message.append(encoded_letter)

    # print(encoded_message)
    return encoded_message

def decode(encoded_message, key):
    decoded_message = ''

    for num in encoded_message:
        # print(num)
        # print(chr(num))
        decoded_letter = chr((num**int(key)) % n)
        decoded_message = decoded_message + decoded_letter
    return decoded_message


if __name__ == '__main__':
    setKeys()

    message = "Hellooo"

    print ("Our message:", message)
    print("Coded message: ", encode(message, public_key))
    print("Decoded message: ", decode(encode(message, public_key), private_key))

