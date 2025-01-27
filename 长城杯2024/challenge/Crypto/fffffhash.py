import os
from Crypto.Util.number import *
def giaogiao(hex_string):
	base_num = 0x6c62272e07bb014262b821756295c58d
	x = 0x0000000001000000000000000000013b
	MOD = 2**128
	for i in hex_string:
		base_num = (base_num * x) & (MOD - 1) 
		base_num ^= i
	return base_num


giao=201431453607244229943761366749810895688

print("1geiwoligiaogiao")
hex_string = int(input(),16)
s = long_to_bytes(hex_string)

if giaogiao(s) == giao:
	print(os.getenv('FLAG'))
else:
	print("error")