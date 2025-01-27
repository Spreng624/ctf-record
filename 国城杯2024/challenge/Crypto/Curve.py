#sagemath
from Crypto.Util.number import *

def add(P, Q):
    (x1, y1) = P
    (x2, y2) = Q

    x3 = (x1*y2 + y1*x2) * inverse(1 + d*x1*x2*y1*y2, p) % p
    y3 = (y1*y2 - a*x1*x2) * inverse(1 - d*x1*x2*y1*y2, p) % p
    return (x3, y3)

def mul(x, P):
    Q = (0, 1)
    while x > 0:
        if x % 2 == 1:
            Q = add(Q, P)
        P = add(P, P)
        x = x >> 1
    return Q

p = 64141017538026690847507665744072764126523219720088055136531450296140542176327
a = 362
d = 7
e=0x10001

gx=bytes_to_long(b'D0g3xGC{*****************}')

PR.<y>=PolynomialRing(Zmod(p))
f=(d*gx^2-1)*y^2+(1-a*gx^2)
gy=int(f.roots()[0][0])

assert (a*gx^2+gy^2)%p==(1+d*gx^2*gy^2)%p

G=(gx,gy)

eG = mul(e, G)
print(eG)

#eG = (34120664973166619886120801966861368419497948422807175421202190709822232354059, 11301243831592615312624457443883283529467532390028216735072818875052648928463)