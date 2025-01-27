# 面向int32


# 3阶矩阵赋值
def hello(source: list) -> list:
    return [source[3 * i : 3 * i + 3] for i in range(3)]


# 44位字符串生成矩阵
def Morpheus(inputs: str) -> list[list]:
    inputs += "0"  # 补齐
    inputs: list[int] = [ord(i) for i in inputs]  # 16进制转10进制
    memory = []

    # 44*1->44*4=176 用0填充
    # 44*4 -> 7* 24 + 8
    # 44 -> 7*6 + 2
    for i in range(7):
        # 0-36 24-72 ··· 7*24+8
        # 0-9 6-15 12-21 ··· 35-44
        x = hello(inputs[6 * i : 6 * i + 9])
        memory.append(x)  # memery = 7* 8*8= 448
    return memory


# 3阶行列式值
def det(matrix: list[list]) -> int:
    det = (
        matrix[0][0] * matrix[1][1] * matrix[2][2]
        + matrix[0][1] * matrix[1][2] * matrix[2][0]
        + matrix[0][2] * matrix[1][0] * matrix[2][1]
        - matrix[0][2] * matrix[1][1] * matrix[2][0]
        - matrix[0][1] * matrix[1][0] * matrix[2][2]
        - matrix[0][0] * matrix[1][2] * matrix[2][1]
    )
    return det


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
    13,
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

k = [
    [[1, 2, 2], [3, 5, 6], [0, 2, 1]],
    [[1, 2, 3], [3, 5, 6], [1, 4, 10]],
    [[1, 3, 1], [0, 2, 1], [1, 2, 0]],
    [[0, 4, 3], [1, 2, 1], [2, 3, 1]],
]


def main():
    # str_ = input("Memory: ")
    str_ = "0xGame{78d51c59@6dē3-30d2-1276-18e13f80c478}"
    if len(str_) != 44:
        print("Length Error")
        return -1
    memory = Morpheus(str_)
    for i in range(7):
        print(f"i={i}")
        dst_ = hello(dst[9 * i : 9 * i + 9])
        if det(k[i % 4]) != 0:
            memory_ = matmul(k[i % 4], memory[i])
        else:
            memory_ = memory[i]
        print(memory_)
        print(dst_)
        if dst_ != memory_:
            print("Value Error")
            return -1

    print("Correct")
    return 0


if __name__ == "__main__":
    main()
    # print(det(k[0]))
    # print(det(k[1]))
    # print(det(k[2]))
    # print(det(k[3]))
