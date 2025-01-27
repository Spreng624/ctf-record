#!/usr/local/bin/python
from Crypto.Cipher import AES
from hashlib import md5

from string import ascii_letters, digits
from hashlib import sha256
from random import randint
from random import choice

import findProof


class Point:
    def __init__(self, x, y, curve, isInfinity=False):
        self.x = x % curve.p
        self.y = y % curve.p
        self.curve = curve
        self.isInfinity = isInfinity

    def __add__(self, other):
        return self.curve.add(self, other)

    def __mul__(self, other):
        return self.curve.multiply(self, other)

    def __rmul__(self, other):
        return self.curve.multiply(self, other)

    def __str__(self):
        return f"({self.x},{self.y})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.curve == other.curve


class Curve:
    def __init__(self, a, b, p):
        self.a = a % p
        self.b = b % p
        self.p = p

    def multiply(self, P: Point, k: int) -> Point:
        Q = P
        R = Point(0, 0, self, isInfinity=True)
        while k > 0:
            if (k & 1) == 1:
                R = self.add(R, Q)
            Q = self.add(Q, Q)
            k >>= 1
        return R

    def find_y(self, x):
        x = x % self.p
        y_squared = (pow(x, 3, self.p) + self.a * x + self.b) % self.p
        assert (
            pow(y_squared, (self.p - 1) // 2, self.p) == 1
        ), "The x coordinate is not on the curve"
        y = pow(y_squared, (self.p + 1) // 4, self.p)
        assert pow(y, 2, self.p) == (pow(x, 3, self.p) + self.a * x + self.b) % self.p
        return y

    def add(self, P: Point, Q: Point) -> Point:
        if P.isInfinity:
            return Q
        elif Q.isInfinity:
            return P
        elif P.x == Q.x and P.y == (-Q.y) % self.p:
            return Point(0, 0, self, isInfinity=True)
        if P.x == Q.x and P.y == Q.y:
            param = (3 * pow(P.x, 2, self.p) + self.a) * pow(2 * P.y, -1, self.p)
        else:
            param = (Q.y - P.y) * pow(Q.x - P.x, -1, self.p)
        Sx = (pow(param, 2, self.p) - P.x - Q.x) % self.p
        Sy = (param * ((P.x - Sx) % self.p) - P.y) % self.p
        return Point(Sx, Sy, self)


def getrandpoint(E):
    while True:
        try:
            g = randint(1, E.p)
            G = Point(g, E.find_y(g), E)
            break
        except:
            continue
    return G


def proof_of_work():
    proof = "".join([choice(ascii_letters + digits) for _ in range(20)])
    _hexdigest = sha256(proof.encode()).hexdigest()
    print(f"[+] sha256(XXXX+{proof[4:]}) == {_hexdigest}")
    x = input("[+] Plz tell me XXXX: ")
    if len(x) != 4 or sha256((x + proof[4:]).encode()).hexdigest() != _hexdigest:
        return False
    return True


def MD5(m):
    return md5(str(m).encode()).digest()


a = 10809567548006703521
b = 9981694937346749887
p = 25321837821840919771
E = Curve(a, b, p)

findProof.main()
G_x = int(input("[+] Give me the G_x\n> "))
G_y = int(input("[+] Give me the G_y\n> "))
G = Point(G_x, G_y, E)
print(f"[+] Share_G : {G}")

b = randint(1, E.p)  # Bob's private key
B = b * G  # Bob's public key
print(f"[+] Bob_PubKey : {B}")

A_x = int(input("[+] Give me the Alice_PubKey.x\n> "))
A_y = int(input("[+] Give me the Alice_PubKey.y\n> "))
A = Point(A_x, A_y, E)  # Alice's Public Key
print(f"[+] Alice_PubKey : {A}")

Share_Key = b * A
Cipher = AES.new(MD5(Share_Key.x), AES.MODE_ECB)
pt = Cipher.decrypt(bytes.fromhex(input("[+] Give me the ciphertext\n> ")))
print(f"[+] Bob get the flag : {pt.decode()}")
