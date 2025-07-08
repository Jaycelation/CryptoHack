import requests

url = 'http://aes.cryptohack.org/block_cipher_starter'
req = requests.get(f"{url}/encrypt_flag")
data = req.json()

print(data)
c = data["ciphertext"]
r = requests.get(f"{url}/decrypt/{c}")

data = r.json()
print(data)
p = data["plaintext"]

print(bytes.fromhex(p))