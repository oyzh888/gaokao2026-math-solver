import math
# (♦): ∀V∈(0,1), h>0: f(t)>V ⇒ f(t-h)>V·2^{-h}.
# This DOES constrain positives! Apply with t>0 where f(t)>=1 (so f(t)>V for ALL V<1), and t-h>0:
#   f(t-h) > V·2^{-h} for all V<1 ⟹ f(t-h) >= 2^{-h} (sup V=1).  
#   So: if f(t)>=1 (t>0), then for any h∈(0,t): f(t-h) >= 2^{-h} > 0.  
#   ⟹ f(s) >= 2^{-(t-s)} >0 for all s∈(0,t).  By BAND f(s)∈(-∞,0]∪[1,∞), and f(s)>0 ⟹ f(s)>=1!
#   ⟹ if f(t)>=1 (t>0) then f(s)>=1 for ALL s∈(0,t).   (POS-LEMMA, very strong!)
print("POS-LEMMA: f(t)>=1 (t>0) ⟹ f(s)>=1 ∀s∈(0,t).  [via (♦): f(s)>=2^{-(t-s)}>0, then BAND]")
# verify the (♦) step numerically with the rise-fall f:
def f(x):
    if x<0: return 2.0**x
    if x==0: return 1.0
    if x<1: return -1.0+0.5*2.0**(x)
    if x<2: return 2.0**(x-1)
    return -2.0
# t=1.5 (f=2^0.5=1.41>=1), s=0.005: POS-LEMMA demands f(0.005)>=1. actual:
print("t=1.5 f=%.3f>=1. s=0.005 f(s)=%.3f. POS-LEMMA needs >=1 -> VIOLATED, so f invalid."%(f(1.5),f(0.005)))
# Now POS-LEMMA changes everything:
# Define the positive set is "downward closed toward 0" for >=1: if f>=1 at t, then f>=1 on all (0,t].
# So {x>0: f(x)>=1} = (0, M) or (0,M] for some M∈[0,∞] (an initial interval from 0!). 
# And {x>0: f(x)<=0} = [M,∞) region (the tail). 
# BUT cond②: 0<x<1 ⟹ f(x)<f(0). f(0)>=1. If f(x)>=1 on (0,M)⊇(0,1) when M>=1...
#   Then on (0,1), f(x)>=1 AND f(x)<f(0). OK if f(0)>f(x)>=1. 
#   If M<=... hmm. Actually let's just get monotonicity now.
print()
print("So {f>=1}∩(0,∞)=(0,M) initial interval; {f<=0}=[M,∞) tail (M∈[0,∞]).")
