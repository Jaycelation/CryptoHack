from sympy import isprime, factorint

def is_primitive_root(g, p):
    phi = p - 1
    factors = factorint(phi)
    for q in factors.keys():
        if pow(g, phi // q, p) == 1:
            return False
    return True


def find_smallest_primitive_root(p):
    for g in range(2, p):
        if is_primitive_root(g, p):
            return g
    return None

p = 28151

smallest_primitive_root = find_smallest_primitive_root(p)
print(f"The smallest primitive element of F_{p} is {smallest_primitive_root}")
