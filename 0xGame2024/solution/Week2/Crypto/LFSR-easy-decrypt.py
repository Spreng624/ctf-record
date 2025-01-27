from hashlib import md5


def MD5(m):
    return md5(str(m).encode()).hexdigest()


def func(A: list[list[int]], B: list[int], n: int):
    # A n行n+1列的二进制矩阵(增广矩阵)
    A = [A[i] + [B[i]] for i in range(n)]  # 增广矩阵
    for i in range(n):
        # 找出第i行的主元
        for j in range(i, n):
            if A[j][i]:
                # 交换第i行和第j行
                A[i], A[j] = A[j], A[i]
                break
        else:
            continue
        # 消元
        for j in range(n):
            if i != j and A[j][i]:
                A[j] = [A[j][k] ^ A[i][k] for k in range(n + 1)]
    X = [A[i][n] for i in range(n)]
    return X


if __name__ == "__main__":

    """
    165943427582675380464843619836793254673
    299913606793279087601607783679841106505
    192457791072277356149547266972735354901
    """

    outputs1 = 299913606793279087601607783679841106505
    outputs2 = 192457791072277356149547266972735354901
    outputs1 = [int(bit) for bit in bin(outputs1)[2:]]
    outputs2 = [int(bit) for bit in bin(outputs2)[2:]]

    # 定义长度为 2n 的二进制列表 K
    n = 128
    K = outputs1 + outputs2

    # 构造系数矩阵 A 和常数向量 B
    A = [K[i : i + n] for i in range(n)]
    B = K[n : 2 * n]

    # 求解线性方程组
    X = func(A, B, n)
    mask = int("".join(str(bit) for bit in X), 2)

    print(f"0xGame{{{MD5(mask)}}}")
    # 0xGame{d56821feacab64cdb87c754ad06823a2}
