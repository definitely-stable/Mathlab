"""Independent TRUE W(3,4)/W(3,8) symplectic-spread hard-case maps for JPKC.

Reconstruct D4's mathematical all-h star construction from first principles;
do NOT import the unmerged D4 PR/D3 auxiliary energy implementation.
This is a FINITE original-GQ stress fixture, not an all-h proof in Python.
"""
from itertools import combinations
from math import comb

from hyp105_b1_symplectic import symplectic_gq, normalized
from hyp105_issue230_proof_audit import parameters, _model


def _irreducible_c(field):
    for c in range(1,field.q):
        if all(field.mul(z,z)^field.mul(c,z)^1 for z in range(field.q)):
            return c
    raise AssertionError("symplectic symmetric irreducible pencil not found")


def spread_adversary_model(power):
    if power not in (2,3):
        raise ValueError("supported true original finite symplectic spread powers 2/3 only")
    field,points,lines,incidences=symplectic_gq(power)
    s=field.q
    data=parameters(s)
    a,V=data["a"],data["V"]
    if len(points)!=V or len(lines)!=V:
        raise AssertionError("original W(3,s) cardinality inconsistent")
    c=_irreducible_c(field)
    p_index={p:i for i,p in enumerate(points)}
    l_index={tuple(line):i for i,line in enumerate(lines)}
    reps=[(1,z) for z in range(s)]+[(0,1)]
    spread=[]
    for b in range(s):
        for d in range(s):
            pts=[]
            for x0,x1 in reps:
                y0=field.mul(b,x0)^field.mul(d,x1)
                y1=field.mul(d,x0)^field.mul(b^field.mul(c,d),x1)
                pts.append(p_index[normalized((x0,x1,y0,y1),field)])
            spread.append(l_index[tuple(sorted(pts))])
    vertical=tuple(sorted(p_index[normalized((0,0,x0,x1),field)]
                          for x0,x1 in reps))
    spread.append(l_index[vertical])
    if len(set(spread))!=s*s+1:
        raise AssertionError("actual symplectic spread repeated an original line")
    used_points=[p for l in spread for p in lines[l]]
    if sorted(used_points)!=list(range(V)):
        raise AssertionError("spread must partition all true ORIGINAL GQ points")

    anchors=a//4
    other=a-anchors
    per_anchor=other//(2*(s+1))
    count=anchors*per_anchor
    if not 0<count<=len(spread) or per_anchor*(s+1)>other:
        raise AssertionError("D4 star grouping palette capacity")
    left=[None]*V
    for anchor in range(anchors):
        selected=[p for l in spread[anchor*per_anchor:(anchor+1)*per_anchor]
                  for p in lines[l]]
        if len(selected)!=per_anchor*(s+1) or len(set(selected))!=len(selected):
            raise AssertionError("spread lines selected twice")
        for j,p in enumerate(selected):
            if left[p] is not None:
                raise AssertionError("original point twice in star blocks")
            left[p]=(anchor,anchors+j)
    first={e for e in left if e is not None}
    if len(first)!=count*(s+1):
        raise AssertionError("original selected pair map not injective")
    available=iter(e for e in combinations(range(a),2) if e not in first)
    for p in range(V):
        if left[p] is None:
            left[p]=next(available)
    if len(set(left))!=V:
        raise AssertionError("globally completed original f map not injective")
    excess=comb(a,2)-V
    if not 0<=excess<a-1:
        raise AssertionError("nonminimal physical alphabet")
    skipped={tuple(sorted((i,(i+1)%a))) for i in range(excess)}
    right=tuple(e for e in combinations(range(a),2) if e not in skipped)
    if len(right)!=V or len(set(right))!=V:
        raise AssertionError("globally completed original g map not injective")
    stars=[0]*a
    for u,v in right:
        stars[u]+=1
        stars[v]+=1
    if min(stars)<a-3:
        raise AssertionError("balanced original right star condition failed")

    Mf=0
    for line in lines:
        for p,q in combinations(line,2):
            if set(left[p]).intersection(left[q]):
                Mf+=1
    floor=count*comb(s+1,2)
    if Mf<floor:
        raise AssertionError("actual ORIGINAL collinearity pencil lower violated")
    model=_model(s,points,lines,incidences,left,right)
    certificate={
        "s":s,"power":power,"original_spread_lines":len(spread),
        "selected_spread_lines":count,
        "selected_original_points":count*(s+1),
        "M_f_original_exact":Mf,"M_f_D4_floor":floor,
        "original_right_min_degree":min(stars),
        "all_h_asymptotic_statement_from_D4_only":True,
        "root_S_small_counterfamily_constructed":False,
    }
    return model,certificate
