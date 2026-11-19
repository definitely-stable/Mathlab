"""Independent third-construction FULL-A/CORE-C mixed-source book contraction.

This module does NOT call the old or new literal source-key generators.
It computes R_A,R_C,K_AC, original SRG-collinear Gram, F1/F2 and
physically sourced theta through distinct algorithms on real original
W(3,s), then verifies the exact inherited #737 source proof inequalities.
K is the ACTUAL induced ORIGINAL source-pencil conflict maximum for the
diagnostic paired core, never an invented uniform K=10.
"""
from collections import Counter,defaultdict
from itertools import combinations


def independent_source_mixed_contractions(source,gq,physical):
    flags=source["flags"]
    f,g=source["f"],source["g"]
    A=sorted(source["A"]);C=sorted(source["C"])
    J={i:set() for i in C}
    for i,j in combinations(C,2):
        p,l=flags[i];q,r=flags[j]
        if ((p==q and set(g[l])&set(g[r])) or
            (l==r and set(f[p])&set(f[q]))):
            J[i].add(j)
            J[j].add(i)
    K=max((len(z) for z in J.values()),default=0)
    answer={}
    for typ in ("x","y"):
        if typ=="x":
            outer,inner=f,g
            outidx,inidx=0,1
            col=gq["point_col"]
        else:
            outer,inner=g,f
            outidx,inidx=1,0
            col=gq["line_col"]
        RA=Counter()
        RC=Counter()
        for i in A:
            factor=flags[i]
            for y in inner[factor[inidx]]:
                RA[factor[outidx],y]+=1
        for i in C:
            factor=flags[i]
            for y in inner[factor[inidx]]:
                RC[factor[outidx],y]+=1
        for p in range(source["V"]):
            if sum(RA[p,y] for y in range(source["a"]))>2*(source["s"]+1):
                raise AssertionError("FULL source R_A physical symbol total > original pencil")
        max_RC=max(RC.values(),default=0)
        if max_RC>K+1:
            raise AssertionError("real source R_C symbol fibre exceeds J_C clique")
        inv=defaultdict(list)
        for p,pair in enumerate(outer):
            for x in pair:inv[x].append(p)
        def col_count(p,x):
            return sum(x in outer[q] for q in col[p])
        Gram=sum(col_count(p,x)**2
                 for p in range(source["V"]) for x in range(source["a"]))
        B=F1=F2=theta=0
        for u in set(flags[i][outidx] for i in C):
            pair=outer[u]
            for x,k in ((pair[0],pair[1]),(pair[1],pair[0])):
                for p in inv[k]:
                    c=col_count(p,x)
                    kac=sum(RA[p,y]*RC[u,y] for y in range(source["a"]))
                    if kac>2*(source["s"]+1)*(K+1):
                        raise AssertionError("actual source K_AC cap invalid")
                    B+=c*kac
                    theta+=kac
                    F1+=c*c
                    F2+=kac*kac
        if not (theta==physical["theta"]
                and B*B<=F1*F2
                and F1<=2*Gram
                and F2<=2*(source["s"]+1)*(K+1)*theta
                and theta<=4*len(A)*physical["Delta"]
                and B*B<=16*(source["s"]+1)*(K+1)*len(A)*
                         physical["Delta"]*Gram):
            raise AssertionError("literal ORIGINAL FULL-A CORE-C SRG F1 F2 theta fail")
        answer[typ]=dict(
            historical_book_independent_multiplicity=B,
            full_allowed_SOURCE_and_CORE_physical_theta=theta,
            actual_original_induced_source_J_max_K=K,
            source_F1=F1,source_F2=F2,
            true_original_SR_G_collinearity_Gram=Gram,
            actual_CORE_symbol_clique_max=max_RC,
            distinct_original_source_mixed_SRG_Gram_F1_F2_theta_proof_passed=True)
    return answer
