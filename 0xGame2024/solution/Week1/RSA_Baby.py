from hashlib import md5


def MD5(m):
    return md5(str(m).encode()).hexdigest()


c = 344136655393256706
d = 488474228706714247
N = 547938466798424179
m = pow(c, d, N)
flag = "0xGame{" + MD5(m) + "}"

print(flag)
