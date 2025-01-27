from random import getrandbits
from secret import flag, Mask_seed
from hashlib import md5


def MD5(m):
    return md5(str(m).encode()).hexdigest()


# LFSR
class LFSR:
    def __init__(self, Mask_seed, Length):
        self.Length = Length  # Length of the LFSR
        assert Mask_seed.bit_length() < self.Length + 1
        self.seed = getrandbits(self.Length)
        self.state = self.init_state(self.seed)
        self.mask = self.init_state(Mask_seed)

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


assert Mask_seed.bit_length() == 128
test = LFSR(Mask_seed, 128)
print(test.seed)
print(test.getrandbits(128))
print(test.getrandbits(128))

assert flag == "0xGame{" + MD5(Mask_seed) + "}"
"""
165943427582675380464843619836793254673
299913606793279087601607783679841106505
192457791072277356149547266972735354901
"""
