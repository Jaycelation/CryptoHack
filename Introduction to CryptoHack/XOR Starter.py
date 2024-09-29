# The Python pwntools library has a convenient xor() function that can XOR together data of different types and lengths. But first, you may want to implement your own function to solve this.
str_data = 'label'
result = ''

for i in str_data:
    result += chr(ord(i) ^ 13)

print(result)

