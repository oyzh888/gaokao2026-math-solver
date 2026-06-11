import math, random
def mk(c):
    def f(x):
        if x<0: return 2.0**x
        if x==0: return c
        return -2.0**(-x)
    return f
f=mk(1.0)
# Dense random cond① test
random.seed(42)
fails=0
for _ in range(2000000):
    a=random.uniform(-5,5); b=random.uniform(-5,5)
    if f(a)<=f(b)+1e-12:
        d=random.uniform(-10,10)
        if f(b+d)>f(b)+1e-12 and not f(a+d)>f(a)+1e-12:
            fails+=1
print("canonical f dense cond① random test fails:", fails)

# Verify each "violation always breaks cond①" — test 3 violating structures:
def viol_band(x):  # f in (0,1) on a positive point -> should fail
    if x<0: return 2.0**x
    if x==0: return 1.0
    if 0<x<1: return 0.5  # in (0,1) FORBIDDEN
    return -2.0**(-x)
def viol_dec(x):  # decreasing on positives
    if x<0: return 2.0**x
    if x==0: return 1.0
    return -2.0**(-x)-0.3*x  # add decreasing component? actually -2^-x -0.3x : derivative? -2^-x increasing(+), -0.3x dec. mixed
def viol_nonmono(x):
    if x<0: return 2.0**x
    if x==0: return 1.0
    return -2.0**(-x) + 0.5*math.sin(3*x)*2**(-x)  # wiggle
abgrid=[-3,-2,-1,-0.5,-0.1,0,0.3,0.7,1.0,1.5,2.0,2.5,3.0]
dgrid=[round(-9+18*i/1800,5) for i in range(1801)]
def cond1(f):
    for a in abgrid:
        fa=f(a)
        for b in abgrid:
            if fa<=f(b)+1e-9:
                fb=f(b)
                for d in dgrid:
                    if f(b+d)>fb+1e-9 and not (f(a+d)>fa+1e-9): return False
    return True
print("viol_band (f∈(0,1) on positives) passes cond①?", cond1(viol_band), "(expect False)")
print("viol_nonmono (wiggly) passes cond①?", cond1(viol_nonmono), "(expect False)")
