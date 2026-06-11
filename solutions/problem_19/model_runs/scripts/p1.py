def f(x):
    return 2**x if x<0 else 1-x

fm1 = f(-1)
print("f(-1) =", fm1)

# scan
N=400000
good=[]
for i in range(N+1):
    d = -5 + 10*i/N
    if f(-1+d) > fm1:
        good.append(d)
print("d range where f(-1+d)>1/2:", round(min(good),5), round(max(good),5))

for d in [0.0, 0.0001, 1.4999, 1.5, 1.5001, 0.999, 1.0, 1.001]:
    print(f"d={d}: f(-1+d)={f(-1+d):.5f} > 0.5? {f(-1+d)>0.5}")
