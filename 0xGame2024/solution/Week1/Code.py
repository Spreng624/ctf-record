# How to use mathematics to represent information?
from Crypto.Util.number import *
from base64 import b64decode

m0 = b"0xGame{73d7"
m1 = 60928972245886112747629873
m2 = "3165662D393339332D3034"
m3 = b"N2YwZTdjNGRlMX0="

m0 = m0
m1 = long_to_bytes(m1)
m2 = bytes.fromhex(m2)
m3 = b64decode(m3)

print((m0 + m1 + m2 + m3).decode())  # 0xGame{73d72f64-7656-11ef-9393-047f0e7c4de1}
