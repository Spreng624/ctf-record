from string import ascii_letters, digits
from hashlib import sha256
from itertools import product


def find_proof(proof, target_hash):
    dict_ = ascii_letters + digits
    for word in ("".join(combination) for combination in product(dict_, repeat=4)):
        if sha256((word + proof).encode()).hexdigest() == target_hash:
            return word
    return None


def main():
    # 从用户那里获取proof和target_hash
    proof = input("请输入proof: ")
    target_hash = input("请输入target_hash: ")

    # 打印出需要破解的哈希值
    print(f"[+] sha256(XXXX+{proof}) == {target_hash}")

    # 找到正确的XXXX
    xxxx = find_proof(proof, target_hash)
    if xxxx:
        print(f"找到的XXXX是: {xxxx}")
    else:
        print("没有找到正确的XXXX")


if __name__ == "__main__":
    main()
