import gmpy2


def giao(base_num, i):
    x = 0x0000000001000000000000000000013B
    MOD = 2**128
    base_num = (base_num * x) & (MOD - 1)  # 取后128位
    base_num ^= i
    return base_num


def regiao(base_num, i):
    x = 0x0000000001000000000000000000013B
    print(hex(gmpy2.invert(x, 2**128)))
    x = 0xB1041AD2562FF2FF2FF2FF2FF2FF2FF3
    print(x)
    MOD = 2**128
    base_num ^= i
    base_num = (base_num * x) & (MOD - 1)  # 取后128位
    return base_num


A = 0x6C62272E07BB014262B821756295C58D
print(A)
print(giao(A, 0x1))
print(regiao(giao(A, 0x1), 0x1))
