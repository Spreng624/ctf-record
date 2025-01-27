from hashlib import md5


def MD5(m):
    return md5(str(m).encode()).hexdigest()


def recover_state(o_state: list[int], mask: list[int], length):
    # 计算state的最后一个元素
    o = o_state[-1]
    for i in range(length - 1, 0, -1):
        o ^= o_state[i - 1] & mask[i]
    o ^= 0
    state = [o] + o_state[:-1]

    return state


def decode(mask: list[int], outputs: list[int]):
    current_state = outputs
    for _ in range(128):
        current_state = recover_state(current_state, mask, 128)
    seed = int("".join(str(bit) for bit in current_state), 2)  # state转为seed
    return seed


if __name__ == "__main__":
    # 已知mask_seed,两次LFSR运算得到state,逆推seed
    Mask_seed = 245818399386224174743537177607796459213
    mask = [int(i) for i in bin(Mask_seed)[2:]]
    outputs1 = 103763907686833223776774671653901476306
    outputs1 = [0] + [int(bit) for bit in bin(outputs1)[2:]]
    outputs2 = 136523407741230013545146835206624093442
    outputs2 = [0] + [int(bit) for bit in bin(outputs2)[2:]]
    seed = decode(mask, outputs1)
    print(f"0xGame{{{MD5(seed)}}}")
    # 0xGame{030ec00de18ceb4ddea5f6612d28bf39}
