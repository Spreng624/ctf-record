import gmpy2
from Crypto.Util.number import *
from sympy.ntheory import factorint
import findProof


def rsa0(n, e, c):
    def de(c, e, n):
        k = 0
        while True:
            m = c + n * k
            result, flag = gmpy2.iroot(m, e)
            if True == flag:
                return result
            k += 1

    m = de(c, e, n)
    print(m)


def rsa1(n, e, c, dp):
    p, q = factorint(n).keys()
    d = gmpy2.invert(e, (p - 1) * (q - 1))

    m = pow(c, d, n)
    print(m)


def rsa2(n, e, c):
    p, q = factorint(n).keys()
    d = gmpy2.invert(e, (p - 1) * (q - 1))

    m = pow(c, d, n)
    print(m)


def rsa3(n, e, c, e_, c_):

    p, q = factorint(n).keys()
    d = gmpy2.invert(e, (p - 1) * (q - 1))

    m = pow(c, d, n)
    print(m)


if __name__ == "__main__":
    findProof.main()
    n, e, c = input("Enter n, e, c: ").split(",")
    n, e, c = int(n), int(e), int(c)
    rsa0(n, e, c)
    n, e, c, dp = input("Enter n, e, c, dp: ").split(",")
    n, e, c, dp = int(n), int(e), int(c), int(dp)
    rsa1(n, e, c, dp)
    n, e, c = input("Enter n, e, c: ").split(",")
    n, e, c = int(n), int(e), int(c)
    rsa2(n, e, c)
    n, e, c, e_, c_ = input("Enter n, e, c, e_, c_: ").split(",")
    n, e, c, e_, c_ = int(n), int(e), int(c), int(e_), int(c_)
    rsa3(n, e, c, e_, c_)
