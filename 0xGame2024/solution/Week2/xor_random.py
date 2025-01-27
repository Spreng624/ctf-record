def int64_to_bytes_list(*ints):
    # 将每个64位整数转换为8字节，然后合并它们
    merged_bytes = b"".join(x.to_bytes(8, "big") for x in ints)
    # 转换为字节列表，并去除零字节
    byte_list = [byte for byte in merged_bytes if byte != 0]
    return byte_list


# 示例整数
v13 = 1306349891698577164
v14 = 1666090013777994827
v15 = 1885983640899768073
v16 = 99338668810000

# 转换并打印结果
# byte_list = int64_to_bytes_list(v13, v14, v15, v16)
byte_list = int64_to_bytes_list(v16, v15, v14, v13)
byte_list.reverse()
flag_list = []

# 解密过程
randomValue = 123  # 123, 204
for i in range(30):
    if i % 2 == 1:
        xorValue = byte_list[i] ^ randomValue
    else:
        xorValue = byte_list[i] ^ (randomValue + 3)
    flag_list.append(chr(xorValue))

flag_list = "".join(flag_list)
print(f"0xGame{{{flag_list}}}")
