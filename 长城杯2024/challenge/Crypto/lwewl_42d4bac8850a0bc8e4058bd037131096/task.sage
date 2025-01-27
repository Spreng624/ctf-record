from Crypto.Util.number import *
from random import randint
from secret import flag

assert flag.startswith(b'flag{') and flag.endswith(b'}')
flag = flag[5:-1]
flag1 = flag[:len(flag)//2]
flag2 = flag[len(flag)//2:]

class LWE:
    def __init__(self, lwe_dim, lwe_num_samples, lwe_plaintext_modulus, lwe_ciphertext_modulus, rlwe_dim, rlwe_modulus):
        self.lwe_dim = lwe_dim
        self.lwe_num_samples = lwe_num_samples
        self.lwe_plaintext_modulus = lwe_plaintext_modulus
        self.lwe_ciphertext_modulus = lwe_ciphertext_modulus
        self.lwe_secret_key = self.distribution(0, self.lwe_ciphertext_modulus - 1, self.lwe_dim)
        self.rlwe_dim = rlwe_dim
        self.rlwe_modulus = rlwe_modulus

    def distribution(self, lbound, rbound, dim):
        return [randint(lbound, rbound) for _ in range(dim)]

    def lwe_encrypt(self, message):
        a = self.distribution(0, lwe_ciphertext_modulus - 1, self.lwe_dim)
        e = self.distribution(-15, 15, 1)[0]
        return a, sum([a[i] * self.lwe_secret_key[i] for i in range(self.lwe_dim)]) + message + e * lwe_plaintext_modulus

    def lwe_keygen(self):
        A = []
        B = []
        for _ in range(self.lwe_num_samples):
            sample = self.lwe_encrypt(0)
            A.append(sample[0])
            B.append(sample[1])
        return A, B

    def encrypt(self, message, lwe_pubkey1, lwe_pubkey2):
        const = vector(ZZ, self.distribution(-1, 1, self.lwe_num_samples))
        e = self.distribution(-15, 15, 1)[0]
        return const * matrix(GF(lwe_ciphertext_modulus), lwe_pubkey1), const * vector(GF(lwe_ciphertext_modulus), lwe_pubkey2) + message + e * lwe_plaintext_modulus

    def rlwe_sample(self, flag):
        P.<x> = PolynomialRing(Zmod(self.rlwe_modulus))

        while True:
            monomials = [x^i for i in range(self.rlwe_dim + 1)]
            c = self.distribution(0, self.rlwe_modulus - 1, self.rlwe_dim) + [1]
            f = sum([c[i] * monomials[i] for i in range(self.rlwe_dim + 1)])
            PR = P.quo(f)
            if f.is_irreducible():
                break
        a = self.distribution(0, self.rlwe_modulus - 1, self.rlwe_dim)
        e = self.distribution(-5, 5, self.rlwe_dim)
        s = [flag[i] for i in range(len(flag))]
        b = PR(a) * PR(s) + PR(e)
        return a, b, f, self.rlwe_modulus

lwe_dimension = 2**9
lwe_num_samples = 2**9 + 2**6 + 2**5 + 2**2
lwe_plaintext_modulus = next_prime(256)
lwe_ciphertext_modulus = next_prime(1048576)
rlwe_dim = 64
rlwe_modulus = getPrime(128)

lwe = LWE(lwe_dimension, lwe_num_samples, lwe_plaintext_modulus, lwe_ciphertext_modulus, rlwe_dim, rlwe_modulus)
lwe_pubkey1, lwe_pubkey2 = lwe.lwe_keygen()
lwe_public_key = [lwe_pubkey1, lwe_pubkey2]
lwe_cipher1 = []
lwe_cipher2 = []
for flag_char in flag1:
    tmp1, tmp2 = lwe.encrypt(flag_char, lwe_pubkey1, lwe_pubkey2)
    lwe_cipher1.append(tmp1)
    lwe_cipher2.append(tmp2)

lwe_ciphertext = [lwe_cipher1, lwe_cipher2]
save(lwe_public_key, "lwe_public_key")
save(lwe_ciphertext, "lwe_ciphertext")

rlwe_ciphertext = lwe.rlwe_sample(flag2)
save(rlwe_ciphertext, "rlwe_ciphertext")
