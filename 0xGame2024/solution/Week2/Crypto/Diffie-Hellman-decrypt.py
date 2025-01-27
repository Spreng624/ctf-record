from string import ascii_letters, digits
from hashlib import sha256
from random import choice
from itertools import product
from Crypto.Util.number import isPrime, getPrime
from Crypto.Cipher import AES
from hashlib import md5
from Crypto.Util.Padding import unpad


def find_proof(proof, target_hash):
    dict_ = ascii_letters + digits
    for word in ("".join(combination) for combination in product(dict_, repeat=4)):
        if sha256((word + proof).encode()).hexdigest() == target_hash:
            return word
    return None


# 从用户那里获取proof和target_hash
proof = input("请输入proof: ")
target_hash = input("请输入target_hash: ")

# 打印出需要破解的哈希值
print(f"[+] sha256(XXXX+{proof}) == {target_hash}")

# 找到正确的XXXX
xxxx = find_proof(proof, target_hash)
if xxxx:
    print(f"找到的XXXX是: {xxxx}")
else:
    print("没有找到正确的XXXX")


q = int(input("请输入q: "))
g = int(input("请输入g: "))
Alice_PubKey = int(input("请输入Alice的公钥: "))

Bob_PriKey = 1234567890  # Bob私钥
Bob_PubKey = pow(g, Bob_PriKey, q)  # Bob的公钥
print(f"Bob的公钥是: {Bob_PubKey}")

ct_hex = input("把你的密文的十六进制字符串放这里")  # 加密后的密文的十六进制字符串
ct = bytes.fromhex(ct_hex)  # 将十六进制字符串转换为字节串

# 计算共享密钥
Share_Key = pow(Alice_PubKey, Bob_PriKey, q)

# 使用共享密钥的MD5哈希值作为AES解密的密钥
cipher = AES.new(md5(str(Share_Key).encode()).digest(), AES.MODE_ECB)

# 解密密文
pt = cipher.decrypt(ct)
print("解密的消息:", pt.decode())

# 去除填充
try:
    pt = unpad(pt, AES.block_size)
    print("解密的消息:", pt.decode())
except ValueError:
    print("解密失败，可能密钥错误或填充不正确。")
