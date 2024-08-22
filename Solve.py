from Crypto.PublicKey import RSA
from base64 import b64decode

with open('certificate.pem', 'r') as pem_file:
    pem_data = pem_file.read()

key = RSA.import_key(pem_data)

modulus = key.n

print(modulus)
