def decrypt(encrypted_str):
    alphabat = "0123456789abcdef"
    decrypted_str = ""

    for char in encrypted_str:
        if char in alphabat:
            # 找到字符在alphabat中的索引
            index = alphabat.index(char)
            # 逆向计算原始索引
            original_index = (index - 3) * 13 % 16
            decrypted_str += alphabat[original_index]
        else:
            # 如果字符不是十六进制字符，直接追加
            decrypted_str += char

    return decrypted_str


# 示例加密字符串
encrypted_example = "ab50e920-4a97-70d1-b646-cdac5c873376"

# 解密示例
decrypted = decrypt(encrypted_example)
print(f"0xGame{{{decrypted}}}")
