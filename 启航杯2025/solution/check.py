encrypted_flag = "726B607765584646154014411A400E461445160E174542410E1A4147450E4642131446131017451542165E"

flag = ""
for i in range(0, len(encrypted_flag), 2):
    flag += chr(int(encrypted_flag[i : i + 2], 16) ^ 0x23)

print(flag)  # QHCTF{ee6c7b9c-e7f5-4fab-9bdf-ea07e034f6a5}
