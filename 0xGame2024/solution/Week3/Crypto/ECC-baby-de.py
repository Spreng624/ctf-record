from Crypto.Cipher import AES
from hashlib import md5


def MD5(m):
    return md5(str(m).encode()).digest()


k = 1670419487
M_x = 944662661  # M = C - G_ * k = (944662661 : 635214115 : 1)
Cipher = AES.new(MD5(M_x), AES.MODE_ECB)
enc = "29bb47e013bd91760b9750f90630d8ef82130596d56121dc101c631dd5d88201a41eb3baa5aa958a6cd082298fc18418"
enc = bytes.fromhex(enc)
flag = Cipher.decrypt(enc)
print(flag.decode())  # 0xGame{0b0e28c2-b36d-d745-c0be-fcf0986f316a}
