# Python's PyCryptodome library implements this with the methods bytes_to_long() and long_to_bytes(). You will first have to install PyCryptodome and import it with from Crypto.Util.number import *. For more details check the FAQ.
from Crypto.Util.number import *

flag = 11515195063862318899931685488813747395775516287289682636499965282714637259206269
print(long_to_bytes(flag))