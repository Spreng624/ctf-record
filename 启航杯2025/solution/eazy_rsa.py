# -*- coding: utf-8 -*-
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64


private_key = b"""
-----BEGIN RSA PRIVATE KEY-----\n
MIICWwIBAAKBgQDIMXWdJOp5N7utubIOO0PmH7izlWzWT5g1LZ7O/c2klWIRuu1D\n
JFzAHT/h3/Rx1JU3/NSY9g0E0ETZerI9PaEUNRIooCZm3Uy3LAPybVIOHpOP4bZ8\n
L2I/GIf4i/Yt8MzLk/7r6au5pFh+ifl8G/ce6nSgh5LWs/jpjOv61pYsWwIDAQAB\n
AoGAA4uAqiozrrbSb3aY1RCumJ4aLq/oL/lT2Ck5JTAwWog8ptS5C9XSgKJj9bN6\n
CCP8CnRDLXw56cpoVbOLAXOcbQ+gga/V0SMNeyDsc7Rtk9psRH+BgnxdsL24KOQf\n
x7qGNoWUqRCHZ7qafRbu0yGOkeS8Mi3EDr2iYedIDzOSW40CQQDOqgQTfZHjt1bV\n
4b5UWFP/N8C4gaoB13xnfE5hh15keiQta2unXvCxvaOdYD1KuOIq9NLP7Uzl05/5\n
5GXxx6avAkEA9/v7cYaJHoHQTyrHQrdEGrMSYcmA6o1+jDpoCPmY4kHg6Tz+8uR/\n
RGXCdJ0ztBSOTP2r+Y1huZpqL6jzR4KAFQJAf/L06RhCPajh4zOLQe8ZuhZLhDAL\n
EG7YP73PTUShJTYVteUe1pXKEVEmviW6bMvAgvXmmwMBK/10uyM0FpgUUwJASjSq\n
Akeq4mkgB4Cajdk/VOn+9yoQHJ/onVeg6AagfBwQjFrHQ7Gib7ovnSupXBrGlj1W\n
Z9+pvZt6aPaajex8HQJAXgHPmgnnZ/pjoAHVC65FOQS6Iw7yDjmrh5FI0ZAs1itB\n
OOiZbvpiuVaOu/QDhcD//QCvlCNDwsGobYjTxVr6kg==\n
-----END RSA PRIVATE KEY-----
"""


encrypted_message = "W3QljW92bNcoS6T7RcLQOlwnGk4Pl3YxLrx5UU+jyfh9yMjC0tOSZxcWjy4woZ2YKf+BlSFZN4hwbUeEF2k/RkmO3Ml5946X++cxnsgbkTP8IkLtmfR9O3tyOTvw3qcUW99aQX63aM0ha4QY1QCvyya7Tvm2jgy00zIF5cByHXM="


def decrypt_message(encrypted_message, private_key):
    key = RSA.import_key(private_key)
    cipher = PKCS1_OAEP.new(key)
    decrypted_message = cipher.decrypt(base64.b64decode(encrypted_message)).decode()
    return decrypted_message


decrypted = decrypt_message(encrypted_message, private_key)
print("解密后的消息:")
print(decrypted)
