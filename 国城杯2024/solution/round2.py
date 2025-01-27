def Makebox(p0):
    ointArray = [0] * 1024
    for i in range(1024):
        i2 = 1023 - i
        ointArray[i2] = i
    for i in range(1024):
        ointArray[i] ^= ord(p0[i % len(p0)])
    return ointArray


class Round:
    def __init__(self):
        super().__init__()

    def shl(self, p0, p1):
        p0 = (p0 >> 3) % 1024
        return Round.Result(p0, ((p1 + p0) % 1024))

    def shr(self, p0, p1):
        p0 = (p0 << 3) % 1024
        return Round.Result(p0, ((p1 + p0) % 1024))

    def add(self, p0, p1, p2):
        p1 = (p1 + p0[p2]) % 1024
        return Round.Result(p1, (p2 + p1) % 1024)

    def sub(self, p0, p1, p2):
        p1 = (((p1 - p0[p2]) % 1024) + 1024) % 1024
        return Round.Result(p1, (p2 + p1) % 1024)

    def xor(self, p0, p1, p2):
        i = (p0[p2] ^ p1) % 1024
        return Round.Result(i, (p2 + i) % 1024)

    def round(self, p0, p1):
        assert len(p1) == 12
        result = None
        ointArray = [0] * 12
        i2 = 33
        for i in range(12):
            c = ord(p1[i])
            for _ in range(32):
                match (p0[i2] ^ c) % 5:
                    case 0:
                        result = self.add(p0, c, i2)
                    case 1:
                        result = self.sub(p0, c, i2)
                    case 2:
                        result = self.xor(p0, c, i2)
                    case 3:
                        result = self.shl(c, i2)
                    case 4:
                        result = self.shr(c, i2)
                    case _:
                        Round.Result(c, i2)
                c = result.getNum()
                i2 = result.getRip()
            ointArray[i] = c
        return ointArray

    class Result:
        def __init__(self, num, rip):
            self.num = num
            self.rip = rip

        def getNum(self):
            return self.num

        def getRip(self):
            return self.rip


def func(password):
    match password[7]:
        case "A":
            return True
        case "C":
            return True
        case "E":
            return True
        case "M":
            return True
        case "P":
            return True
        case "b":
            return True
        case "n":
            return True
        case "w":
            if password[8] in ["J", "P", "Q", "T", "U", "Z"]:
                return True
    # if i == 8 and p in ["B", "I", "N", "T", "W", "d"]:
    #     continue
    # if i == 9 and p in ["g"]:
    #     continue
    return False


def Crack(encoded_box):
    ointArray1 = [352, 646, 752, 882, ord("A"), 0, ord("z"), 0, 0, 7, 350, 360]
    ps = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz_"
    password = "000000000000"
    assert len(password) == 12
    for i in range(12):
        for p in ps:
            password = password[:i] + p + password[i + 1 :]
            result = Round().round(encoded_box, password)
            if result[i] == ointArray1[i]:
                if func(password):
                    continue
                break
        else:
            print("Failed to crack")
            break
    print(password)
    return password


# 示例用法
if __name__ == "__main__":
    encoded_box = Makebox("c9m1bRmfY5Wk")
    password = Crack(encoded_box)
    # _rounD_we_go
    print(f"D0g3xGC{{round_and{password}}}")
