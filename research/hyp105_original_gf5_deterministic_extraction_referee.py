"""AA4-DETG5: deterministic original-GF5 sixflag assignment by exact conditioning.

For any finite DISTINCT ORIGINAL selected D6 / produced aligned BBo
source-sixset family on the SAME fixed globally injected f,g:
  E[number of signed events] =
     (54162 * #D6 + 53838 * #produced BBo) / 51**6.

A fixed 51-valued checksum-4 palette per ORIGINAL source flag can be
chosen greedily by EXACT conditional expectations, never assuming
independence of overlapping sixsets. The resulting event count is no
more than that expectation. If the numerator <51**6 it is EXACTLY zero.
We validate actual W(3,2) / W(3,4) source IDs; no synthetic flags.

The completion-counter is a new ORIGINAL source-coordinate affine
GF(5) inclusion-exclusion with fixed column palettes and residual
per-component Kirchhoff demands. It does not import previous GF5 flow
solvers. It never enumerates 51**6 full assignments.
"""
from collections import Counter,defaultdict
from fractions import Fraction
from itertools import combinations, product
from math import comb, isqrt

from hyp105_full_physical_degree_tail import genuine_source


PALETTES=tuple(x for x in product(range(1,5),repeat=4) if sum(x)%5==4)
SIGNS=tuple(frozenset((0,i,j)) for i,j in combinations(range(1,6),2))
DENOM=51**6
WEIGHTS={"D6":54162,"BBo-produced":53838}
assert len(PALETTES)==51 and len(SIGNS)==10


def _minimal_alphabet(v):
    a=(1+isqrt(1+8*v))//2
    while comb(a,2)<v:a+=1
    while a>2 and comb(a-1,2)>=v:a-=1
    return a


def _check_source(power,f,g):
    if type(power) is not int or power not in (1,2):
        raise ValueError("finite ORIGINAL source fixture only genuine W32/W34")
    s,v,flags=genuine_source(power)
    a=_minimal_alphabet(v)
    legal=set(combinations(range(a),2))
    try:
        f=tuple(tuple(t) for t in f)
        g=tuple(tuple(t) for t in g)
    except (TypeError,ValueError) as exc:
        raise ValueError("missing complete fixed original source maps") from exc
    if (len(f)!=v or len(g)!=v or len(set(f))!=v
        or len(set(g))!=v or any(t not in legal for t in f+g)):
        raise ValueError("complete separately globally pair-injective maps required")
    return (s,v,tuple(flags),f,g)


def _is_named_c6(edges):
    if len(edges)!=6 or len(set(edges))!=6:
        return False
    adj=[set() for _ in range(6)]
    for i,j in edges:
        if i==j:return False
        adj[i].add(j);adj[j].add(i)
    if any(len(z)!=2 for z in adj):
        return False
    reached={0}
    todo=[0]
    while todo:
        for v in adj[todo.pop()]:
            if v not in reached:
                reached.add(v);todo.append(v)
    return len(reached)==6


def _source_coordinate_edges(flags,ids,f,g):
    """Twelve pairs (column i, coefficient slot, column j, slot)."""
    physical=[]
    byside=[]
    for side,labels in ((0,f),(1,g)):
        occupied=defaultdict(list)
        for j,id_ in enumerate(ids):
            factor=flags[id_][side]
            for slot,coordinate in enumerate(labels[factor]):
                occupied[coordinate].append((j,2*side+slot))
        if len(occupied)!=6 or any(len(z)!=2 for z in occupied.values()):
            raise ValueError("not 6 physical coordinates of degree two per type")
        pairs=[]
        for coordinate in sorted(occupied):
            first,last=sorted(occupied[coordinate])
            if first[0]==last[0]:
                raise ValueError("physical loop in ORIGINAL dual")
            physical.append((first[0],first[1],last[0],last[1]))
            pairs.append((first[0],last[0]))
        byside.append(tuple(sorted(pairs)))
    if len(physical)!=12:
        raise AssertionError("incorrect true original 12 physical coordinates")
    return tuple(physical),tuple(byside)


def _middle_of_named_c4(edges,anchor):
    if len(edges)!=4 or len(set(edges))!=4:
        raise ValueError("ORIGINAL BBo remainder not simple C4")
    adjacent=defaultdict(set)
    for u,v in edges:
        if u==v:raise ValueError("original C4 contains a loop")
        adjacent[u].add(v);adjacent[v].add(u)
    if len(adjacent)!=4 or anchor not in adjacent or any(
            len(z)!=2 for z in adjacent.values()):
        raise ValueError("BBo original C4 has incorrect degrees")
    opposite=set(adjacent)-{anchor}-adjacent[anchor]
    if len(opposite)!=1:
        raise AssertionError("original middle source ID not unique")
    return next(iter(opposite))


def _classify_original_sixset(flags,ids, f,g, pencils, edges_by_side):
    from collections import Counter
    six=tuple(flags[i] for i in ids)
    pc=Counter(p for p,_ in six)
    lc=Counter(l for _,l in six)
    left,right=edges_by_side
    if (len(pc)==6 and len(lc)==6
        and _is_named_c6(left) and left==right):
        return "D6"
    if (sorted(pc.values())!=[1,1,1,1,2]
        or sorted(lc.values())!=[1,1,1,1,2]):
        raise ValueError("family allows only genuine D6 or aligned ORIGINAL BBo")
    p=next(k for k,v in pc.items() if v==2)
    ell=next(k for k,v in lc.items() if v==2)
    root=[i for i in ids if flags[i]==(p,ell)]
    left_anchor=[i for i in ids if flags[i][0]==p and flags[i][1]!=ell]
    right_anchor=[i for i in ids if flags[i][1]==ell and flags[i][0]!=p]
    if not (len(root)==len(left_anchor)==len(right_anchor)==1):
        raise ValueError("not overlapping ORIGINAL repeated point and line flags")
    q=flags[right_anchor[0]][0]
    r=flags[left_anchor[0]][1]
    if r in pencils[q]:
        raise ValueError("ORIGINAL q,r incident: no nonincident FULL projection")
    middle=tuple(sorted(set(ids)-set(root+left_anchor+right_anchor)))
    ordered=tuple(root+left_anchor+right_anchor)+middle
    _,(canonical_l,canonical_r)=_source_coordinate_edges(flags,ordered,f,g)
    if (canonical_l.count((0,1))!=2 or
        canonical_r.count((0,2))!=2):
        raise ValueError("false original double-anchor BBo source projection")
    lc4=tuple(e for e in canonical_l if e!=(0,1))
    rc4=tuple(e for e in canonical_r if e!=(0,2))
    if not (len(lc4)==len(rc4)==4
            and set(v for edge in lc4 for v in edge)=={2,3,4,5}
            and set(v for edge in rc4 for v in edge)=={1,3,4,5}):
        raise ValueError("not the two genuine ORIGINAL BBo physical C4 remainders")
    left_middle=_middle_of_named_c4(lc4,2)
    right_middle=_middle_of_named_c4(rc4,1)
    if left_middle!=right_middle:
        raise ValueError("unaligned BBo does not arise via a physical 3-path")
    return "BBo-produced"


def prepare_original_family(power, f,g, sextuples):
    """Finite list of genuine ORIGINAL six-flag motifs on the SAME fixed maps.

    The list is a selected subfamily. There is NO implication that every
    accepted ORIGINAL sixset of the entire true GQ is in the list.
    """
    s,v,flags,f,g=_check_source(power,f,g)
    pencils=[set() for _ in range(v)]
    for p,l in flags:pencils[p].add(l)
    try: raw=tuple(tuple(q) for q in sextuples)
    except (TypeError,ValueError) as exc:
        raise ValueError("missing ORIGINAL sixsets") from exc
    out=[]
    seen=set()
    for q in raw:
        if (len(q)!=6 or
            any(type(i) is not int or not 0<=i<len(flags) for i in q)
            or len(set(q))!=6):
            raise ValueError("six DISTINCT genuine ORIGINAL source flag IDs required")
        ids=tuple(sorted(q))
        if ids in seen:raise ValueError("duplicate ORIGINAL sextuple")
        seen.add(ids)
        edges,sides=_source_coordinate_edges(flags,ids,f,g)
        kind=_classify_original_sixset(flags,ids,f,g,pencils,sides)
        out.append({"ids":ids,"edges":edges,"kind":kind})
    return {"s":s,"V":v,"original_flags":flags,"f":f,"g":g,
            "motifs":tuple(sorted(out,key=lambda m:m["ids"]))}


def _completion_count(edges, plus, fixed_cols):
    """Count assignments to remaining 51-palettes with one signed event.

    GF(5) incidence currents x on physical coordinate edges:
    B*x=4*sigma and x!=0. Fixed palettes determine all incident x.
    On the unassigned-to-unassigned edges the residual Kirchhoff
    demands form an independent affine GF(5) source constraint.

    IE over only the unassigned-to-unassigned edges: for a selected
    subset A, allow its x in GF(5), zero all other unassigned x.
    This gives 5^(|A|-u+c) solutions iff each connected component has
    total residual demand 0 mod 5. Thus exact integer signed count,
    with no brute force 51^(#remaining) and no external flow oracle.
    """
    fixed=dict(fixed_cols)
    if any(i not in range(6) or p not in PALETTES for i,p in fixed.items()):
        raise ValueError("invalid fixed ORIGINAL palette")
    signs=tuple(1 if i in plus else -1 for i in range(6))
    unassigned=tuple(i for i in range(6) if i not in fixed)
    local={v:j for j,v in enumerate(unassigned)}
    residual=[4*signs[i] for i in unassigned]
    free=[]
    for i,slot_i,j,slot_j in edges:
        if i in fixed and j in fixed:
            if (signs[i]*fixed[i][slot_i]+
                signs[j]*fixed[j][slot_j])%5:
                return 0
        elif i in fixed:
            x=(signs[i]*fixed[i][slot_i])%5
            residual[local[j]]+=x
        elif j in fixed:
            x=(-signs[j]*fixed[j][slot_j])%5
            residual[local[i]]-=x
        else:
            free.append((local[i],local[j]))
    n=len(unassigned)
    m=len(free)
    answer=0
    powers=tuple(5**i for i in range(m+1))
    for mask in range(1<<m):
        parent=list(range(n))
        def root(x):
            while parent[x]!=x:
                parent[x]=parent[parent[x]]
                x=parent[x]
            return x
        for k,(i,j) in enumerate(free):
            if mask & (1<<k):
                ri=root(i);rj=root(j)
                if ri!=rj:parent[rj]=ri
        comp=[0]*n
        roots=set()
        for i,b in enumerate(residual):
            r=root(i);roots.add(r)
            comp[r]+=b
        if any(comp[r]%5 for r in roots):
            continue
        exponent=mask.bit_count()-n+len(roots)
        if exponent<0:
            raise AssertionError("negative unsigned original GF5 nullity")
        answer+=(-1 if (m-mask.bit_count())%2 else 1)*powers[exponent]
    if answer<0 or answer>51**n:
        raise AssertionError("original signed affine GF5 completion count invalid")
    return answer


def _motif_conditional_mass(motif,assignment):
    fixed=tuple((i,assignment[id_]) for i,id_ in enumerate(motif["ids"])
                if id_ in assignment)
    count=sum(_completion_count(motif["edges"],plus,fixed) for plus in SIGNS)
    return Fraction(count,51**(6-len(fixed)))


def unconditional_original_mass(family):
    """Known independent 90-case GF5 theorem input, rechecked exactly."""
    totals=Counter(m["kind"] for m in family["motifs"])
    numerator=sum(WEIGHTS[k]*n for k,n in totals.items())
    if numerator<0:raise AssertionError("negative independent expectation")
    return Fraction(numerator,DENOM)


def direct_original_signed_events(family,assignment):
    """A DIFFERENT physical-coordinate loop, no IE or conditional oracle."""
    if any(id_ not in assignment for m in family["motifs"]
           for id_ in m["ids"]):
        raise ValueError("assignment must cover every chosen ORIGINAL source flag")
    found=[]
    for m in family["motifs"]:
        for plus in SIGNS:
            signs=tuple(1 if i in plus else -1 for i in range(6))
            if all((signs[i]*assignment[m["ids"][i]][slot_i]+
                    signs[j]*assignment[m["ids"][j]][slot_j])%5==0
                   for i,slot_i,j,slot_j in m["edges"]):
                found.append((m["ids"],tuple(sorted(plus))))
    return tuple(found)


def deterministic_gf5_assign(family, *,max_motifs=24):
    """Method of exact conditional expectations; NO motif independence.

    All 51 palettes are tried for each original source ID, greedily.
    Proof: averaging candidate conditional expectations is exactly the
    old expectation because one original ID palette was uniform on 51.
    Thus the best candidate never increases the global expected risk.
    After all variables are fixed the exact expected risk is an
    INTEGER equal to the directly inspected number of signed events.
    """
    motifs=family["motifs"]
    if type(max_motifs) is not int or max_motifs<0:
        raise ValueError("nonnegative tractability bound required")
    if len(motifs)>max_motifs:
        raise ValueError("referee per-run exact IE motif budget exceeded")
    impacts=defaultdict(list)
    for k,m in enumerate(motifs):
        for id_ in m["ids"]:impacts[id_].append(k)
    ordered=tuple(sorted(impacts,key=lambda i:(-len(impacts[i]),i)))
    baseline=unconditional_original_mass(family)
    for m in motifs:
        actual=_motif_conditional_mass(m,{})
        if actual!=Fraction(WEIGHTS[m["kind"]],DENOM):
            raise AssertionError(("independent original GF5 signed census mismatch",
                                  m["kind"],actual))
    assignment={}
    risk=baseline
    trace=[]
    for id_ in ordered:
        old_part=sum((_motif_conditional_mass(motifs[k],assignment)
                      for k in impacts[id_]),Fraction())
        candidates=[]
        for palette in PALETTES:
            assignment[id_]=palette
            local=sum((_motif_conditional_mass(motifs[k],assignment)
                       for k in impacts[id_]),Fraction())
            candidates.append((local,palette))
        del assignment[id_]
        if sum((r for r,_ in candidates),Fraction())!=51*old_part:
            raise AssertionError("51 original palettes do not partition exact completions")
        local,palette=min(candidates)
        assignment[id_]=palette
        risk=risk-old_part+local
        if risk<0 or risk>baseline:
            raise AssertionError("exact derandomization conditional risk went up")
        trace.append((id_,str(risk)))
    observed=direct_original_signed_events(family,assignment)
    if risk!=len(observed):
        raise AssertionError(("independent direct physical GF5 events disagree",
                              str(risk),len(observed)))
    if baseline<1 and observed:
        raise AssertionError("fractional first-moment condition failed")
    return {
        "selected_ORIGINAL_sixset_count":len(motifs),
        "selected_original_ids":ordered,
        "class_population":dict(sorted(Counter(m["kind"] for m in motifs).items())),
        "baseline_exact_expected_signed_events":baseline,
        "deterministic_original_palette_assignment":dict(sorted(assignment.items())),
        "conditioned_exact_signed_event_count":risk,
        "direct_checked_original_signed_events":observed,
        "assigned_every_original_ID_only_once":len(assignment)==len(ordered),
        "zero_selected_motif_signed_events":len(observed)==0,
        "stepwise_exact_risk_trace":tuple(trace),
        "not_all_original_sixsets_covered_unless_family_is_exhaustive":True,
    }


def worst_case_zero_certificate_size():
    """Independent 51^6 denominator; all motifs in 2 proved classes."""
    return (DENOM-1)//max(WEIGHTS.values())


if __name__=="__main__":
    from hyp105_gf5_original_sixid_flow_referee import planted_original_bb_overlap
    import json
    w=planted_original_bb_overlap(1)
    family=prepare_original_family(1,w["f"],w["g"],[w["ids"]])
    r=deterministic_gf5_assign(family)
    print(json.dumps({
        "true_original_s":family["s"],
        "w32_actual_source_sixset_ids":w["ids"],
        "selected_motifs":r["class_population"],
        "exact_initial_expected_signed_events":str(r["baseline_exact_expected_signed_events"]),
        "realized_signed_events":int(r["conditioned_exact_signed_event_count"]),
        "source_palette_assignment":r["deterministic_original_palette_assignment"],
        "uniform_all_class_motif_first_moment_threshold":worst_case_zero_certificate_size(),
        "scope":"SELECTED source sixsets ONLY, not a proof of all-source deterministic ASET"
    },indent=2))
