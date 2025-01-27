#!/usr/local/bin/python

from hashlib import sha256


from Crypto.Util.number import getPrime, isPrime, inverse
from hashlib import sha256
from random import randint
import findProof


def Hash(msg):
    # 哈希函数
    return int(sha256(msg).hexdigest(), 16)


def forge_signature(q, m, m_, r, s):
    m = Hash(m)
    m_ = Hash(m_)
    phi = q - 1
    u = (m_ * inverse(m, phi)) % phi
    s_ = (s * u) % phi
    r_ = CRT(r * u, r, phi, q)
    return (r_, s_)


def CRT(r1, r2, p1, p2):
    """使用中国剩余定理求解"""
    M = p1 * p2
    M1 = p2
    M2 = p1

    r = (r1 * M1 * inverse(M1, p1) + r2 * M2 * inverse(M2, p2)) % M
    return r


if __name__ == "__main__":
    findProof.main()

    q = int(input("Enter q: "))
    msg = input("Enter message: ")
    msg = bytes.fromhex(msg)
    r = int(input("Enter r: "))
    s = int(input("Enter s: "))

    msg_ = (b"0xGame2024_Crypto_is_a_great_game").hex()
    print(f"msg_: {msg_}")

    msg_ = bytes.fromhex(msg_)
    r_, s_ = forge_signature(q, msg, msg_, r, s)
    print(f"r_: {r_}")
    print(f"s_: {s_}")
