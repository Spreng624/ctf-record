from random import getrandbits
from secret import flag, seed
from hashlib import md5


def MD5(m):
    return md5(str(m).encode()).hexdigest()


class LFSR:
    def __init__(self, seed, Length):
        self.Length = Length
        assert seed.bit_length() < self.Length + 1
        self.Mask_seed = getrandbits(self.Length)
        self.state = self.init_state(seed)
        self.mask = self.init_state(self.Mask_seed)

    def init_state(self, seed):
        result = [int(i) for i in bin(seed)[2:]]
        PadLenth = self.Length - len(result)
        result += [0] * PadLenth
        assert len(result) == self.Length
        return result

    def next(self):
        output = 0
        for i in range(self.Length):
            output ^= self.state[i] & self.mask[i]
        self.state = self.state[1:] + [output]
        return output

    def getrandbits(self, Length):
        result = []
        for _ in range(Length):
            result.append(str(self.next()))
        return int("".join(result), 2)


assert seed.bit_length() == 128
test = LFSR(seed, 128)
print(test.Mask_seed)
print(test.getrandbits(128))
print(test.getrandbits(128))

assert flag == "0xGame{" + MD5(seed) + "}"
"""
245818399386224174743537177607796459213
103763907686833223776774671653901476306
136523407741230013545146835206624093442
"""
