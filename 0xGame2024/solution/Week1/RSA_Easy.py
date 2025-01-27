from Crypto.Util.number import *
from hashlib import md5
from random import randint
from gmpy2 import invert, gcd


# Hash Function:
def MD5(m):
    return md5(str(m).encode()).hexdigest()


N, e = 689802261604270193, 620245111658678815
c = 289281498571087475

p, q = 823642439, 837502087
phi = (p - 1) * (q - 1)

d = inverse(e, phi)
print(f"d = {d}")
m = pow(c, d, N)  # 密文

flag = "0xGame{" + MD5(m) + "}"
print(flag)
