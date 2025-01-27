#!/usr/local/bin/python
# 引入所需的库
from Crypto.Util.number import isPrime, getPrime  # 用于生成素数
from string import ascii_letters, digits  # 用于生成随机字符串
from Crypto.Cipher import AES  # AES加密库
from hashlib import sha256  # SHA-256哈希库
from random import randint  # 生成随机数
from random import choice  # 从列表中随机选择元素
from hashlib import md5  # MD5哈希库
from os import urandom  # 生成随机字节串


# 定义一个函数，用于计算MD5哈希值
def MD5(m):
    return md5(str(m).encode()).digest()


# 定义一个函数，用于生成Diffie-Hellman密钥交换所需的参数
def gen(bit_length):
    while True:
        q = getPrime(bit_length)  # 生成一个素数q
        p = 2 * q + 1  # 计算p，使得p也是素数
        if isPrime(p):  # 检查p是否为素数
            g = randint(2, p - 1)  # 生成一个随机数g
            if (pow(g, 2, p) != 1) & (pow(g, q, p) != 1):  # 确保g不是1也不是p-1
                break
    return q, g  # 返回生成的q和g


# 定义一个函数，用于工作量证明
def proof_of_work():
    proof = "".join(
        [choice(ascii_letters + digits) for _ in range(20)]
    )  # 生成一个20位的随机字符串
    _hexdigest = sha256(proof.encode()).hexdigest()  # 计算字符串的SHA-256哈希值
    print(f"[+] sha256(XXXX+{proof[4:]}) == {_hexdigest}")
    x = input("[+] Plz tell me XXXX: ")  # 用户输入前缀
    if (
        len(x) != 4 or sha256((x + proof[4:]).encode()).hexdigest() != _hexdigest
    ):  # 验证用户输入
        return False
    return True


# 执行工作量证明，确保程序不会继续执行直到用户通过验证
# assert proof_of_work()

# 生成Diffie-Hellman参数
q, g = gen(128)
print(f"Share (q,g) : {q,g}")

# Alice生成自己的私钥和公钥
Alice_PriKey = randint(1, q)
Alice_PubKey = pow(g, Alice_PriKey, q)
print(f"Alice_PubKey : {Alice_PubKey}")

# Bob提供他的公钥
Bob_PubKey = int(input("[+] Give me the Bob_PubKey\n> "))
print(f"Bob_PubKey : {Bob_PubKey}")

# Alice计算共享密钥
Share_Key = pow(Bob_PubKey, Alice_PriKey, q)

# 使用共享密钥的MD5哈希值作为AES加密的密钥
Cipher = AES.new(MD5(Share_Key), AES.MODE_ECB)

# 加密flag变量
ct = Cipher.encrypt("0xGame{Hello wOrld!}")

# 打印加密后的密文
print(f"Alice tell Bob : {ct.hex()}")
