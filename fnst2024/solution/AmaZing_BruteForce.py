s = [
    0x08,
    0x05,
    0x0A,
    0x02,
    0x15,
    0x23,
    0x3E,
    0x36,
    0x3A,
    0x36,
    0x2F,
    0x55,
    0x31,
    0x58,
    0x3F,
    0x18,
]

key = [0x08 ^ ord("f"), 0x05 ^ ord("l"), 0x0A ^ ord("a"), 0x02 ^ ord("g")]
for i in range(16):
    print(chr(s[i] ^ key[i % 4]), end="")
# flag{JUST_D0_1T}