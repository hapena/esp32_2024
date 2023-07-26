string = 'Hola'
print(string.encode())
string = b'Hola'
print(string)

b = bytes([72, 111, 108, 97])
b_str = b.decode()
print(b_str)
# 'Hola'