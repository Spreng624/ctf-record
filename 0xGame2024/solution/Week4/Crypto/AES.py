#!/usr/local/bin/python
from secret import flag
from os import urandom


class GF:
    def __init__(self, value):
        if type(value) == int:
            self.value = [(value // (3**i)) % 3 for i in range(5)]
        elif type(value) == list and len(value) == 5:
            self.value = value
        else:
            assert False, "Wrong input to the constructor"

    def __str__(self):
        return f"GF({self.to_int()})"

    def __repr__(self):
        return str(self)

    def __hash__(self):
        return hash(tuple(self.value))

    def __eq__(self, other):
        assert type(other) == GF
        return self.value == other.value

    def __add__(self, other):
        assert type(other) == GF
        return GF([(x + y) % 3 for x, y in zip(self.value, other.value)])

    def __sub__(self, other):
        assert type(other) == GF
        return GF([(x - y) % 3 for x, y in zip(self.value, other.value)])

    def __mul__(self, other):
        assert type(other) == GF

        arr = [0 for _ in range(9)]
        for i in range(5):
            for j in range(5):
                arr[i + j] = (arr[i + j] + self.value[i] * other.value[j]) % 3

        # Modulus: x^5 + 2*x + 1
        for i in range(8, 4, -1):
            arr[i - 4] = (arr[i - 4] - 2 * arr[i]) % 3
            arr[i - 5] = (arr[i - 5] - arr[i]) % 3

        return GF(arr[:5])

    def __pow__(self, other):
        assert type(other) == int
        base, ret = self, GF(1)
        while other > 0:
            if other & 1:
                ret = ret * base
            other >>= 1
            base = base * base
        return ret

    def inverse(self):
        return self**241

    def __div__(self, other):
        assert type(other) == GF
        return self * other.inverse()

    def to_int(self):
        return sum([self.value[i] * (3**i) for i in range(5)])


SBOX, INV_SBOX = dict(), dict()
for i in range(3**5):
    v = GF(23) + (GF(0) if i == 0 else GF(i).inverse())
    SBOX[GF(i)] = v
    INV_SBOX[v] = GF(i)


class BlockCipher:
    def __init__(self, key: bytes, rnd: int):
        assert len(key) == 9
        sks = [GF(b) for b in key]
        for i in range(rnd * 9):
            sks.append(sks[-1] + SBOX[sks[-9]])
        self.subkeys = [sks[i : i + 9] for i in range(0, (rnd + 1) * 9, 9)]
        self.rnd = rnd

    def _add_key(self, l1, l2):
        return [x + y for x, y in zip(l1, l2)]

    def _sub_key(self, l1, l2):
        return [x - y for x, y in zip(l1, l2)]

    def _sub(self, l):
        return [SBOX[x] for x in l]

    def _sub_inv(self, l):
        return [INV_SBOX[x] for x in l]

    def _shift(self, b):
        return [b[0], b[1], b[2], b[4], b[5], b[3], b[8], b[6], b[7]]

    def _shift_inv(self, b):
        return [b[0], b[1], b[2], b[5], b[3], b[4], b[7], b[8], b[6]]

    def _mix(self, b):
        b = b[:]  # Copy
        for i in range(3):
            x = GF(7) * b[i] + GF(2) * b[3 + i] + b[6 + i]
            y = GF(2) * b[i] + b[3 + i] + GF(7) * b[6 + i]
            z = b[i] + GF(7) * b[3 + i] + GF(2) * b[6 + i]
            b[i], b[3 + i], b[6 + i] = x, y, z
        return b

    def _mix_inv(self, b):
        b = b[:]  # Copy
        for i in range(3):
            x = GF(86) * b[i] + GF(222) * b[3 + i] + GF(148) * b[6 + i]
            y = GF(222) * b[i] + GF(148) * b[3 + i] + GF(86) * b[6 + i]
            z = GF(148) * b[i] + GF(86) * b[3 + i] + GF(222) * b[6 + i]
            b[i], b[3 + i], b[6 + i] = x, y, z
        return b

    def encrypt(self, inp: bytes):
        assert len(inp) == 9
        b = [GF(x) for x in inp]

        b = self._add_key(b, self.subkeys[0])
        for i in range(self.rnd):
            b = self._sub(b)
            b = self._shift(b)
            if i < self.rnd - 1:
                b = self._mix(b)
            b = self._add_key(b, self.subkeys[i + 1])

        return bytes([x.to_int() for x in b])

    def decrypt(self, inp: bytes):
        assert len(inp) == 9
        b = [GF(x) for x in inp]

        for i in reversed(range(self.rnd)):
            b = self._sub_key(b, self.subkeys[i + 1])
            if i < self.rnd - 1:
                b = self._mix_inv(b)
            b = self._shift_inv(b)
            b = self._sub_inv(b)
        b = self._sub_key(b, self.subkeys[0])

        return bytes([x.to_int() for x in b])


MENU = "\
+--------------+\n\
| [E] Encrypt  |\n\
| [F] Getflag  |\n\
+--------------+\n\
"

key = urandom(9)
cipher = BlockCipher(key, 3)

print(MENU)
while True:
    choice = input("[+] choice:\n>")

    if choice == "E":
        pt = bytes.fromhex(input("[+] encrypt:\n>"))
        ct = cipher.encrypt(pt)
        print(f"[+] result: {ct.hex()}")

    if choice == "F":
        guess = bytes.fromhex(input("[+] guess:\n>"))
        if guess == key:
            print(f"[+] flag: {flag}")
            exit()
        else:
            print(f"[!] Wrong")
