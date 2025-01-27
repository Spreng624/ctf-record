import findProof


def find_keystream(m, c):
    # 将密文从十六进制转换为字节
    c_bytes = bytes.fromhex(c)

    # 将明文转换为字节
    m_bytes = bytes.fromhex(m)
    # 提取密钥流
    keystream = bytes(a ^ b for a, b in zip(m_bytes, c_bytes))
    return keystream


# 使用提取的密钥流来解密其他密文
def decrypt(ciphertext, keystream):
    if type(ciphertext) == bytes:
        ct = ciphertext
    else:
        ct = bytes.fromhex(ciphertext)

    result = b""
    for i in range(len(ct)):
        result += bytes([ct[i] ^ keystream[i % len(keystream)]])
    return result.decode("utf-8")


if __name__ == "__main__":
    findProof.main()
    m = "0xGame{Hello-World-This-Is-A-Very-long-flag}".encode("utf-8").hex()
    print(f"m={m}")
    c = input("请输入加密文本")
    keystream = find_keystream(m, c)

    c = input("请输入加密文本")
    # 解密操作
    decrypted_text = decrypt(c, keystream)
    print("解密后的文本:", decrypted_text)
