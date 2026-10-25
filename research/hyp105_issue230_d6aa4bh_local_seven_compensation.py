"""AA4-BH: localized positive SEVEN-GF5 original sixflag compensation.

NEW scope: coefficientwise for EVERY fixed original W(3,2^h) f,g:
  S[P,L] = J[P,L] - AA[P,L] + T_D6[P,L]/12.
J is the doubly physical six-coordinate 2-regular join; AA is its
source-distinct A/A sector; T_D6 is the squarefree two-color trace from
#572. The scalar J-AA+D6 identity was already known in #534/#q:
the NEW mathematical output is its LOCAL two-physical-sixset coefficient
version with explicit source-factor square-zero projection and exact
finite W32/W34 independent localized ledgers. NOT root Branch A/B/C.

Finite code enumerates ORIGINAL source incidences with no random maps,
from an OCCUPIED given six-POINT-coordinate palette P. All original
LINE-image labels remain the SAME single completely fixed g.
"""
from collections import Counter,defaultdict
from itertools import combinations,combinations_with_replacement,product
from math import comb

from hyp105_issue230_d6aa4ay_quenched_allD_opposite_mean import _params
from hyp105_g5e2b3e1b0_seven_signature import R3_CERTIFIED_FLOORS


def _original_source(model):
    s=model["s"]
    V,a,_,_=_params(s)
    inc=tuple(tuple(p) for p in model["incidences"])
    f=tuple(tuple(sorted(p)) for p in model["left_labels"])
    g=tuple(tuple(sorted(p)) for p in model["right_labels"])
    if len(f)!=V or len(g)!=V or len(set(f))!=V or len(set(g))!=V:
        raise ValueError("original point and LINE maps must be complete and globally injected")
    if any(len(e)!=2 or e[0]==e[1] or min(e)<0 or max(e)>=a for e in f+g):
        raise ValueError("invalid original physical pair-edge coordinates")
    d=s+1
    if len(inc)!=V*d or len(set(inc))!=len(inc):
        raise ValueError("all actual original incidence flag IDs must be unique")
    point=[[ ] for _ in range(V)]
    line=[[ ] for _ in range(V)]
    point_neighbours=[set() for _ in range(V)]
    for idx,(p,l) in enumerate(inc):
        if type(p) is not int or type(l) is not int or p<0 or l<0 or p>=V or l>=V:
            raise ValueError("original incidence ID source factor index out of range")
        point[p].append(idx)
        line[l].append(idx)
        point_neighbours[p].add(l)
    if any(len(q)!=d for q in point+line):
        raise ValueError("true source incidence factor degree must be d")
    if any(len(point_neighbours[p]&point_neighbours[q])>1
           for p in range(V) for q in range(p+1,V)):
        raise ValueError("actual W(3,s) original source GQ C4-freeness violated")
    return s,V,a,inc,f,g,point,line


def physical_sixmask_of_original_flags(ids,inc,g):
    """Check exactly SIX typed physical coordinates each appearing twice."""
    degrees=Counter()
    for j in ids:
        l=inc[j][1]
        u,v=g[l]
        degrees[u]+=1
        degrees[v]+=1
    if len(degrees)!=6 or any(v!=2 for v in degrees.values()):
        return None
    return tuple(sorted(degrees))


def _source_kind(ids,inc,side):
    multiplicities=tuple(sorted(Counter(inc[j][side] for j in ids).values()))
    return {(1,1,1,1,1,1):"A",(1,1,1,1,2):"B",(2,2,2):"C"}.get(multiplicities)


def _D6_dual_compatible(ids,inc,f,g):
    """Independent source-order cyclic incidence dual; no colored-D trace."""
    duals=[]
    for side,labels in ((0,f),(1,g)):
        stars=defaultdict(list)
        for i,j in enumerate(ids):
            for c in labels[inc[j][side]]:
                stars[c].append(i)
        if len(stars)!=6 or any(len(v)!=2 for v in stars.values()):
            raise AssertionError("physical six-coordinate two-regular precondition missing")
        dual=tuple(sorted(tuple(v) for v in stars.values()))
        duals.append(dual)
    if duals[0]!=duals[1]:
        return False
    adjacency=[[] for _ in range(6)]
    for u,v in duals[0]:
        adjacency[u].append(v)
        adjacency[v].append(u)
    if any(len(x)!=2 for x in adjacency):
        raise AssertionError("true six-position physical dual not 2regular")
    reached={0}
    while True:
        additions={v for i in tuple(reached) for v in adjacency[i]}-reached
        if not additions:break
        reached|=additions
    return len(reached)==6


def _physical_point_2factors(P,support):
    """Independent six-coordinate typed physical SOURCE-multigraph census.

    Degree two on each of exactly SIX physical POINT coordinates, source
    edges repeated at most twice. No synthetic original W graph.
    """
    possible=tuple(e for e in combinations(P,2) if e in support)
    for edges in combinations_with_replacement(possible,6):
        deg=Counter(v for e in edges for v in e)
        if len(deg)==6 and all(deg[u]==2 for u in P):
            yield edges


def localized_original_seven_fiber(model,P,*,collect_witnesses=8):
    """Exact selected seven GF5 counts by RIGHT six-physical-coordinate L.

    Enumerate REAL original flags over six physical POINT coordinates P.
    No RIGHT physical image remapping, no fake source factors, no sampling.
    """
    s,V,a,inc,f,g,p_src,l_src=_original_source(model)
    P=tuple(P)
    if len(P)!=6 or len(set(P))!=6 or any(type(c) is not int or not 0<=c<a for c in P):
        raise ValueError("six distinct real original POINT physical coordinates required")
    P=tuple(sorted(P))
    phys={e:p for p,e in enumerate(f)}
    records=defaultdict(lambda:dict(join=0,AA=0,D6=0,
        tags=Counter(),cross=Counter(),weighted_GF5_numerator=0,
        examples=[]))
    left_count=Counter()
    candidates=0
    point_patterns=Counter()
    for physical_edges in _physical_point_2factors(P,set(phys)):
        factor_mult=Counter(phys[e] for e in physical_edges)
        mult=tuple(sorted(factor_mult.values()))
        if mult==(1,1,1,1,1,1):kind="A"
        elif mult==(1,1,1,1,2):kind="B"
        elif mult==(2,2,2):kind="C"
        else:raise AssertionError("complete 2-regular six physical coords must be A,B,C")
        point_patterns[kind]+=1
        buckets=[]
        for p,mult in sorted(factor_mult.items()):
            if mult==1:buckets.append(tuple((j,) for j in p_src[p]))
            else:
                if mult!=2:raise AssertionError("source factor repeated >twice")
                buckets.append(tuple(combinations(p_src[p],2)))
        for choices in product(*buckets):
            ids=tuple(sorted(j for group in choices for j in group))
            if len(ids)!=6 or len(set(ids))!=6:
                raise AssertionError("six DIFFERENT actual ORIGINAL incidence flag IDs")
            candidates+=1
            left_count[kind]+=1
            L=physical_sixmask_of_original_flags(ids,inc,g)
            if L is None:
                continue
            rightkind=_source_kind(ids,inc,1)
            if rightkind not in ("A","B","C"):
                raise AssertionError("true original LINE 2regular source partition")
            entry=records[L]
            entry["join"]+=1
            entry["cross"][(kind,rightkind)]+=1
            if kind=="A" and rightkind=="A":
                entry["AA"]+=1
                tag=("D6" if _D6_dual_compatible(ids,inc,f,g) else None)
                if tag:entry["D6"]+=1
            elif kind=="C" and rightkind=="C":
                raise AssertionError("genuine W3 GQ forbidden source C/C six-incidence cycle")
            elif (kind,rightkind)==("B","A"):tag="B-left/A-right"
            elif (kind,rightkind)==("A","B"):tag="A-left/B-right"
            elif "C" in (kind,rightkind) and "A" in (kind,rightkind):tag="C/A"
            elif "C" in (kind,rightkind) and "B" in (kind,rightkind):tag="C/B"
            elif (kind,rightkind)==("B","B"):
                p_repeat=next(p for p,n in Counter(inc[j][0] for j in ids).items() if n==2)
                l_repeat=next(l for l,n in Counter(inc[j][1] for j in ids).items() if n==2)
                pp={j for j in ids if inc[j][0]==p_repeat}
                ll={j for j in ids if inc[j][1]==l_repeat}
                overlap=len(pp&ll)
                if overlap>1:
                    raise AssertionError("genuine source GQ B/B overlap >1")
                tag="B/B-overlap" if overlap else "B/B-disjoint"
            else:
                raise AssertionError("all non-AA non-CC original source joins must be seven-positive")
            if tag:
                entry["tags"][tag]+=1
                entry["weighted_GF5_numerator"]+=R3_CERTIFIED_FLOORS[tag]
                if len(entry["examples"])<collect_witnesses:
                    entry["examples"].append((ids,tag))
    expected=sum(left_count.values())
    if expected!=candidates:
        raise AssertionError("unilateral original flag generation lost candidate")
    result={}
    for L,v in records.items():
        J=v["join"]; AA=v["AA"]; T=12*v["D6"]
        S=sum(v["tags"].values())
        if S!=J-AA+T//12 or v["cross"].get(("C","C"),0):
            raise AssertionError("coefficientwise original seven-class compensation failed")
        result[L]={"physical_P":P,"physical_L":L,
                   "two_sided_join_coefficient":J,
                   "AA_squarefree_source_factor_coefficient":AA,
                   "original_D6_squarefree_sixtrace_coefficient":T,
                   "original_D6_from_trace":v["D6"],
                   "seven_GF5_positive_coefficient":S,
                   "compensator_non_AA":J-AA,
                   "all_seven_GF5_tags":dict(v["tags"]),
                   "source_3by3_A_B_C_cells":
                       {f"{x}/{y}":n for (x,y),n in v["cross"].items()},
                   "GF5_51palette_certified_weighted_numerator":
                       v["weighted_GF5_numerator"],
                   "sample_true_original_sixflag_sets":tuple(v["examples"])}
    return {
        "s":s,"a":a,"V":V,"physical_P":P,
        "point_sixcoord_physical_patterns":dict(point_patterns),
        "point_side_true_original_sixflag_candidates_by_type":dict(left_count),
        "point_side_true_original_sixflag_candidates":candidates,
        "local_right_physical_fibers":result,
        "exact_coefficientwise_J_minus_AA_plus_trace_over_12":True,
        "all_h_mathematical_identity_but_this_is_finite_source_census":True,
        "all_fixed_f_g_seven_lower_NOT_PROVED":True,
        "branch_C_full_equivalence_NOT_CLAIMED":True,
        "root_230":"OPEN_WITH_FORMAL_BLOCKER"}


def dyadic_all_h_seven_coefficient_scope(s):
    """Formal symbolic all-h scope, NEVER a fabricated W(3,s) incidence."""
    if type(s) is not int or s<2 or s&(s-1):
        raise ValueError("actual dyadic source order only")
    V,a,K,m=_params(s)
    return {
        "s":s,"h":s.bit_length()-1,"V":V,"a":a,"m":m,
        "full_original_W3_incidence_required":True,
        "H_join":"[t^6 x_P^2 y_L^2] PROD_(p,l) original (1+t*x_f(p)*y_g(l))",
        "H_AA":"same coefficient with source z_p^2=w_l^2=0 and sum over z,w source monomials",
        "D6":"[x_P*y_L] Tr_(squarefree physical coordinates)(A_D^6)/12",
        "seven_fiber_exact_identity":"S[P,L]=J[P,L]-AA[P,L]+D6[P,L]",
        "positive_compensation_channels":"J-AA>=0, D6>=0 coefficientwise",
        "this_does_NOT_prove_omega_s6_for_ALL_fixed_f_g":True,
        "not_root_Branch_A_or_B_or_accepted_C":True,
        "root_230":"OPEN_WITH_FORMAL_BLOCKER"}
