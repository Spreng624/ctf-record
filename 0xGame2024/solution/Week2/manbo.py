import random
import base64

flag = "0xGame{This_is_a_fake_flag}"


def real_real_real_random():
    random_num = random.randint(1, 1000)
    return str(random_num)


def RC4(plain, K):
    S = [0] * 256
    T = [0] * 256
    for i in range(0, 256):
        S[i] = i
        T[i] = K[i % len(K)]

    j = 0
    for i in range(0, 256):
        j = (j + S[i] + ord(T[i])) % 256
        S[i], S[j] = S[j], S[i]

    i = 0
    j = 0

    cipher = []
    for s in plain:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        t = (S[i] + S[j]) % 256
        k = S[t]
        cipher.append(chr(ord(s) ^ k))
    print(f"cipher={cipher}")

    return (base64.b64encode("".join(cipher).encode())).decode()


def base3(s):
    base3_s = ""
    for i in s:
        print(f"i={i}")
        dec_value = ord(i)
        print(f"dec_value={dec_value}")
        base3_c = ""
        while dec_value > 0:
            base3_c += str(dec_value % 3)
            dec_value = dec_value // 3
        base3_c = base3_c[::-1].rjust(5, "0")
        base3_s += base3_c
    return base3_s


def manbo_encode(base3_s):
    manbo_dict = {"0": "曼波", "1": "哦耶", "2": "哇嗷"}
    manbo_text = ""
    for i in base3_s:
        manbo_text += manbo_dict[i]
    return manbo_text


def encode(i):
    flag_part = flag[i * 2 : i * 2 + 2]
    print(flag_part)
    key = str(359)
    print(f"key={key}")
    b = RC4(flag_part, key)
    print(f"b={b}")
    c = base3(b)
    print(f"c={c}")
    d = manbo_encode(c)
    print(f"d={d}")


encode(0)
