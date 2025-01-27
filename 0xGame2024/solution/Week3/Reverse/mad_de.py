# 3阶矩阵赋值
def hello(source: list) -> list:
    return [source[3 * i : 3 * i + 3] for i in range(3)]


# 矩阵乘法
def matmul(a: list[list], b: list[list]) -> list[list]:
    c = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for i in range(3):
        for j in range(3):
            for k in range(3):
                c[i][j] += a[i][k] * b[k][j]
    return c


# 64
dst = [
    488,
    448,
    385,
    1367,
    1235,
    1054,
    317,
    273,
    258,
    620,
    320,
    325,
    1463,
    748,
    755,
    1513,
    797,
    822,
    333,
    266,
    402,
    189,
    159,
    245,
    189,
    161,
    257,
    354,
    327,
    547,
    251,
    192,
    294,
    401,
    291,
    439,
    240,
    253,
    269,
    670,
    704,
    753,
    145,
    159,
    164,
    553,
    315,
    302,
    1252,
    728,
    711,
    1469,
    805,
    740,
    455,
    337,
    213,
    254,
    229,
    110,
    300,
    160,
    158,
    0,
]

k_ = [
    [[7, -2, -2], [3, -1, 0], [-6, 2, 1]],
    [[-26, 8, 3], [24, -7, -3], [-7, 2, 1]],
    [[2, -2, -1], [-1, 1, 1], [2, -1, -2]],
    [[-1, 5, -2], [1, -6, 3], [-1, 8, -4]],
]


def main():

    for i in range(7):
        dst_ = hello(dst[9 * i : 9 * i + 9])
        memory_ = matmul(k_[i % 4], dst_)
        for j in range(3):
            for k in range(3):
                print(chr(memory_[j][k]), end="")
        print("\b\b\b", end="")


if __name__ == "__main__":
    main()
# 0xGame{78d51c59-6dc3-30d2-1276-18e13f80c478}
