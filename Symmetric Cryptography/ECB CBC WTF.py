import requests
from Crypto.Util.Padding import unpad

BASE = "https://aes.cryptohack.org/ecbcbcwtf"

def decrypt_block(block_hex):
    url = f"{BASE}/decrypt/{block_hex}/"
    r = requests.get(url)
    return bytes.fromhex(r.json()['plaintext'])

def get_ciphertext():
    r = requests.get(f"{BASE}/encrypt_flag/")
    ct = bytes.fromhex(r.json()["ciphertext"])
    return ct

def xor(a, b):
    return bytes(x ^ y for x, y in zip(a, b))

cipher = get_ciphertext()
iv = cipher[:16]
ct_blocks = [cipher[i:i+16] for i in range(16, len(cipher), 16)]

plaintext = b""
prev = iv
for c in ct_blocks:
    decrypted = decrypt_block(c.hex())
    plaintext += xor(decrypted, prev)
    prev = c

try:
    print(unpad(plaintext, 16).decode())
except ValueError:
    print("Unpad failed, raw output:", plaintext)
