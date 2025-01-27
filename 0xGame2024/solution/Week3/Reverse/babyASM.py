data = [
    20,
    92,
    43,
    69,
    81,
    73,
    95,
    23,
    72,
    22,
    24,
    69,
    25,
    27,
    22,
    17,
    23,
    29,
    24,
    73,
    17,
    24,
    85,
    27,
    112,
    76,
    15,
    92,
    24,
    1,
    73,
    84,
    13,
    81,
    12,
    0,
    84,
    73,
    82,
    8,
    82,
    81,
    76,
    125,
]  # 44


def printf(format, *args):
    print(format % args)  # 简化的printf实现，实际printf更复杂


def printFLAG(flag_bytes):
    printf("%s", bytes(flag_bytes))


def main():
    # 第一个循环：将每个字节增加28
    for i in range(22):
        data[i] += 28

    printFLAG(data)  # 打印处理后的data数组

    # 第二个循环：对data数组进行异或操作
    for i in range(22, 43):
        data[i] ^= data[i - 22]

    printFLAG(data)  # 打印处理后的data数组
    # 0xGame{3d24a572-394e-aec7-b9c2-f9097fda1f4L}


if __name__ == "__main__":
    main()
