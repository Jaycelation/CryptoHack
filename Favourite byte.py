encoded = bytes.fromhex('73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d')

def decode(s):
    return ''.join([chr(s ^ a) for a in encoded])

for i in range(0, 127):
    if 'crypto' in decode(i):
        print(decode(i))