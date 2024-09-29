# Commutative: A ⊕ B = B ⊕ A
# Associative: A ⊕ (B ⊕ C) = (A ⊕ B) ⊕ C
# Identity: A ⊕ 0 = A
# Self-Inverse: A ⊕ A = 0
from pwn import *

KEY1 = 'a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313'
KEY2xKEY1 = '37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e'
KEY2xKEY3 = 'c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1'
FLAGxKEY1xKEY3xKEY2 = '04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf'

KEY1 = bytes.fromhex(KEY1)
KEY2 = xor(bytes.fromhex(KEY2xKEY1), KEY1)
KEY3 = xor(bytes.fromhex(KEY2xKEY3), KEY2)
KEY4 = xor(bytes.fromhex(KEY2xKEY1), KEY3)
FLAG = xor(bytes.fromhex(FLAGxKEY1xKEY3xKEY2), KEY4)

print(FLAG)