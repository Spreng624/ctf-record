#!/usr/local/bin/python
from random import choice
from hashlib import sha256
from string import ascii_letters, digits

from secret import flag
from Crypto.Util.number import getPrime, isPrime, inverse
from hashlib import sha256
from random import randint


class Elgamal:
    def __init__(self):
        self.q, self.g = self.gen()
        self.d = randint(0, self.q - 2)
        self.y = pow(self.g, self.d, self.q)

    def gen(self):
        # 原根生成函数
        q = 8867984692712162589394753592684462893849721383808359270870591946309591420901509987341888487540800853389811701998166292427185543648905432008953442556844003

        while True:
            # q = getPrime(512)
            p = 2 * q + 1
            if isPrime(p):
                g = randint(2, p - 1)
                if (pow(g, 2, p) != 1) & (pow(g, q, p) != 1):
                    break
        return q, g

    def Hash(self, msg):
        # 哈希函数
        return int(sha256(msg).hexdigest(), 16)

    def Sign(self, msg):
        # 签名函数
        m = self.Hash(msg)
        phi = self.q - 1

        while True:
            k = getPrime(512)
            if k < phi:
                break

        r = pow(self.g, k, self.q)
        s = ((m - self.d * r) * inverse(k, phi)) % (phi)
        return (r, s)

    def Verity(self, msg, Signature):
        # 验签函数
        m = self.Hash(msg)
        r, s = Signature

        A = (pow(self.y, r, self.q) * pow(r, s, self.q)) % self.q
        B = pow(self.g, m, self.q)

        if A == B:
            return True
        else:
            return False


def proof_of_work():
    proof = "".join([choice(ascii_letters + digits) for _ in range(20)])
    _hexdigest = sha256(proof.encode()).hexdigest()
    print(f"[+] sha256(XXXX+{proof[4:]}) == {_hexdigest}")
    x = input("[+] Plz tell me XXXX: ")
    if len(x) != 4 or sha256((x + proof[4:]).encode()).hexdigest() != _hexdigest:
        return False
    return True


assert proof_of_work()

S = Elgamal()
print(f"My Public Key (q,g,y):{S.q, S.g, S.y}")
msg = (b"Welcome_to_0xGame2024_Crypto").hex()

print(f"The input msg : {msg}")
msg = bytes.fromhex(msg)
r, s = S.Sign(msg)
print(f"And the msg signatue (r,s):{r,s}")

print("Now, it's your turn to help me sign something")
msg_ = bytes.fromhex(input("[+] Give me your message:\n>"))
r_ = int(input("[+] Give me your r:\n>"))
s_ = int(input("[+] Give me your s:\n>"))

if S.Verity(msg_, (r_, s_)) and (msg_ == msg):
    print("It looks like you know how to verify the signature. Try getting the flag.")
elif S.Verity(msg_, (r_, s_)):
    print(f"flag : {flag}")
else:
    print("Is something wrong ?")
