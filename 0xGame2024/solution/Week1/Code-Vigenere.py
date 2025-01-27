from os import urandom
from base64 import b64encode


def Encrypt(msg: str, key):
    Lenth = len(key)  # 获取密钥长度
    result = ""

    upper_base = ord("A")
    lower_base = ord("a")
    KEY = [ord(key.upper()[_]) - upper_base for _ in range(Lenth)]

    index = 0
    for m in msg:
        tmp_key = KEY[index % Lenth]
        # 非字母字符不加密
        if not m.isalpha():
            result += m
            continue

        # 大写字母加密
        if m.isupper():
            result += chr(upper_base + (ord(m) - upper_base + tmp_key) % 26)
        # 小写字母加密
        else:
            result += chr(lower_base + (ord(m) - lower_base + tmp_key) % 26)
        index += 1
    return result


flag = "0lCcop{oyd94092-g8mq-4963-88b6-4helrxdhm6q7}"

key1 = key2 = key3 = key4 = key5 = ""
for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/":
    if Encrypt(flag, "" + i + "0000")[1] == "x":
        key1 += i
    if Encrypt(flag, "0" + i + "000")[2] == "G":
        key2 += i
    if Encrypt(flag, "00" + i + "00")[3] == "a":
        key3 += i
    if Encrypt(flag, "000" + i + "0")[4] == "m":
        key4 += i
    if Encrypt(flag, "0000" + i + "")[5] == "e":
        key5 += i

print(key1, key2, key3, key4, key5)
print(Encrypt(flag, "3+yyP"))  # 0xGame{acb94092-e8bc-4963-88f6-4fcadbbfb6c7}
