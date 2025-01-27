#!/usr/local/bin/python
from base64 import b64encode, b64decode
from Crypto.Cipher import AES
from datetime import datetime
from os import urandom
import json
from time import sleep
from pwn import *


KEY = urandom(16)
flag2 = "0xGame{c0ngr4t1ng_w1th_c0d3_4r3_1n_th3_w0rld}"  # 32 <= length < 48
ip = "118.195.138.159"
port = 10005
io = remote(ip, port)


def pad(data: bytes):
    l = 16 - len(data) % 16  # PCKS7 padding length
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


def login(data):
    data = data.encode()
    data = b64decode(data)
    IV, C = data[:16], data[16:]
    DEC = AES.new(KEY, AES.MODE_CBC, IV)
    data = DEC.decrypt(C)
    if data[-1] > 16:
        return False
    for i in range(1, data[-1] + 1):
        if data[-1] != data[-i]:
            return False
    return True


def main():
    # data = input("[+] Enter your cookie:\n>").strip()

    # 输出F
    io.sendlineafter(b"Tell me your choice:\n>", b"F")
    # 接收flag2
    data = io.recvuntil(b"\n", drop=True).decode().strip()
    data = data.split("Here is flag2 :")[1].strip()
    print(f"[+] Here is flag2: {data}")
    data = b64decode(data.encode())
    # 输出L
    io.sendlineafter(b"Tell me your choice:\n>", b"L")

    P = bytearray(0)
    for i in range(1, 3):
        P += explode(data, i)
        print(P)
    P = bytes(P).decode()
    print(P)  # 0xGame{6e02937e-634d-4f6f-8ef6-e5f387006cde}


def explode(data: bytes, block_num: int) -> bytearray:
    P = bytearray(16)  # 记录明文
    B = bytearray(16)  # 记录初步解密的块
    for i in range(1, 17):
        print("            ", end="\r")
        print(round(100 * (i - 1 + block_num * 16) / 48, 2), "%", end="\r")
        for byte in range(256):
            IV_ = bytearray(16)
            if block_num == 0:
                IV = data[:16]
                for j in range(16):
                    IV_[j] = IV[j]
                for j in range(1, i):
                    IV_[-j] = B[-j] ^ i
                IV_[-i] = byte
                IV_ = bytes(IV_)
                data_ = IV_ + data[16:32]
            elif block_num == 1:
                IV = data[16:32]
                for j in range(16):
                    IV_[j] = IV[j]
                for j in range(1, i):
                    IV_[-j] = B[-j] ^ i
                IV_[-i] = byte
                IV_ = bytes(IV_)
                data_ = IV_ + data[32:48]
            elif block_num == 2:
                IV = data[32:48]
                for j in range(16):
                    IV_[j] = IV[j]
                for j in range(1, i):
                    IV_[-j] = B[-j] ^ i
                IV_[-i] = byte
                IV_ = bytes(IV_)
                data_ = IV_ + data[48:64]
            else:
                return None
            if put(b64encode(data_)):
                B[-i] = IV_[-i] ^ i
                P[-i] = IV[-i] ^ B[-i]
                break
    return P


def put(try_data):
    # 输出try_data
    io.sendlineafter(b"cookie:\n>", try_data)
    # 接受信息
    response = io.recvline()
    if b"Unkown Wrong" in response:
        return False
    else:
        print(response)
        return True

    # if login(try_data):
    #     return True
    # else:
    #     return False


if __name__ == "__main__":
    main()
