import math
# I'll now VERIFY the rigorous proof of monotonicity directly from axioms via the contrapositive (★),
# testing that the implication chain is valid (no f needed — pure logic check on the inequalities).
#
# THEOREM: 0<u<v ⇒ f(u)<f(v).
# Proof by contradiction: assume f(u)>=f(v) for some 0<u<v. Then f(v)<=f(u), so by ①: D(u)⊆D(v).  (I)
# We exhibit d* ∈ D(u)\D(v), contradicting (I).
#
# Construct d* using a NEGATIVE landing for the u-side:
#   For ε>0 small, let d = -u - ε  (so u+d = -ε <0). Then f(u+d)=2^{-ε}.
#   d∈D(u) ⟺ 2^{-ε} > f(u).   ... requires f(u)<1.
#   AND v+d = v-u-ε. d∉D(v) ⟺ f(v+d) <= f(v).
# This needs f(u)<1. So split:
#
# CASE 1: f(u) < 1.
#   Choose ε>0 with 2^{-ε}>f(u) (possible since f(u)<1, take ε< -log2 f(u); if f(u)<=0 any ε works).
#   Then d=-u-ε ∈ D(u). Need d∉D(v): f(v+d)=f(v-u-ε)<=f(v).
#   Sub-pick ε also so that v-u-ε is handled. We can ALSO push ε so v+d<0: ε>v-u ⇒ v+d<0, f(v+d)=2^{v+d}<1.
#     Then need 2^{v+d}<=f(v). If f(v)>=1: 2^{v+d}<1<=f(v) ✓ d∉D(v). 
#     If f(v)<1: need 2^{v-u-ε}<=f(v) ⟺ v-u-ε<=log2 f(v) ⟺ ε>=v-u-log2 f(v). achievable (ε large). ✓
#   So in CASE 1 we need BOTH: ε< -log2 f(u) (for d∈D(u))  AND  ε>=max(v-u, v-u-log2 f(v)) (for d∉D(v)).
#   Compatible iff -log2 f(u) > v-u-log2 f(v) ... i.e. log2 f(v) - log2 f(u) > v-u... hmm needs f(v)/f(u) related.
#   This is getting tangled. Let me just NUMERICALLY verify CASE-based existence of d* for the assumed 
#   bad config f(u)>=f(v), scanning d over reals, for arbitrary (u,v,f(u),f(v)) consistent with axioms.
# Actually cleaner: scan d directly. Given the WHOLE f is unknown, the cleanest rigorous proof uses the 
# spike at 0 / negative structure. Let me VERIFY the final clean version below.
print("Switching to the clean spike-based proof — verifying numerically.")

# CLEAN PROOF (verify the inequality logic):
# Lemma M: for any p with f(p)<1 and any q, if f(q)<=f(p) and p,q satisfy..., 
# Let me just confirm the KEY lemma that powers everything:
# LEMMA: for x>0, f(x) >= f(0).   [i.e. f(x)>=f(0)>=1 for all x>0]  -- TEST if this is forced & consistent.
# Test consistency with cond②: cond② says f(x)<f(0) on (0,1). LEMMA says f(x)>=f(0). CONTRADICTION on (0,1).
# So LEMMA false. So f(x)<f(0) possible. 
# Therefore the spike argument must allow f(b)<f(0) for b near 0. Reconcile: the spike d=-b∈D(b) needs f(0)>f(b) TRUE on (0,1). Then anchor a<0 fails. So how is cond① satisfiable AT ALL on (0,1)?!
# Unless: for b∈(0,1), there's NO a<0 with f(a)<=f(b) AND ... a=log2 f(b) needs f(b)>0. If f(b)<=0, no such a. 
#   => for b∈(0,1) with f(b)>0: spike d=-b∈D(b)\D(a) where a=log2 f(b). CONTRADICTION.
#   => for b∈(0,1): f(b)<=0 !!  (can't be in (0,f(0))positive)
# CHECK: does d=-b really ∈D(b)? f(b+(-b))=f(0)>f(b)? on (0,1) f(b)<f(0) by②. YES. and need f(b)>0 to define a=log2 f(b)<0 with f(a)=f(b)<=f(b)✓. Then a+(-b)=a-b<a<0 wait a-b: a<0,b>0 so a-b<0, f=2^{a-b}<2^a=f(a). so -b∉D(a). 
#   => d=-b ∈ D(b)\D(a). VIOLATES D(b)⊆D(a). 
# So for b∈(0,1): f(b)>0 is IMPOSSIBLE. Hence f(b)<=0 on (0,1). Combined cond②(auto). 
print("RIGOROUS: for b∈(0,1), f(b)<=0. (else spike d=-b lands on f(0)>f(b), unmatched by a=log2 f(b)<0)")
# verify the inequalities:
fb=0.3; b=0.5; a=math.log2(fb)
print("ex: b=0.5,f(b)=0.3>0. a=log2(0.3)=%.3f. d=-b=-0.5. f(b+d)=f(0)>=1>0.3 ✓∈D(b). a+d=%.3f<a, 2^{a+d}=%.3f<2^a=0.3 ✗∉D(a). violation confirmed."%(a,a-b,2**(a-b)))
