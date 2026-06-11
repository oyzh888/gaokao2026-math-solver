# Reason about (3i): f(x)=2^x for x<0. Condition (2): 0<x<1 => f(x)<f(0).
# Want f(0)>=1.
# Key tool: note for x<0, f(x)=2^x in (0,1), strictly increasing, sup ->1 as x->0-.
# Suppose f(0)=c. Want c>=1.
# Idea: use d in D sets. Take x1=0? D(0)={d: f(d)>f(0)=c}.
# Consider negative arguments approaching 0: f(x)=2^x close to 1.
# Suppose c<1. Pick x<0 with 2^x in (c,1), i.e. f(x)>c=f(0). Then f(0)<f(x) => f(0)<=f(x) => by (1): D(x) subset D(0).
# D(x) for x<0: {d: f(x+d)>f(x)=2^x}. d slightly... contains small positive d? f(x+d) for x+d still<0: 2^{x+d}>2^x iff d>0. So (0, -x) subset D(x) at least for the part staying negative. Actually for 0<d<-x, x+d<0, 2^{x+d}>2^x. yes. So (0,-x) ⊆ D(x).
# Then D(x) ⊆ D(0) means (0,-x) ⊆ D(0) = {d: f(d)>c}.
# For d in (0,-x) with d possibly >=... if d in (0,1): f(d)<f(0)=c by condition(2)! so f(d)<c => d NOT in D(0). Contradiction if (0,-x) intersects (0,1).
# choose x in (-1,0) with 2^x>c. Then -x in (0,1), so (0,-x) subset (0,1). Every d there has f(d)<c, contradicting (0,-x)⊆D(0).
# Such x exists iff there's x in (-1,0) with 2^x>c, i.e. c<2^x for some x in(-1,0) => c< sup=1 (approached). If c<1 pick x close to 0. CONTRADICTION.
# Hence c>=1. 
print("Logic check: need x in (-1,0) with 2^x > c, possible iff c<1 (since 2^x->1).")
# numeric demonstrate the contradiction quantity
c=0.9
import math
x=math.log2((c+1)/2)  # 2^x=(c+1)/2 in (c,1), and is x in (-1,0)? 
print("c=",c,"x=",x,"2^x=",2**x,"x in(-1,0)?",-1<x<0,"-x in(0,1)?",0<-x<1)
