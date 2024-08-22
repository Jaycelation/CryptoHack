def gcd_extended(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = gcd_extended(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def mod_inverse(a, m):
    gcd, x, y = gcd_extended(a, m)
    if gcd != 1:
        return None
    else:
        return x % m

def solve_modular_equation(a, b, c):
    a_inv = mod_inverse(a, c)
    if a_inv is None:
        return "Không có nghiệm, vì a và c không nguyên tố cùng nhau."
    x = (a_inv * b) % c
    return x

a = int(input("Nhập giá trị a: "))
b = int(input("Nhập giá trị b: "))
c = int(input("Nhập giá trị c: "))
result = solve_modular_equation(a, b, c)
print(f"Nghiệm của phương trình {a}x ≡ {b} mod {c} là: {result}")
