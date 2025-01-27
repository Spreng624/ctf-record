from Crypto.Util.number import *
from hashlib import md5
from random import randint


def MD5(m):
    return md5(str(m).encode()).hexdigest()


def CRT(a, n):
    N = 1
    for i in range(len(a)):
        N *= n[i]
    x = 0
    for i in range(len(a)):
        m = N // n[i]
        x += a[i] * m * inverse(m, n[i])
    return x % N


def attack(M, N):
    M = M % N
    ans = []
    for m in range(2, N):
        if pow(m, 2, N) == M:
            ans.append(m)
    return ans


N = 1022053332886345327
p, q = 970868179, 1052721013
e = 294200073186305890
c = 107033510346108389
phi = (p - 1) * (q - 1)

print(f"gcd(e, phi) = {GCD(e, phi)}")

D = inverse(e // 2, phi)
M = pow(c, D, N)
print(f"M = {M}")

# m1_list, m2_list = attack(M, p), attack(M, q)
# print(f"m1_list = {m1_list}")
# print(f"m2_list = {m2_list}")

m1_list = [215973055, 754895124]
m2_list = [215896886, 836824127]

for m1 in m1_list:
    for m2 in m2_list:
        m = CRT([m1, m2], [p, q])
        if pow(m, e, N) == c:
            print(f"0xGame{{{MD5(m)}}}")
