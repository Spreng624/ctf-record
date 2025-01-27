from Crypto.Util.number import inverse
from random import getrandbits
from pwn import *


class RNG:
    def __init__(self, seed):
        self.mt = [0] * 624
        self.mt[0] = seed
        self.mti = 0
        for i in range(1, 624):
            self.mt[i] = self._int32(
                1812433253 * (self.mt[i - 1] ^ (self.mt[i - 1] >> 30)) + i
            )

    def _int32(self, x):
        """
        Convert a integer to a 32-bit integer."""
        return int(0xFFFFFFFF & x)

    def extract(self):
        if self.mti == 0:
            self.twist()
        y = self.mt[self.mti]
        y = y ^ y >> 11
        y = y ^ y << 7 & 2636928640
        y = y ^ y << 15 & 4022730752
        y = y ^ y >> 18
        self.mti = (self.mti + 1) % 624
        return self._int32(y)

    def twist(self):
        for i in range(0, 624):
            y = self._int32(
                (self.mt[i] & 0x80000000) + (self.mt[(i + 1) % 624] & 0x7FFFFFFF)
            )
            self.mt[i] = (y >> 1) ^ self.mt[(i + 397) % 624]

            if y % 2 != 0:
                self.mt[i] = self.mt[i] ^ 0x9908B0DF


def reverse_seed(x: int) -> int:
    x = (x - 1) * inverse(1812433253, 2**32) % 2**32
    x ^= x << 30 & 0xFFFFFFFF
    return x


def reverse_twist(twist):
    reverse_twist = [0] * 624
    for i in range(623, -1, -1):
        k = twist[i] ^ twist[(i + 397) % 624]
        if (k & 0x80000000) >> 31 == 1:  ##末位1和0判断
            k = k ^ 0x9908B0DF
            lowbit = 1
            highbit = (k & 0x40000000) >> 30
            reverse_twist[i] = highbit << 31
            reverse_twist[(i + 1) % 624] = (
                reverse_twist[(i + 1) % 624] + ((k & 0x3FFFFFFF) << 1) + lowbit
            )
            if i != 623:
                twist[(i + 1) % 624] = reverse_twist[(i + 1) % 624]
        elif (k & 0x80000000) >> 31 == 0:
            lowbit = 0
            highbit = (k & 0x40000000) >> 30
            reverse_twist[i] = highbit << 31
            reverse_twist[(i + 1) % 624] = (
                reverse_twist[(i + 1) % 624] + ((k & 0x3FFFFFFF) << 1) + lowbit
            )
            if i != 623:
                twist[(i + 1) % 624] = reverse_twist[(i + 1) % 624]
    return reverse_twist


def xorshift(y):
    y ^= y >> 18
    temp = y
    while temp:
        temp <<= 15
        temp &= 4022730752
        y ^= temp
    temp = y
    while temp:
        temp <<= 7
        temp &= 2636928640
        y ^= temp
    temp = y
    while temp:
        temp >>= 11
        y ^= temp
    return y


def test():
    result = []
    seed = getrandbits(32)
    print("Seed:", seed)
    rng = RNG(seed)
    mt = rng.mt.copy()
    for _ in range(624):
        result.append(rng.extract())

    mt_ = result.copy()
    # mt = input().split(", ")
    # mt = [int(i) for i in mt]

    for i in range(len(mt_)):
        mt_[i] = xorshift(mt_[i])

    if rng.mt == mt_:
        print("Success")
    else:
        print("Failed")

    # mt__ = untwist(mt_)
    mt__ = reverse_twist(mt_)
    if mt[1:] == mt__[1:]:
        print("Success")
    else:
        print("Failed")

    seed = reverse_seed(mt__[1])

    result_ = []
    rng = RNG(seed)
    for _ in range(624):
        result_.append(rng.extract())

    if result == result_:
        print("Success")
    else:
        print("Failed")


def main():
    result = io.recvuntil(b"\n", drop=True).decode().strip()
    result = io.recvuntil(b"\n", drop=True).decode().strip()
    result = result[1:-1]
    mt_ = result.split(", ")
    mt_ = [int(i) for i in mt_]

    for i in range(len(mt_)):
        mt_[i] = xorshift(mt_[i])

    mt__ = reverse_twist(mt_)
    seed = reverse_seed(mt__[1])
    print(str(seed).encode())

    io.sendlineafter(b"[+] seed = ?\n>", str(seed).encode())

    result = io.recvuntil(b"\n", drop=True).decode().strip()
    print(result)  # 0xGame{2569bd55-a14d-46d8-81f5-e1397e4be7bc}


ip = "118.195.138.159"
port = 10006
io = remote(ip, port)


if __name__ == "__main__":
    main()
