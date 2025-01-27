from Crypto.Util.number import bytes_to_long, long_to_bytes
from numpy import eye, matrix
from random import randint

# import fpylll

flag = "0xGame{12-12431-1423-121672}".encode("utf-8")
assert len(flag) % 4 == 0
Length = len(flag) // 4

Noise = [[randint(1, pow(2, 90)) for _ in range(4)] for _ in range(4)]  # 4*4 matrix

Noise[0] = [bytes_to_long(flag[i * Length : (i + 1) * Length]) for i in range(4)]
M = matrix(Noise)


def Orthogonal_Matrix(n, p):
    up = matrix(eye(n, dtype=int))  # upper triangular matrix
    low = matrix(eye(n, dtype=int))  # lower triangular matrix
    for i in range(n - 1):
        for j in range(i + 1, n):
            up[i, j] = randint(1, p)
            low[j, i] = randint(1, p)
    return up * low


C = Orthogonal_Matrix(4, 65537)

print((C * M).tolist())
"""
[
    [
        1849784703482951012865152264025674575,
        2664848085955925754350117767673627932,
        2099783527396520151610274180590854166,
        1020558595577301617108111920545804527,
    ],
    [
        1207449566811121614020334020195802372,
        1954621976999112878661150903673543232,
        1326050406731534201574943690688237338,
        1361813208094227445768111591959011963,
    ],
    [
        888810907577479776819993141014777624,
        1216302736807928240875874427765340645,
        1027359437421599069599327712873719567,
        238961447144792739830554790892164336,
    ],
    [
        60622164517940943037274386912282,
        82958508138755168576836012717468,
        70072118066826856564329627650828,
        16296740862142507745322242235326,
    ],
]
"""
Noise = [
    [
        58596440058654765094286903,
        69377248846131264731819316,
        60910008503494441471652194,
        58497746791226042414948989,
    ]
]

# 假设 Length 是 8
Length = 8

# 还原 flag
flag = b""
for noise in Noise[0]:
    flag += long_to_bytes(noise)

# 将字节字符串转换为 ASCII 字符串
flag = flag.decode("latin-1")  # 或者使用其他适当的编码

print(flag)  # 0xGame{04679c42-2bc1-42b2-b836-1b0ca542f36b}
