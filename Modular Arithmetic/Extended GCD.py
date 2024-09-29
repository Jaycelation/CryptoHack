#Knowing that p,q are prime, what would you expect gcd(p,q) to be? For more details on the extended Euclidean algorithm, check out this page

def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gcd, x1, y1 = extended_gcd(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
        return gcd, x, y

p = 26513
q = 32321

gcd, u, v = extended_gcd(p, q)
print(f"u = {u}, v = {v}")



