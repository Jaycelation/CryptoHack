import requests
from binascii import unhexlify

BASE = "https://aes.cryptohack.org/symmetry"

resp = requests.get(f"{BASE}/encrypt_flag/")
full = resp.json()['ciphertext']
iv = full[:32]
ct_flag = full[32:]

resp = requests.get(f"{BASE}/encrypt/{ct_flag}/{iv}/")
pt_hex = resp.json()['ciphertext']
flag = bytes.fromhex(pt_hex).decode()
print("Flag:", flag)
