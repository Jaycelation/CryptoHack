import requests
from binascii import unhexlify, hexlify

r = requests.get('https://aes.cryptohack.org/flipping_cookie/get_cookie/')
cookie = r.json()['cookie']
iv = cookie[:32]
ciphertext = cookie[32:]

orig = b"admin=False;expiry="
target = b"admin=True;expiry="

iv_bytes = bytearray(unhexlify(iv))
for i in range(len("admin=True;")):
    iv_bytes[i] ^= orig[i] ^ target[i]

new_iv = hexlify(bytes(iv_bytes)).decode()

check_url = f'https://aes.cryptohack.org/flipping_cookie/check_admin/{ciphertext}/{new_iv}/'
res = requests.get(check_url)
print(res.text)
