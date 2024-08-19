# encoded = '0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104'
# encoded = bytes.fromhex(encoded)
#
# flag_format = b'crypto{'
#
# key = [o1 ^ o2 for (o1, o2) in zip(encoded, flag_format)] + [ord("y")]
# flag = []
# key_len = len(key)
# for i in range(len(encoded)):
#     flag.append(encoded[i] ^ key[i % key_len])
# flag = "".join(chr(o) for o in flag)
#
# print(flag)
encoded = '0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104'
encoded = bytes.fromhex(encoded)

flag_format = b'crypto{'
for char in range(ord('a'), ord('z') + 1):
    key = [o1 ^ o2 for (o1, o2) in zip(encoded, flag_format)] + [char]
    flag = []
    key_len = len(key)
    for i in range(len(encoded)):
        flag.append(encoded[i] ^ key[i % key_len])

    flag = "".join(chr(o) for o in flag)
    print(f"'{chr(char)}': {flag}")
