# f odd, f(x)=2^x for x<0
def f(x):
    if x<0: return 2**x
    if x==0: return 0.0
    return -2**(-x)   # odd extension

# D(x0) = {d: f(x0+d) > f(x0)}
def in_D(x0, d):
    return f(x0+d) > f(x0)

import random
random.seed(0)
# test: for x1,x2 with x1*x2!=0 and f(x1)<=f(x2), check D(x2) subset D(x1)
fails=0
for _ in range(200000):
    x1 = random.uniform(-3,3)
    x2 = random.uniform(-3,3)
    if abs(x1)<1e-6 or abs(x2)<1e-6: continue
    if f(x1) <= f(x2):
        # sample d, check d in D(x2) => d in D(x1)
        d = random.uniform(-6,6)
        if in_D(x2,d) and not in_D(x1,d):
            fails+=1
            if fails<5:
                print("COUNTEREXAMPLE x1=%.3f x2=%.3f d=%.3f"%(x1,x2,d),
                      "f(x1)=%.4f f(x2)=%.4f"%(f(x1),f(x2)))
print("fails:", fails)
