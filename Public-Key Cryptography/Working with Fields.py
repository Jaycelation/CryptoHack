def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def mod_inverse(g, p):
    gcd, x, y = extended_gcd(g, p)
    if gcd != 1:
        raise ValueError("Inverse doesn't exist")
    else:
        return x % p

g = 209
p = 991

d = mod_inverse(g, p)
print(f"The modular inverse of {g} modulo {p} is {d}")
