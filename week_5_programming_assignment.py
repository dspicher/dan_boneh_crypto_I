from IPython import embed
import gmpy2
from gmpy2 import mpz

p = mpz('13407807929942597099574024998205846127479365820592393377723561443721764030073546976801874298166903427690031858186486050853753882811946569946433649006084171')

g = mpz('11717829880366207009516117596335367088558084999998952205599979459063929499736583746670572176471460312928594829675428279466566527115212748467589894601965568')

h = mpz('3239475104050450443565264378728065788649097520952449527834792452971981976143292558073856937958553180532878928001494706097394108577585732452307673444020333')

B = mpz(2**20)


lhs_map = {}
lhs = set([])
for idx, x1 in enumerate(range(2**20+1)):
    res = gmpy2.divm(h, gmpy2.powmod(g, x1, p), p)
    lhs.add(res)
    lhs_map[res] = x1

rhs_map = {}
rhs = set([])
rhs_base = gmpy2.powmod(g, B, p)
for idx, x0 in enumerate(range(2**20+1)):
    res = gmpy2.powmod(rhs_base, x0, p)
    rhs.add(res)
    rhs_map[res] = x0

match = lhs.intersection(rhs)
assert(len(match) == 1)
match_value = match.pop()
x0 = rhs_map[match_value]
x1 = lhs_map[match_value]
x = x0*B+x1

print("found solution\nx0 =\t\t{}\nx1 =\t\t{}\nh/g^x1 =\t{}\n(g^B)^x0 =\t{}\nh =\t\t{}\ng^x =\t\t{}\nx =\t\t{}".format(
    x0,
    x1,
    gmpy2.divm(h, gmpy2.powmod(g, x1, p), p),
    gmpy2.powmod(rhs_base, x0, p),
    h,
    gmpy2.powmod(g, x, p),
    x
))
