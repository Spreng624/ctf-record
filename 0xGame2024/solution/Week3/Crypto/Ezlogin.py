#!/usr/local/bin/python
from base64 import b64encode, b64decode
from Crypto.Cipher import AES
from datetime import datetime
from os import urandom
import json

# from secret import flag1, flag2
flag1 = "flag{ez_login_is_awesome}"
flag2 = "flag{ez_login_is_still_awesome}"

MENU = "\
+--------------+\n\
| [R] Regist   |\n\
| [L] Login    |\n\
| [F] Getflag  |\n\
+--------------+\n\
"

KEY = urandom(16)


def pad(data: bytes):
    l = 16 - len(data) % 16
    return data + bytes([l] * l)


def unpad(data: bytes):
    for i in range(1, data[-1] + 1):
        if data[-1] != data[-i]:
            print("Unpad error")
    return data[: -data[-1]]


def encrypt(data):
    IV = urandom(16)
    ENC = AES.new(KEY, AES.MODE_CBC, IV)
    result = ENC.encrypt(pad(data.encode()))
    return b64encode(IV + result).decode()


def decrypt(data):
    data = b64decode(data)
    IV, C = data[:16], data[16:]
    DEC = AES.new(KEY, AES.MODE_CBC, IV)
    result = DEC.decrypt(C)
    return unpad(result).decode()


def register():
    username = input("[+] username:\n>").strip()
    if "admin" in username:
        print("[!] Cannot register as admin user!")
    else:
        now = datetime.now()
        time = int(datetime.timestamp(now))
        cookie = {}
        cookie["username"] = username
        cookie["time"] = time
        print(f"[+] cookie : {encrypt(json.dumps(cookie))}")
    return


def login():
    cookie = input("[+] cookie:\n>").strip()

    try:
        cookie = decrypt(cookie.encode())
        cookie = json.loads(cookie)
        username = cookie["username"]
    except json.decoder.JSONDecodeError:
        print("[!] JSON Wrong")
        return 0
    except TypeError:
        print("[!] TypeError Wrong")
        return 0
    except:
        print("[!] Unkown Wrong")
        return 0

    if username == "admin":
        print(f"[+] Here is flag1 : {flag1}")
    else:
        print(f"[+] Welcome to 0xGame2024 Crypto! {username}")
    return 1


def getflag2():
    print(f"[+] Here is flag2 : {encrypt(flag2)}")
    return


print(MENU)
while True:
    choice = input("[+] Tell me your choice:\n>")
    if choice == "R":
        register()
    elif choice == "L":
        while True:
            if login():
                break
    elif choice == "F":
        getflag2()
    else:
        print("[!] Invalid choice")
