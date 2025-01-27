#!/usr/local/bin/python
from random import getrandbits

# from secret import flag


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


result = []
seed = getrandbits(32)
rng = RNG(seed)
for _ in range(624):
    result.append(rng.extract())
print(f"[+] result:")
print(result)
print(f"[+] seed = ?")
try:
    seed_ = int(input(">"))
    # if seed_ == seed : print(f'[+] flag： {flag}')
except:
    print(f"[!] Error")
