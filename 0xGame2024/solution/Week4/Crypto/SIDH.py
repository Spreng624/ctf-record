# from random import randint
# from secret import flag

# ea, eb = 110, 67
# p = 2**ea*3**eb - 1
# F.<i> = GF(p**2, modulus=[1,0,1])

# E0 = EllipticCurve(F, [1,0])

# PA = E0.random_point()
# QA = E0.random_point()
# sA = randint(0, 2**ea)
# RA = PA + sA*QA
# print(f'[+] RA = {RA.xy()}')

# RB_= [int(i) for i in input(f'[+] Give me RB:\n>').split(',')]
# #Example: 1,2,3,4 

# RB = E0(RB_[0]*i + RB_[1], RB_[2]*i + RB_[3])
# phi_B =  E0.isogeny(RB, algorithm='factored')
# E_B = phi_B.codomain()
# assert E_B.is_isogenous(E0)

# R_share = phi_B(PA) + sA * phi_B(QA)
# phi_share = E_B.isogeny(R_share, algorithm='factored')
# secret = phi_share.codomain().j_invariant()

# secret_ = [int(i) for i in input('[+] Tell me the secret\n>').split(',')]
# secret_ = secret_[0] * i + secret_[1]
# #Example: 1,2

# if secret_ == secret:
# 	print(f'[+] flag:{flag}')
# else:
# 	print('[+] Wrong')