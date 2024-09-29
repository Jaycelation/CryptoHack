plaintext  = 12
e = 65537
p = 17
q = 23
n = p*q

ciphertext = pow(plaintext, e, n)
print(ciphertext)