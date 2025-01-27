encrypted_flag = "0B12190E1C213B6268686C6B6A69776F3B633B776E3C3B6D773B38393C773E3F3B6E69623B6D393F6D6227"

flag = ""
for i in range(0, len(encrypted_flag), 2):
    flag += chr(int(encrypted_flag[i : i + 2], 16) ^ 90)

print(flag)  # QHCTF{a8226103-5a9a-4fa7-abcf-dea438a7ce78}
