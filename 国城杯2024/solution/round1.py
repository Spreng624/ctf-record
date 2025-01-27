import base64

# 标准Base64字符集
BASE64_CHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"


class MakePath:
    BASE64_CHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"  # Base64字符集

    def __init__(self):
        super().__init__()

    def Makebox(self, p0):
        ointArray = [0] * 1024
        for i1 in range(1024):
            i2 = i1 - 1023
            ointArray[i2] = i1
        for i in range(1024):
            i2 = i % len(p0)
            i1 = ointArray[i] ^ ord(p0[i2])
            ointArray[i] = i1
        return ointArray

    def encode(self, p0, p1):
        return self.Makebox(self.encodeToBase64(p1))

    def encodeToBase64(self, p0: str):
        # 将输入字符串转换为字节数组
        bytes_data = p0.encode("utf-8")
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


# 示例用法
if __name__ == "__main__":
    make_path = MakePath()
    encoded_string = make_path.encodeToBase64("round_and")
    print("Base64 Encoded:", encoded_string)
    encoded_box = make_path.Makebox(encoded_string)
    print("Encoded Box:", encoded_box)
