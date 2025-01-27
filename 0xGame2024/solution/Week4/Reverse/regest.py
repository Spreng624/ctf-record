import ctypes
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA
from Crypto.Cipher import PKCS1_OAEP


def calculate_hash(data):
    # 创建一个SHA-1哈希对象
    hash_obj = SHA.new()

    # 提供数据进行哈希计算
    hash_obj.update(data)

    # 获取哈希值（二进制形式）
    hash_value = hash_obj.digest()

    # 将哈希值转换为十六进制字符串
    hex_digest = hash_value.hex()

    # 将十六进制字符串格式化为C代码中的格式（每两个字符一组）
    formatted_hex = "".join(
        [hex_digest[i : i + 2] for i in range(0, len(hex_digest), 2)]
    )

    return formatted_hex


# 测试函数
if __name__ == "__main__":
    for j in range(8):
        data = b"0xGameUser"
        modified_data = bytearray()
        for i in range(len(data)):
            modified_data.append(data[i] ^ (0x1C >> j))
        data = bytes(modified_data)
        print(data)

        # 调用函数并打印结果
        result = calculate_hash(data)
        print(f"0xGame{{{result}}}")
