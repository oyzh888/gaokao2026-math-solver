import math, random
print("="*60); print("CONSOLIDATED VERIFICATION OF ALL PARTS"); print("="*60)
# (1)
def f1(x): return 2**x if x<0 else 1-x
good=[(-5+10*i/400000) for i in range(400001) if f1(-1+(-5+10*i/400000))>0.5]
print("(1) D(-1) =~ (%.5f, %.5f)  -> (0, 1.5)"%(min(good),max(good)))
# (2)
def f2(x): return 2**x if x<0 else (0.0 if x==0 else -2**(-x))
random.seed(0); fails=0
for _ in range(300000):
    x1,x2=random.uniform(-3,3),random.uniform(-3,3)
    if abs(x1)<1e-6 or abs(x2)<1e-6: continue
    if f2(x1)<=f2(x2):
        d=random.uniform(-6,6)
        if f2(x2+d)>f2(x2) and not f2(x1+d)>f2(x1): fails+=1
print("(2) containment counterexamples:", fails, "(expect 0)")
# (3i) construction validity for c<1
c=0.9; x=math.log2((c+1)/2)
print("(3i) c=%.2f -> x=%.4f in(-1,0):%s, 2^x=%.3f in(c,1):%s"%(c,x,-1<x<0,2**x,c<2**x<1))
# (3ii) canonical valid f passes cond1 & cond2; strictly increasing
def f3(x): return 2**x if x<0 else (1.0 if x==0 else -2**(-x))
random.seed(1); fails=0
for _ in range(2000000):
    a,b=random.uniform(-5,5),random.uniform(-5,5)
    if f3(a)<=f3(b)+1e-12:
        d=random.uniform(-10,10)
        if f3(b+d)>f3(b)+1e-12 and not f3(a+d)>f3(a)+1e-12: fails+=1
inc=all(f3(0.1*i)<f3(0.1*i+0.1) for i in range(1,100))
neg=all(f3(0.05*i)<=0 for i in range(1,200))
c2=all(f3(x)<1 for x in [0.1,0.3,0.5,0.7,0.9])
print("(3ii) canonical f: cond1 fails=%d, cond2=%s, f<=0 on(0,inf)=%s, strictly incr=%s"%(fails,c2,neg,inc))
