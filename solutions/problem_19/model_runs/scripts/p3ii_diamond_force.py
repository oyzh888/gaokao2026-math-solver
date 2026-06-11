import math
# (♦): ∀V∈(0,1), h>0: f(t)>V ⇒ f(t-h)>V·2^{-h}.
# Apply with t=x>0, and V just below f(x) IF f(x)∈(0,1). Take h=x (so t-h=0): 
#   f(x)>V ⇒ f(0)>V·2^{-x}.  As V->f(x)^- (f(x)<1): f(0)>=f(x)·2^{-x}. => f(x)<=f(0)·2^{x}.  upper bound, weak.
# Apply with t-h<0: let t=x>0, h>x so t-h=x-h<0, f(t-h)=2^{x-h}. (♦): f(x)>V ⇒ 2^{x-h}>V·2^{-h} ⇒ 2^x>V.
#   So f(x)>V ⇒ V<2^x. i.e. for all V∈(0,1) with V<f(x): V<2^x. => f(x)<=2^x OR f(x)>=1.
#   Precisely: if f(x)<1 then (taking V->f(x)) f(x)<=2^x... wait V<f(x) and conclude V<2^x for ALL such V 
#   means sup of such V = min(f(x),1) <= 2^x. So min(f(x),1)<=2^x. Since x>0, 2^x>1, so min(f(x),1)<=2^x always true. WEAK.
# Hmm (♦) only constrains via V<1. For x>0, 2^x>1 so it's loose.
#
# The REAL extra constraints come from pairs (a<0, b>0) and (a>0,b>0). Let me extract pair (a<0,b>0) when f(a)<=f(b).
# f(a)=2^a (a<0). f(b)=f(b). If 2^a<=f(b): D(b)⊆D(a).
#   D(a)={d:f(a+d)>2^a}. D(b)={d:f(b+d)>f(b)}.
#   D(b)⊆D(a): ∀d, f(b+d)>f(b) ⇒ f(a+d)>2^a.
# The failure we saw: d with b+d<0, f(b+d)=2^{b+d}>f(b) (so b+d > log2 f(b), and b+d<0); then need f(a+d)>2^a i.e. if a+d<0: 2^{a+d}>2^a i.e d>0. but d here = (neg)-b <0 => contradiction. 
# So: whenever f(b) < 1 (so that some negative argument exceeds it), there are d<0 in D(b) (landing negative), 
#   and these must be in D(a) for ALL a<0 with 2^a<=f(b). But d<0 with a+d<0 is NEVER in D(a). 
#   The ONLY escape: a+d>=0, i.e. d>=-a. But we can take a->0^- (a close to 0, still 2^a<=f(b) if f(b)<1... need 2^a<=f(b), a<=log2 f(b)<0). For a=log2 f(b) (so 2^a=f(b)), d>=-a=-log2 f(b)=log2(1/f(b))>0. But our problematic d<0 <that. CONTRADICTION unless NO such d<0 exists in D(b).
#   => For b>0 with f(b)<1: D(b) must contain NO negative d?? But d∈D(b) with b+d<0 needs 2^{b+d}>f(b) 
#      i.e. b+d>log2 f(b) i.e. d> log2 f(b) - b. Since f(b)<1, log2 f(b)<0. Is log2 f(b)-b <0? yes (both neg/neg). So there's a range d∈(log2 f(b)-b, -b) where b+d∈(log2 f(b),0), negative, giving d∈D(b) with d possibly NEGATIVE if log2 f(b)-b < d <0 i.e. need log2 f(b)-b<0 (yes) AND the interval (max(log2 f(b)-b,?),0) ... d<0 part is (log2 f(b)-b, 0)∩(...,-b). since -b<0, d<-b<0. interval (log2 f(b)-b, -b), all NEGATIVE (since -b<0). NONEMPTY (length b... = -b-(log2 f(b)-b)=-log2 f(b)>0). 
#   So D(b) ALWAYS contains negative d's when f(b)<1. These can't be in D(a) for a<0. CONTRADICTION with D(b)⊆D(a).
# THEREFORE: for ALL b>0, f(b) >= 1 = ... wait need 2^a<=f(b) to invoke. If f(b)<1, pick a=log2 f(b)+ε<0 close, 2^a slightly>f(b)? need 2^a<=f(b) so a<=log2 f(b). Take a=log2 f(b) exactly: 2^a=f(b), f(a)=f(b) (<=). Then D(b)⊆D(a). The negative d∈D(b) (just shown nonempty) must be in D(a): impossible. 
# ⇒ CONTRADICTION. Hence f(b)>=1 for all b>0?? But cond② says f(b)<f(0) on (0,1) and we'll get f(0)... 
# WAIT that contradicts cond②!! Let me recheck with numbers.
def chk(fb, b):
    if fb>=1: return "fb>=1 no neg-d issue"
    a=math.log2(fb)  # 2^a=fb, a<0
    # negative d in D(b): d in (log2(fb)-b, -b), check b+d in (log2 fb,0)
    d=(math.log2(fb)-b - b)/2  # midpoint-ish, ensure <0 and >log2fb-b
    lo=math.log2(fb)-b; hi=-b
    d=(lo+hi)/2
    return "fb=%.3f b=%.2f a=%.3f neg-d range=(%.3f,%.3f) sample d=%.3f b+d=%.3f"%(fb,b,a,lo,hi,d,b+d)
print(chk(0.58,0.25))
print(chk(0.7,0.5))
