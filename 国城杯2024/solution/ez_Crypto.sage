from Crypto.Util.number import *


def all_two_squares(n):
    return [
        (abs(d[0]), abs(d[1])) for d in divisors(GaussianIntegers()(n)) if norm(d) == n
    ]


def solve_e(sign1, sign2, q):
    H1, r1, s1 = sign1
    H2, r2, s2 = sign2

    s1_inv = inverse(s1, q)
    s2_inv = inverse(s2, q)

    A = r1 * r1 * s1_inv * s1_inv
    B = 2 * H1 * r1 * s1_inv * s1_inv - r2 * s2_inv
    C = H1 * H1 * s1_inv * s1_inv - H2 * s2_inv

    P = PolynomialRing(Zmod(q), "x")
    x = P.gen()
    eq = A * x ^ 2 + B * x + C

    print(eq.roots())
    # [(91973915966463187834053272623425597244095846333, 1), (1865444199836044046649, 1)]

    print(long_to_bytes(91973915966463187834053272623425597244095846333))
    print(long_to_bytes(1865444199836044046649))  # b'e = 44519'


p = 149328490045436942604988875802116489621328828898285420947715311349436861817490291824444921097051302371708542907256342876547658101870212721747647670430302669064864905380294108258544172347364992433926644937979367545128905469215614628012983692577094048505556341118385280805187867314256525730071844236934151633203
q = 829396411171540475587755762866203184101195238207
g = 87036604306839610565326489540582721363203007549199721259441400754982765368067012246281187432501490614633302696667034188357108387643921907247964850741525797183732941221335215366182266284004953589251764575162228404140768536534167491117433689878845912406615227673100755350290475167413701005196853054828541680397
y = 97644672217092534422903769459190836176879315123054001151977789291649564201120414036287557280431608390741595834467632108397663276781265601024889217654490419259208919898180195586714790127650244788782155032615116944102113736041131315531765220891253274685646444667344472175149252120261958868249193192444916098238

H1, r1, s1 = (
    659787401883545685817457221852854226644541324571,
    334878452864978819061930997065061937449464345411,
    282119793273156214497433603026823910474682900640,
)
H2, r2, s2 = (
    156467414524100313878421798396433081456201599833,
    584114556699509111695337565541829205336940360354,
    827371522240921066790477048569787834877112159142,
)
c = 18947793008364154366082991046877977562448549186943043756326365751169362247521
C = 179093209181929149953346613617854206675976823277412565868079070299728290913658

# solve_e((H1, r1, s1), (H2, r2, s2), q)
# ans = all_two_squares(C)
# print(ans)

e = 44519
ans = [
    (411800265284112683889770914584779351243, 97538457512222161659361018727247943103),
    (385935421767853150067085999079428269993, 173629085716646134993835981317457288147),
    (347432454257893250496407965506777649463, 241627603783727624224706687817893681267),
    (302951519846417861008714825074296492447, 295488723650623654106370451762393175957),
    (295488723650623654106370451762393175957, 302951519846417861008714825074296492447),
    (173629085716646134993835981317457288147, 385935421767853150067085999079428269993),
    (139154793241392602890445837550424516283, 399661297475592982293435778542228355087),
    (16944416637726545286802875167254662553, 422854698361903371427733980562270024707),
    (63300355510251304584114633515453587403, 418433117922332896279236283423489909057),
    (97538457512222161659361018727247943103, 411800265284112683889770914584779351243),
    (212200170463729600479653952183489384503, 366147916608975462877987617004979518093),
    (241627603783727624224706687817893681267, 347432454257893250496407965506777649463),
    (366147916608975462877987617004979518093, 212200170463729600479653952183489384503),
    (399661297475592982293435778542228355087, 139154793241392602890445837550424516283),
    (418433117922332896279236283423489909057, 63300355510251304584114633515453587403),
    (422854698361903371427733980562270024707, 16944416637726545286802875167254662553),
]


for p, q in ans:
    N = p * q
    phi = (p - 1) * (q - 1)
    d = inverse(e, phi)
    m = pow(c, d, N)

    try:
        print(long_to_bytes(int(m)).decode())
    except:
        pass
