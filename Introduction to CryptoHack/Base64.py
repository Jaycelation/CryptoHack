# In Python, after importing the base64 module with import base64, you can use the base64.b64encode() function. Remember to decode the hex first as the challenge description states.
import base64

str= '72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf'
bytes_data = bytes.fromhex(str)
encoded = base64.b64encode(bytes_data)
print(encoded)
