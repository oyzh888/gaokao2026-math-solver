# Compute D(x0) explicitly as a set description, for various x0, to find pattern
def f(x):
    if x<0: return 2**x
    if x==0: return 0.0
    return -2**(-x)

def Dset_endpoints(x0):
    # scan d, find where f(x0+d)>f(x0)
    pts=[]
    N=2000000
    lo,hi=-12,12
    inS=False
    intervals=[]
    start=None
    prev=False
    for i in range(N+1):
        d=lo+(hi-lo)*i/N
        cur = f(x0+d)>f(x0)
        if cur and not prev:
            start=d
        if not cur and prev:
            intervals.append((start,d))
        prev=cur
    if prev: intervals.append((start,hi))
    return intervals

for x0 in [-2,-1,-0.5, 0.5, 1, 2]:
    iv=Dset_endpoints(x0)
    # also show x0+d range = (x0+lo .. ) -> t=x0+d where f(t)>f(x0)
    print("x0=",x0,"f(x0)=%.4f"%f(x0), "D intervals (d):", [(round(a,4),round(b,4)) for a,b in iv],
          " -> t=x0+d:", [(round(x0+a,4),round(x0+b,4)) for a,b in iv])
