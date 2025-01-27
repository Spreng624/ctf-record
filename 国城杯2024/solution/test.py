# 标准Base64字符集
BASE64_CHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"


def encode(input_string):
    # 将输入字符串转换为字节数组
    bytes_data = input_string.encode("utf-8")
    # 初始化输出字符串
    output = []

    # 计算需要填充的字节数
    padding = 3 - (len(bytes_data) % 3)
    if padding < 3:
        bytes_data += b"\x00" * padding  # 填充字节以使长度成为3的倍数

    # 按每3个字节一组处理
    for i in range(0, len(bytes_data), 3):
        # 取出3个字节
        b1, b2, b3 = bytes_data[i : i + 3]
        # 将3个字节合并成一个24位的整数
        combined = (b1 << 16) | (b2 << 8) | b3
        # 分割成4个6位的整数并映射到Base64字符集
        output.append(BASE64_CHARS[(combined >> 18) & 63])
        output.append(BASE64_CHARS[(combined >> 6) & 63])
        output.append(BASE64_CHARS[(combined >> 12) & 63])
        output.append(BASE64_CHARS[combined & 63])

    # 将填充的字符替换为'='
    result = "".join(output)
    if padding:
        result = result[:-padding] + "=" * padding

    return result


def decode(s):
    # 去除输入字符串中的填充字符'='
    padding = s.count("=")
    s = s.rstrip("=")

    # 初始化输出字节数组
    output = bytearray()

    # 按每4个字符一组处理
    for i in range(0, len(s), 4):
        # 将Base64字符转换为对应的6位整数
        i1 = BASE64_CHARS.index(s[i + 0])
        i2 = BASE64_CHARS.index(s[i + 1]) if padding < 3 or i + 1 < len(s) else 0
        i3 = BASE64_CHARS.index(s[i + 2]) if padding < 2 or i + 2 < len(s) else 0
        i4 = BASE64_CHARS.index(s[i + 3]) if padding < 1 or i + 3 < len(s) else 0
        print(i1, i2, i3, i4)
        # 合并成一个24位的整数
        combined = (i1 << 18) | (i3 << 12) | (i2 << 6) | i4
        # 分割成3个8位的字节
        b1 = (combined >> 16) & 0xFF
        b2 = (combined >> 8) & 0xFF
        b3 = combined & 0xFF
        # 添加到输出字节数组
        output.append(b1)
        if padding < 2 or i < len(s):
            output.append(b2)
        if padding < 1 or i < len(s):
            output.append(b3)

    # 返回解码后的字节序列
    return bytes(output)


# 示例用法
if __name__ == "__main__":
    # input_string = "Hello, World!!!"
    # encoded_string = encode(input_string)
    # print("Base64 Encoded:", encoded_string)  # 输出: SGVsbG8sIFdvcmxkIQ==
    # decoded_string = decode(encoded_string).decode("utf-8")
    # print("Base64 Decoded:", decoded_string)
    print(decode("c9m1bRmfY5Wk"))
    print(encode("round_and"))  # D0g3xGC{round_and}
