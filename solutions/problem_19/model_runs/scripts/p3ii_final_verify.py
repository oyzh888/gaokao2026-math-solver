import math, random
# FINAL: construct the canonical valid f (f<=0 on positives, strictly increasing) and verify cond①+②.
# f(x)=2^x for x<0; f(0)=c>=1; for x>0: f(x)<=0, strictly increasing, e.g. f(x)= -2^{-x} (in (-1,0), increasing). 
def mk(c):
    def f(x):
        if x<0: return 2.0**x
        if x==0: return c
        return -2.0**(-x)   # (-1,0), strictly increasing on (0,inf)
    return f
abgrid=[-3,-2,-1,-0.5,-0.25,-0.1,0,0.2,0.5,0.8,1.0,1.5,2.0,2.5,3.0,4.0]
dgrid=[round(-9+18*i/3600,5) for i in range(3601)]
def cond1(f):
    for a in abgrid:
        fa=f(a)
        for b in abgrid:
            if fa<=f(b)+1e-9:
                fb=f(b)
                for d in dgrid:
                    if f(b+d)>fb+1e-9 and not (f(a+d)>fa+1e-9):
                        return False,(a,b,round(d,4),round(fa,3),round(fb,3))
    return True,None
for c in [1.0,1.5,2.0]:
    f=mk(c)
    print("CANONICAL f(x)=-2^{-x} on x>0, f(0)=%.1f: cond1=%s cond2=%s strictly-incr-on(0,inf)=True"%(
        c, cond1(f), all(f(x)<c for x in [0.1,0.5,0.9])))
print()
# Verify ALL lemmas hold for this f:
f=mk(1.0)
# BAND: f(x)<=0 for x>0 ✓ (it's -2^-x<0). 
print("BAND: max f on (0,5):", max(f(x) for x in [0.01*i for i in range(1,500)]), "(<=0)")
# UP2: f(b)<=0 ⟹ f(t)>f(b) ∀t>b: monotone increasing ✓
print("UP2 (monotone on positives):", all(f(0.1*i)<f(0.1*(i+1)) for i in range(1,50)))
