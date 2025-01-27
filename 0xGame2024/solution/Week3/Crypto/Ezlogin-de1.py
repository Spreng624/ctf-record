#!/usr/local/bin/python
from base64 import b64encode, b64decode
from datetime import datetime
import json


def pad(data: bytes):
    l = 16 - len(data) % 16  # PCKS7 padding length
    return data + bytes([l] * l)


def main():
    data = input("[+] Enter your cookie:\n>").strip()
    data = b64decode(data.encode())
    IV, C = data[:16], data[16:]  # 已知密文
    # {"username": "A
    # mqP7rMoHp/NewIwl AOhBvwHRXLTEl9MYRwo4sDjhYSTIB/xRv835m+T4Jc19BYU5SgZRvtronSEn4BA+rYCPRA==

    now = datetime.now()
    t = int(datetime.timestamp(now))
    for i in range(5, 15):
        time = t - i
        cookie = {}
        cookie["username"] = "admin"
        cookie["time"] = time
        P_ = pad(json.dumps(cookie).encode())  # 目标明文

        cookie = {}
        cookie["username"] = "Admin"
        cookie["time"] = time
        P = pad(json.dumps(cookie).encode())  # 已知明文
        print(forge(P, P_, C, IV))


def forge(P, P_, C, IV):
    P = bytearray(P)
    P_ = bytearray(P_)
    IV = bytearray(IV)
    IV[14] = P_[14] ^ IV[14] ^ P[14]
    IV = bytes(IV)
    return b64encode(IV + C).decode()


if __name__ == "__main__":
    main()
