import math, random
# (♦) self-similarity essentially says: on the region where f∈(0,1) reachable... but BAND forbids (0,1) on positives.
# So on positives f is either <=0 or >=1. The (♦) constraint came from negative pairs constraining via V∈(0,1):
#   f(t)>V ⇒ f(t-h)>V·2^{-h}. For positives with f>=1: f(t)>V(any<1) always (f>=1>V), so RHS f(t-h)>V·2^{-h}.
#   Take t>0 f(t)>=1, V->1^-, any h: f(t-h)>2^{-h}. If t-h>0 with f(t-h)>=1>2^{-h} OK auto. If t-h<0: f=2^{t-h}>2^{-h}⟺t>0 ✓. So (♦) AUTO-satisfied when f(t)>=1. (♦) gives NOTHING new on the >=1 region!
# So the binding constraints on the >=1 region are NOT (♦). They are the SPIKE/UP1 ones. 
# I proved UP1: f(b)>=1 ⟹ f(w)<=f(b) ∀w∈(0,b). This means on the set {f>=1}, f is "running max".
# And UP2: f(b)<=0 ⟹ f(t)>f(b) ∀t>b.
# 
# Can rise-fall happen? f(P)>=1 (P>0) then f(Q)<=0 (Q>P). 
#   UP2 at Q: f(t)>f(Q) ∀t>Q. fine. 
#   UP1 at P: f(w)<=f(P) ∀w∈(0,P). fine. 
#   Take ANY R>Q with f(R)>=1 (if exists): UP1 at R ⟹ f(w)<=f(R) ∀w∈(0,R), incl w=P: f(P)<=f(R). 
#   But does an R>Q with f(R)>=1 have to exist? If f stays <=0 for all t>=Q, then no R. 
#   So f could be: <=0 on (0,1), >=1 on say [1,2), <=0 on [2,∞). rise then permanently fall. 
#   Is THAT consistent? Let me build it RESPECTING the exact forms and test cond① super-carefully.
# On [1,2): f>=1, must satisfy UP1 (running max) → f nondecreasing there & >= everything left. 
#   Let f=2^{x-1} on [1,2)? values [1,2). at x=1:1. UP1 ok if these >= all of (0,1) values (which are <=0). yes.
# On (0,1): f<=0. UP2 at each such b: f(t)>f(b) ∀t>b. so f strictly increasing-ish on the <=0 region going right? f(t)>f(b) for t>b. On (0,1) if f<=0 and increasing, ok. Then jumps to >=1 at x=1. 
# On [2,∞): f<=0. UP2 at b∈[2,∞): f(t)>f(b) ∀t>b. But also for b∈[1,2) (f>=1) and t∈[2,∞) (f<=0): t>b, 
#    is there constraint? UP1 at b? b in[1,2) f>=1: f(w)<=f(b) for w∈(0,b), w<b<2, doesn't include t>=2. 
#    Pair (t,b): f(t)<=0<=f(b), f(t)<=f(b) ⟹ D(b)⊆D(t). t∈[2,∞),b∈[1,2). 
#       d∈D(b): f(b+d)>f(b)>=1. ⟹ d∈D(t): f(t+d)>f(t). 
#       Take d with b+d∈[1,2)... or b+d where f>=1 and >f(b). Since f on[1,2) is 2^{x-1} increasing, 
#         d>0 small: b+d∈(b,2), f(b+d)=2^{b+d-1}>2^{b-1}=f(b) ✓ d∈D(b). 
#         then t+d: t>=2, t+d>2, f(t+d)=? if [2,∞) is <=0: f(t+d)<=0. >f(t)<=0? need f(t+d)>f(t). 
#         UP2 at t (f(t)<=0): f(t+d)>f(t) ∀d>0 ✓. so d∈D(t). OK no contra. 
#    Seems rise-then-permanent-fall might survive!! Let me CONSTRUCT & TEST exhaustively.
def f(x):
    if x<0: return 2.0**x
    if x==0: return 1.0
    if x<1: return -1.0+0.5*2.0**(x)   # (0,1): at0+:-0.5, at1-: 0... <=0? -1+0.5*2^x, 2^x<2 so <0. ✓ increasing
    if x<2: return 2.0**(x-1)          # [1,2): [1,2) >=1, increasing
    return -2.0+ 0.0*x                 # [2,inf): -2 <=0
# check cond2: (0,1) f<f(0)=1: f<=0<1 ✓
abgrid=[-3,-2,-1,-0.5,-0.1,0,0.2,0.5,0.8,1.0,1.3,1.6,1.9,2.0,2.5,3.0,4.0]
dgrid=[round(-9+18*i/3600,5) for i in range(3601)]
def cond1(f):
    bad=[]
    for a in abgrid:
        fa=f(a)
        for b in abgrid:
            if fa<=f(b)+1e-9:
                fb=f(b)
                for d in dgrid:
                    if f(b+d)>fb+1e-9 and not (f(a+d)>fa+1e-9):
                        bad.append((a,b,round(d,4),round(fa,3),round(fb,3)))
                        return False,bad[0]
    return True,None
print("rise-then-permanent-fall, cond1:", cond1(f))
print("cond2:", all(f(x)<1 for x in [0.1,0.5,0.9]))
