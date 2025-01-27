def exit():
    print("解谜失败")
    exit(1)


def check(board, x, y):
    t = board[x][y]
    x_ = x - x % 3
    y_ = y - y % 3

    for i in range(9):
        if i != x and i != y and (t == board[x][i] or t == board[i][y]):
            return False

    for i in range(3):
        for j in range(3):
            if x_ + i != x and y_ + j != y and t == board[x_ + i][y_ + j]:
                return False

    return True


def flag(answer):
    s = []

    for i in range(0, len(answer), 6):
        var3 = int(answer[i : i + 6])
        s.append(hex(var3)[2:])

    return "".join(s)


def main():
    board = [
        [5, 7, 0, 9, 4, 0, 8, 0, 0],
        [0, 0, 8, 0, 3, 0, 0, 0, 5],
        [0, 1, 0, 2, 0, 0, 0, 3, 7],
        [0, 0, 9, 7, 2, 0, 0, 0, 0],
        [7, 3, 4, 0, 0, 8, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 7, 5, 1],
        [3, 0, 0, 0, 1, 4, 2, 0, 0],
        [0, 6, 0, 0, 0, 2, 0, 4, 0],
        [0, 2, 7, 0, 0, 9, 5, 0, 0],
    ]

    # board = [
    #    [5, 7, 3| 9, 4, 1| 8, 6, 2],
    #           0        0     0  0
    #    [2, 4, 8| 6, 3, 7| 1, 9, 5],
    #     0  0     0     0  0  0
    #    [9, 1, 6| 2, 8, 5| 4, 3, 7],
    #     0     0     0  0  0
    #    [1, 5, 9| 7, 2, 6| 3, 8, 4],
    #     0  0           0  0  0  0
    #    [7, 3, 4| 1, 5, 8| 6, 2, 9],
    #              0  0     0  0  0
    #    [6, 8, 2| 4, 9, 3| 7, 5, 1],
    #     0  0  0  0  0  0
    #    [3, 9, 5| 8, 1, 4| 2, 7, 6],
    #        0  0  0           0  0
    #    [8, 6, 1| 5, 7, 2| 9, 4, 3],
    #     0     0  0  0     0     0
    #    [4, 2, 7| 3, 6, 9| 5, 1, 8]
    #     0        0  0        0  0
    #     3162 246719 96854 156384 15629 682493 95876 815793 43618
    #     4+6+5+6+5+6+5+6+5= 48
    # ]

    print("请输入你的解谜结果:")
    answer = "316224671996854156384156296824939587681579343618"
    if len(answer) != 48:
        exit()

    var3 = 0

    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                var6 = int(answer[var3])
                if 1 <= var6 <= 9:  # ASCII调整，'0'字符的ASCII码是48，所以需要减去48
                    board[i][j] = var6
                    var3 += 1
                else:
                    exit()

    for i in range(9):
        for j in range(9):
            if not check(board, i, j):
                exit()

    print(
        f"0xGame{{{flag(answer)}}}"
    )  # 0xGame{4d340a40fcd088c5dc9c48778e5643a666b53e42}


if __name__ == "__main__":
    main()

    # board = [
    #     [5, 7, 3, 9, 4, 1, 8, 6, 2],
    #     [2, 4, 8, 6, 3, 7, 1, 9, 5],
    #     [9, 1, 6, 2, 8, 5, 4, 3, 7],
    #     [1, 5, 9, 7, 2, 6, 3, 8, 4],
    #     [7, 3, 4, 1, 5, 8, 6, 2, 9],
    #     [6, 8, 2, 4, 9, 3, 7, 5, 1],
    #     [3, 9, 5, 8, 1, 4, 2, 7, 6],
    #     [8, 6, 1, 5, 7, 2, 9, 4, 3],
    #     [4, 2, 7, 3, 6, 9, 5, 1, 8],
    # ]
    # for i in range(9):
    #     for j in range(9):
    #         if not check(board, i, j):
    #             print("解谜失败")
