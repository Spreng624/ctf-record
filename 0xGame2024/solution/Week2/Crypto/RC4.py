#!/usr/local/bin/python
from os import urandom
from random import choice
from hashlib import sha256
from string import ascii_letters, digits


def KSA(key: bytes):
    keylength = len(key)

    S = [i for i in range(256)]

    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % keylength]) % 256
        S[i], S[j] = S[j], S[i]  # swap

    return S


def PRGA(S):
    i = 0
    j = 0
    while True:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]  # swap

        K = S[(S[i] + S[j]) % 256]
        yield K


def RC4(key: bytes):
    S = KSA(key)
    return PRGA(S)


def Encrypt(plaintext, keystream):
    if type(plaintext) == bytes:
        pt = plaintext
    else:
        pt = bytes.fromhex(plaintext)

    result = b""
    for i in pt:
        result += bytes([i ^ next(keystream)])
    return result.hex()


def proof_of_work():
    proof = "".join([choice(ascii_letters + digits) for _ in range(20)])
    _hexdigest = sha256(proof.encode()).hexdigest()
    print(f"[+] sha256(XXXX+{proof[4:]}) == {_hexdigest}")
    x = input("[+] Plz tell me XXXX: ")
    if len(x) != 4 or sha256((x + proof[4:]).encode()).hexdigest() != _hexdigest:
        return False
    return True


if __name__ == "__main__":
    assert proof_of_work()
    KEY = urandom(8)
    keystream = RC4(KEY)

    m = "0xGame{Hello-World-This-Is-A-Very-long-flag}".encode("utf-8").hex()
    c = Encrypt(m, keystream)
    print("[+] Here are the encrypt result:")
    print(f"c = {c}")

    keystream = RC4(KEY)

    flag = "0xGame{Hey-Man}".encode("utf-8").hex()
    print(f"flag = {Encrypt(flag, keystream)}")
