#!/usr/local/bin/python
from os import urandom
from hashlib import sha256
from random import choice, getrandbits
from string import ascii_letters, digits
from Crypto.Util.number import getPrime, inverse, bytes_to_long


def challenge0(m):
    p = getPrime(150)
    q = getPrime(150)
    N = p * q
    e = 3
    c = pow(m, e, N)
    return (N, e, c)


def challenge1(m):
    p = getPrime(64)
    q = getPrime(64)
    N = p * q
    e = 0x10001
    dp = inverse(e, p - 1)
    c = pow(m, e, N)
    return (N, e, c, dp)


def challenge2(m):
    p = getPrime(64)
    q = getPrime(64)
    N = p * q
    phi = (p - 1) * (q - 1)
    d = getPrime(21)
    e = inverse(d, phi)
    c = pow(m, e, N)
    return (N, e, c)


def challenge3(m):
    p = getPrime(64)
    q = getPrime(64)
    N = p * q
    e = getPrime(127)
    c = pow(m, e, N)
    e_ = getPrime(127)
    c_ = pow(m, e_, N)
    return (N, e, c, e_, c_)


def proof_of_work():
    proof = "".join([choice(ascii_letters + digits) for _ in range(20)])
    _hexdigest = sha256(proof.encode()).hexdigest()
    print(f"[+] sha256(XXXX+{proof[4:]}) == {_hexdigest}")
    x = input("[+] Plz tell me XXXX: ")
    if len(x) != 4 or sha256((x + proof[4:]).encode()).hexdigest() != _hexdigest:
        return False
    return True


def choice_(num):
    if num not in [0, 1, 2, 3]:
        return
    global scores
    m = getrandbits(96)

    match num:
        case 0:
            print(challenge0(m))
        case 1:
            print(challenge1(m))
        case 2:
            print(challenge2(m))
        case 3:
            print(challenge3(m))

    print("[+] input answer:")
    m_ = int(input(">"))
    scores[num] = m_ == m
    score_ = sum(scores)
    print(f"[+] score:{score_}")

    if score_ == 4:
        print(f"[+] flag")
        exit()


# assert proof_of_work()
scores = [0, 0, 0, 0]
while True:
    print("[+] input choice:")
    choice_(int(input(">")))
