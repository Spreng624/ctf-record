import math

hex_numbers = [
    0xC9,
    0xB6,
    0x5C,
    0xCE,
    0xF8,
    0xEE,
    0x8E,
    0xA2,
    0x33,
    0x36,
    0x34,
    0x63,
    0x37,
    0x32,
    0x36,
    0x64,
    0x38,
    0x37,
    0x65,
    0x33,
    0x62,
    0x33,
    0x63,
    0x64,
    0x36,
    0x39,
    0x64,
    0x34,
    0x64,
    0x30,
    0x62,
    0x38,
    0x2A,
    0x7A,
    0x7C,
    0x3B,
    0x85,
    0x33,
    0x6D,
    0xD3,
]


class unsigned_int32:
    def __init__(self, num: int):
        self.num = abs(num) % (2**32)

    def __add__(self, other):
        if isinstance(other, unsigned_int32):
            other = other.num
        return unsigned_int32(self.num + other)

    def __sub__(self, other):
        if isinstance(other, unsigned_int32):
            other = other.num
        return unsigned_int32(self.num - other)

    def __mul__(self, other):
        if isinstance(other, unsigned_int32):
            other = other.num
        return unsigned_int32(self.num * other)

    def __lshift__(self, other):
        if isinstance(other, unsigned_int32):
            other = other.num
        return unsigned_int32(self.num << other)

    def __rshift__(self, other):
        if isinstance(other, unsigned_int32):
            other = other.num
        return unsigned_int32(self.num >> other)

    def __and__(self, other):
        return unsigned_int32(self.num & other.num)

    def __xor__(self, other):
        return unsigned_int32(self.num ^ other.num)


def tran_int(nums: list[int]) -> int:
    num = 0
    i = 0
    while i < len(nums):
        num += nums[i] * (256**i)
        i += 1
    return num


# def tran_int(nums: list[int]) -> int:
#     num = 0
#     i = 0
#     while i < len(nums):
#         num += nums[-1 - i] * (256**i)
#         i += 1
#     return num


def tran_hexlist(num: int):
    hex_numbers = []
    while num > 0:
        hex_numbers.append(num & 0xFF)
        num >>= 8
    return hex_numbers


def tea_dec(v: tuple[int, int], k: list):
    v0, v1 = v
    v0 = unsigned_int32(v0)
    v1 = unsigned_int32(v1)
    delta = -1640531527
    sum = 32 * delta

    for _ in range(32):
        v1 -= ((v0 << 4) + k[2]) ^ (v0 + sum) ^ ((v0 >> 5) + k[3])
        v0 -= ((v1 << 4) + k[0]) ^ (v1 + sum) ^ ((v1 >> 5) + k[1])
        sum -= delta
        print(f"v0: {hex(v0.num)} v1: {hex(v1.num)} sum: {hex(sum)}")

    return v0, v1


keys = [2, 0, 2, 4]
decrypted_hex = []

for i in range(5):
    v = hex_numbers[i * 8 : i * 8 + 8]
    v = tran_int(v[0:4]), tran_int(v[4:8])
    v0, v1 = tea_dec(v, keys)
    decrypted_hex += tran_hexlist(v0.num)
    decrypted_hex += tran_hexlist(v1.num)

flag = ""
for i in range(0, len(decrypted_hex)):
    value = decrypted_hex[i]
    flag += chr(value)
print(f"Flag: {flag}")
