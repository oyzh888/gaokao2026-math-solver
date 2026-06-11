# Verify containment via explicit D formula
def f(x):
    if x<0: return 2**x
    if x==0: return 0.0
    return -2**(-x)

def D(x0):
    # returns membership function
    if x0<0:
        return lambda d: 0 < d < -x0
    else: # x0>0
        return lambda d: (d <= -x0) or (d > 0)

import random
random.seed(1)
fails=0
for _ in range(500000):
    x1=random.uniform(-3,3); x2=random.uniform(-3,3)
    if abs(x1)<1e-9 or abs(x2)<1e-9: continue
    if f(x1)<=f(x2):
        d=random.uniform(-7,7)
        if D(x2)(d) and not D(x1)(d):
            fails+=1
print("formula-based containment fails:", fails)

# Also enumerate which sign cases occur when f(x1)<=f(x2):
# x1<0 => f(x1)>0; x2<0 => f(x2)>0 ; x>0 => f<0
# f(x1)<=f(x2):
# case A x1<0,x2<0: 2^x1<=2^x2 => x1<=x2
# case B x1>0,x2>0: -2^-x1<=-2^-x2 => 2^-x1>=2^-x2 => x1<=x2
# case C x1<0(>0),x2>0(<0): f(x1)>0,f(x2)<0 => f(x1)<=f(x2) impossible
# case D x1>0,x2<0: f(x1)<0<=f(x2) always true
print("cases enumerated OK")
