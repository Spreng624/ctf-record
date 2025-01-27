#!/usr/bin/env python
# visit https://tool.lu/pyc/  for more information
# Version: Python 3.8

import hashlib

# user_input = input("请输入神秘代号：")
# if user_input != "Ciallo~":
#     print("代号不是这个哦")
#     exit()

user_input = "Ciallo~"

input_hash = hashlib.md5(user_input.encode()).hexdigest()
input_hash = list(input_hash)

# 修复后的循环
for i in range(len(input_hash)):
    if input_hash[i].isdigit():  # 检查是否是数字
        original_num = int(input_hash[i])
        new_num = (original_num + 5) % 10
        input_hash[i] = str(new_num)

# 将列表转换回字符串
input_hash = "".join(input_hash)

# 输出结果
print("0xGame{{{}}}".format(input_hash))
