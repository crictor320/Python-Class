"""
Learn about bytes.

Bytes are similar to str type, but they are a sequence of bytes instead of Unicode code points.

Use for raw binary data, fixed-width, single-byte encoding: ASCII

Use the byte() constructor
"""

d = b'data'
print(d, type(d))

# split the bytes using splot() method
info = b'some bytes'
print(info.split())

# Encoding: alt + 162 = ó
message = "Vamos al zoológico"
print(message)
data = message.encode("utf-8") #encode to recognize the ó
print(data)
messagedecode = data.decode("utf-8") #decode back to original
print(messagedecode)