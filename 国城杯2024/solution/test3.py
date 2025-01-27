v5 = "5201314005201314"
v10 = "05B0DF775A764F8A"
v5 = [int(v5[i : i + 2], 16) for i in range(0, len(v5), 2)]
v10 = [int(v10[i : i + 2], 16) for i in range(0, len(v10), 2)]
v15 = [v5[i] ^ v10[i] for i in range(len(v5))]
print(v15)
for i in range(len(v15)):
    v15[i] = chr(v15[i])
v15 = "".join(v15)
print(v15)
