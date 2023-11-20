import hashlib

password = 'password1'

hashobj = hashlib.sha256(password.encode())

print(hashobj.hexdigest())
