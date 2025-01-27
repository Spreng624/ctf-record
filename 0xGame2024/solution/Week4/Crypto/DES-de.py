#!/usr/local/bin/python
from os import urandom

from functools import reduce
from operator import add
from random import Random
from itertools import product

__s_box = [
    [
        [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
        [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
        [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
        [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13],
    ],
    [
        [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
        [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
        [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
        [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9],
    ],
    [
        [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
        [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
        [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
        [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12],
    ],
    [
        [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
        [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
        [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
        [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14],
    ],
    [
        [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
        [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
        [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
        [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3],
    ],
    [
        [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
        [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
        [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
        [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13],
    ],
    [
        [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
        [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
        [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
        [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12],
    ],
    [
        [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
        [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
        [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
        [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11],
    ],
]

__ep = [
    31,
    0,
    1,
    2,
    3,
    4,
    3,
    4,
    5,
    6,
    7,
    8,
    7,
    8,
    9,
    10,
    11,
    12,
    11,
    12,
    13,
    14,
    15,
    16,
    15,
    16,
    17,
    18,
    19,
    20,
    19,
    20,
    21,
    22,
    23,
    24,
    23,
    24,
    25,
    26,
    27,
    28,
    27,
    28,
    29,
    30,
    31,
    0,
]


def EP(data):
    return [data[x] for x in __ep]


def bytes2bin(m):
    return [int(i) for i in bin(int(m.hex(), 16))[2:].zfill(8 * len(m))]


def bin2bytes(m):
    return int("".join([str(i) for i in m]), 2).to_bytes(length=len(m) // 8)


reversed_p = [
    8,
    16,
    22,
    30,
    12,
    27,
    1,
    17,
    23,
    15,
    29,
    5,
    25,
    19,
    9,
    0,
    7,
    13,
    24,
    2,
    3,
    28,
    10,
    18,
    31,
    11,
    21,
    6,
    4,
    26,
    14,
    20,
]


def reverseP(data):
    return [data[i] for i in reversed_p]


def intToBin(m):
    return [int(i) for i in bin(m)[2:].zfill(6)]


def binToInt(m):
    return int("".join([str(i) for i in m]), 2)


def S_box_(data, n):
    row = data[0] * 2 + data[5]
    col = reduce(add, [data[j] * (2 ** (4 - j)) for j in range(1, 5)])
    return [int(x) for x in format(__s_box[n][row][col], "04b")]


# 差分攻击
def Diff_attack(tables, x_list1, y_list1, x_list2, y_list2, N):
    Key1 = [set({}) for _ in range(8)]
    for t in range(N):
        for i in range(8):
            # 相邻的x做差分
            alpha = binToInt(x_list1[t][i * 6 : (i + 1) * 6]) ^ binToInt(
                x_list1[t + 1][i * 6 : (i + 1) * 6]
            )
            beta = binToInt(y_list1[t][i * 4 : i * 4 + 4]) ^ binToInt(
                y_list1[t + 1][i * 4 : i * 4 + 4]
            )
            table = tables[i]
            zSet = table[(alpha, beta)]  # 读表，得到z的范围
            kSet = set({})
            for z in zSet:
                kSet.add(z ^ alpha)
            if Key1[i]:
                Key1[i] &= kSet
            else:
                Key1[i] = kSet

    Key2 = [set({}) for _ in range(8)]
    for t in range(N):
        for i in range(8):
            alpha = binToInt(x_list2[t][i * 6 : (i + 1) * 6]) ^ binToInt(
                x_list2[t + 1][i * 6 : (i + 1) * 6]
            )
            beta = binToInt(y_list2[t][i * 4 : i * 4 + 4]) ^ binToInt(
                y_list2[t + 1][i * 4 : i * 4 + 4]
            )
            table = tables[i]
            zSet = table[(alpha, beta)]
            kSet = set({})
            for z in zSet:
                kSet.add(z ^ alpha)
            if Key2[i]:
                Key2[i] &= kSet
            else:
                Key2[i] = kSet
    print("Key1: \n", Key1)
    print("Key2: \n", Key2)
    Key = [Key1[i] & Key2[i] for i in range(8)]
    print("Key: \n", Key)
    Keyhex = ""
    for i in range(8):
        if len(Key2[i]) == 1:
            Keyhex += format(list(Key2[i])[0], "02x")
    print("Keyhex: ", Keyhex)


def main():
    tables = []  # 8个S盒的表
    x_list1 = []
    y_list1 = []
    x_list2 = []
    y_list2 = []

    # 生成S盒表
    for i in range(8):
        table: dict[(int, int), set[int]] = {}
        # 初始化S盒表
        for alpha in range(1 << 6):
            for beta in range(1 << 6):
                table[(alpha, beta)] = set({})
        # 枚举z
        for z in range(1 << 6):
            for alpha in range(1 << 6):
                beta = [
                    a ^ b
                    for a, b in zip(
                        S_box_(intToBin(z), i), S_box_(intToBin(z ^ alpha), i)
                    )
                ]
                beta = binToInt(beta)
                table[(alpha, beta)].add(z)
        tables.append(table)

    N = 2

    for _ in range(N + 1):
        # 发送64位hex
        msgIn = urandom(8).hex()
        print("输入明文为:", msgIn, "输出密文为:", sep="\n")
        msgIn = bytes2bin(bytes.fromhex(msgIn))
        # 接收64位hex
        msgOut = bytes2bin(bytes.fromhex(input()))

        y = reverseP([a ^ b for a, b in zip(msgOut[:32], msgIn[32:])])
        x_list1.append(EP(msgOut[:32]))
        y_list1.append(y)

        y = reverseP([a ^ b for a, b in zip(msgOut[32:], msgIn[:32])])
        x_list2.append(EP(msgIn[32:]))
        y_list2.append(y)
    Diff_attack(tables, x_list1, y_list1, x_list2, y_list2, N)


if __name__ == "__main__":
    main()
