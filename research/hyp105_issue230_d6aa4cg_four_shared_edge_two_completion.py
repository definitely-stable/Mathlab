"""HYP-105 AA4-CG: TRUE original W(3,2^h) eightpacket crossfamily 4-edge dichotomy.

Families A=(0,1,2,3,4,5) and B=(0,1,2,3,6,7) use the
SAME complete global 256-state LINE swap cube. A and B source sixflag
Q have 4 shared original LINE-factor choices and 2 exclusive choices.

Two different physical 2factors sharing 4 exact edges can coexist only:
(1) 6 original shared physical vertices; exclusive two-edge matchings
    are disjoint alternate pairings of 4 degree-one terminals (C4 switch);
(2) 5 shared-edge vertices; each exclusive pair joins the same two
    degree-one terminals to a DIFFERENT sixth degree-two vertex
    (cherry center / physical-vertex replacement).
These are exact iff classifications when BOTH masks are physical 2factors.
The second case is possible for true W34 (a=14), impossible for W32 a=6.

An all-h conditional statement, NOT proof of universal positive S.
"""
from collections import Counter
from itertools import combinations

from hyp105_issue230_d6aa4bh_local_seven_compensation import _original_source
from hyp105_issue230_d6aa4bq_all_seven_reverse_switching import (
    apply_disjoint_factor_swaps, validate_disjoint_factor_swaps,
)
from hyp105_issue230_d6aa4by_original_independent_2factor_kernel import (
    physical_right_is_six_vertex_two_regular,
)
from hyp105_g5e2b3e1b0_seven_signature import (
    classify_seven_prechecked,
)
from hyp105_issue230_projection import fixture

EIGHT=8
CUBE=1<<EIGHT
FAMILIES={"A":(0,1,2,3,4,5),"B":(0,1,2,3,6,7)}
SHARED_MASK=(1<<4)-1


def _canon(edges):
    out=[]
    for edge in edges:
        if (len(edge)!=2 or any(type(v) is not int or v<0 for v in edge)
                or edge[0]==edge[1]):
            raise ValueError("simple unordered nonloop nonnegative physical edge required")
        out.append(tuple(sorted(edge)))
    if len(out)!=len(set(out)):
        raise ValueError("all physical edges must be distinct")
    return tuple(out)


def _regular6(edges):
    d=Counter(v for e in edges for v in e)
    return len(edges)==6 and len(d)==6 and all(v==2 for v in d.values())


def classify_four_common_completion(shared, a_edges, b_edges):
    """Classify actual 4+2+2 DISTINCT physical edges, no GF5 oracle.

    Returns 'four_cycle_switch', 'vertex_replacement', or 'not_both'.
    Raises for repeated edges/invalid input. Both-live cases are complete.
    """
    if len(shared)!=4 or len(a_edges)!=2 or len(b_edges)!=2:
        raise ValueError("exactly four common and two exclusive edges per family")
    edges=_canon(tuple(shared)+tuple(a_edges)+tuple(b_edges))
    F,A,B=edges[:4],edges[4:6],edges[6:8]
    if not (_regular6(F+A) and _regular6(F+B)):
        return "not_both"
    vertices={v for e in F for v in e}
    degree=Counter(v for e in F for v in e)
    if len(vertices)==6:
        terminals={v for v in vertices if degree[v]==1}
        if len(terminals)!=4 or sorted(degree.values())!=[1,1,1,1,2,2]:
            raise AssertionError("valid shared-six-vertex four-edge deficit must have four endpoints")
        if any(set(e)-terminals for e in A+B):
            raise AssertionError("two completions must match four fixed terminals")
        for pair in (A,B):
            if {v for e in pair for v in e}!=terminals:
                raise AssertionError("valid completion must perfectly match the four terminals")
        # Two different perfect matchings on four points have union C4.
        cycle=Counter(v for e in A+B for v in e)
        if len(cycle)!=4 or set(cycle.values())!={2}:
            raise AssertionError("four exclusive edges must form an alternating C4")
        return "four_cycle_switch"
    if len(vertices)==5:
        terminals={v for v in vertices if degree[v]==1}
        if len(terminals)!=2 or sorted(degree.values())!=[1,1,2,2,2]:
            raise AssertionError("valid shared-five-vertex degree deficit must have two endpoints")
        centers=[]
        for pair in (A,B):
            outside={v for e in pair for v in e}-vertices
            if len(outside)!=1:
                raise AssertionError("new physical vertex must be common center of 2-edge cherry")
            center=next(iter(outside))
            if {frozenset(e) for e in pair}!={frozenset((center,u)) for u in terminals}:
                raise AssertionError("new center connects exactly both terminal vertices")
            centers.append(center)
        if centers[0]==centers[1]:
            raise AssertionError("global injection forbids same two completion edges")
        return "vertex_replacement"
    raise AssertionError("four common edges in 2factor cannot have other vertex count")


def physical_overlapping_eight_masks(original_g,packets):
    """Two genuinely different sixpacket families from ONE ORIGINAL g."""
    g=tuple(_canon(original_g))
    pairs=validate_disjoint_factor_swaps(len(g),packets)
    if len(pairs)!=EIGHT:
        raise ValueError("eight disjoint original LINE image packets required")
    images=tuple((g[u],g[v]) for u,v in pairs)
    masks={}
    for fam,subset in FAMILIES.items():
        masks[fam]=tuple(int(_regular6(tuple(
            images[j][(x>>j)&1] for j in subset
        ))) for x in range(CUBE))
    pattern=Counter()
    for x in range(CUBE):
        if masks["A"][x] and masks["B"][x]:
            shared=tuple(images[i][(x>>i)&1] for i in range(4))
            A=tuple(images[i][(x>>i)&1] for i in (4,5))
            B=tuple(images[i][(x>>i)&1] for i in (6,7))
            c=classify_four_common_completion(shared,A,B)
            if c not in ("four_cycle_switch","vertex_replacement"):
                raise AssertionError("two physical original 2factors violated exact dichotomy")
            pattern[c]+=1
    return {"A":masks["A"],"B":masks["B"],"edges":images,
            "A_active":sum(masks["A"]),"B_active":sum(masks["B"]),
            "same_orientation_joint_types":dict(pattern)}


def _lift(t,fam):
    if fam not in FAMILIES or type(t) is not int or not 0<=t<64:
        raise ValueError("six original LINE orientation bits needed")
    return sum((1<<index) for i,index in enumerate(FAMILIES[fam]) if t>>i&1)


def mixed_8cube_gram(masks):
    """Two separate 64x64 source orientation families; one 256-map g cube."""
    if any(len(masks[k])!=CUBE for k in FAMILIES):
        raise ValueError("256 complete physical global maps required")
    shifted={fam:tuple(
         sum((1<<x) for x in range(CUBE)
             if masks[fam][x^_lift(t,fam)])
         for t in range(64))
         for fam in FAMILIES}
    J=tuple(tuple((shifted["A"][t]&shifted["B"][u]).bit_count()
                  for u in range(64)) for t in range(64))
    # A same-four-prefix positive entry is allowed, unlike #606.
    # But every state counted by such an entry must be a valid
    # C4 switch OR cherry center replacement.
    return {"J":J,"shifted_A":shifted["A"],"shifted_B":shifted["B"],
            "same_four_positive_pairs":sum(
                J[t][u]>0 for t in range(64) for u in range(64)
                if (t&SHARED_MASK)==(u&SHARED_MASK)),
            "total_positive_orientation_pairs":sum(
                v>0 for row in J for v in row)}


def _pick_real_W34_original_sixflags(model):
    """Deterministically choose two TRUE original six-ID sets, 4 common flags.

    Point f forms actual physical left C6. Each original incidence
    belongs to real symplectic W34 and all 8 chosen LINE IDs distinct.
    """
    s,V,a,inc,f,g,point,line=_original_source(model)
    if (s,V,a)!=(4,85,14):
        raise ValueError("true ORIGINAL symplectic W34, not synthetic K14")
    physical=((0,1),(1,2),(2,3),(3,4),(4,5),(0,5))
    point_ids=tuple({edge:i for i,edge in enumerate(f)}[e] for e in physical)
    by_point=[[ ] for _ in range(V)]
    for idx,(p,l) in enumerate(inc):by_point[p].append((l,idx))
    for p in point_ids:
        by_point[p].sort()
    chosen=[]
    def dfs(i,used):
        if i==8:return tuple(chosen)
        p=point_ids[i if i<6 else i-2]
        for line_id,flag in by_point[p]:
            if line_id in used:continue
            chosen.append((line_id,flag))
            found=dfs(i+1,used|{line_id})
            if found is not None:return found
            chosen.pop()
        return None
    # Pick four shared incidences, two A-exclusive and two B-exclusive
    # with same two POINT source factors but different original LINE IDs.
    found=dfs(0,set())
    if found is None:raise AssertionError("no real 8 LINE-distinct sixflag completion")
    line_ids=tuple(line for line,_ in found)
    flags=tuple(flag for _,flag in found)
    QA=flags[:6]
    QB=flags[:4]+flags[6:]
    if len(set(QA))!=6 or len(set(QB))!=6:
        raise AssertionError("six distinct original incidence IDs required")
    if len(set(line_ids))!=8 or len(set(line_ids[:6]))!=6:
        raise AssertionError("eight original globally different LINE IDs required")
    if {inc[i][0] for i in QA}!={inc[i][0] for i in QB}:
        raise AssertionError("same physical f left six-coordinate candidate set")
    return {"QA":QA,"QB":QB,"point_ids":point_ids,"line_ids":line_ids}


def genuine_W34_eightpacket_witness(case):
    """TRUE W(3,4) source and a complete physically legal correlated f,g.

    All 85 original LINE source images are assigned injectively to
    85 edges of K14. The 8 REAL original Q LINE factors occupy exactly
    the requested 4+2+2 physical edges at global x=0.
    """
    if case not in ("four_cycle_switch","vertex_replacement"):
        raise ValueError("an explicitly realized exact dichotomy case required")
    model=fixture(2,"lex")
    s,V,a,inc,f,g,_,_=_original_source(model)
    witness=_pick_real_W34_original_sixflags(model)
    phys_A=((0,5),(2,3)) if case=="four_cycle_switch" else ((4,5),(0,5))
    phys_B=((0,3),(2,5)) if case=="four_cycle_switch" else ((4,6),(0,6))
    shared=((0,1),(1,2),(3,4),(4,5)) if case=="four_cycle_switch" else (
        (0,1),(1,2),(2,3),(3,4))
    target=tuple(tuple(sorted(e)) for e in shared+phys_A+phys_B)
    if classify_four_common_completion(shared,phys_A,phys_B)!=case:
        raise AssertionError("constructive physical original witness is not required case")
    if len(set(target))!=8 or not set(target).issubset(set(g)):
        raise AssertionError("original g physical alphabet lacks witness edges")
    requested=dict(zip(witness["line_ids"],target))
    rest=iter(e for e in g if e not in set(target))
    newg=tuple(requested[l] if l in requested else next(rest) for l in range(V))
    if len(set(newg))!=V:
        raise AssertionError("whole original LINE image injection was not preserved")
    free=iter(i for i in range(V) if i not in set(witness["line_ids"]))
    packets=tuple((l,next(free)) for l in witness["line_ids"])
    if len(set(z for p in packets for z in p))!=16:
        raise AssertionError("eight packet images not source-disjoint")
    actual=dict(model,right_labels=newg)
    return actual,packets,witness


def genuine_W34_original_pair_eight_cube(case):
    """Finite original Q_A,Q_B, 256 COMPLETE original maps, true GF5 only.

    Uses actual source incidence flags, not per-Q image redraw.
    """
    model,packets,witness=genuine_W34_eightpacket_witness(case)
    s,V,a,inc,f,g,_,_=_original_source(model)
    masks=physical_overlapping_eight_masks(g,packets)
    gram=mixed_8cube_gram(masks)
    QA,QB=witness["QA"],witness["QB"]
    if not (masks["A"][0] and masks["B"][0]):
        raise AssertionError("requested both-live original all-h physical witness failed")
    pair_direct=Counter()
    actual={"A":[],"B":[]}
    for x in range(CUBE):
        assignment=apply_disjoint_factor_swaps(
            g,packets,tuple(i for i in range(EIGHT) if (x>>i)&1))
        if len(set(assignment))!=V:
            raise AssertionError("every full original LINE map must remain globally injected")
        A=physical_right_is_six_vertex_two_regular(QA,inc,assignment)
        B=physical_right_is_six_vertex_two_regular(QB,inc,assignment)
        if int(A)!=masks["A"][x] or int(B)!=masks["B"][x]:
            raise AssertionError("independent genuine six-source-Q physical check != 8cube")
        clsA=classify_seven_prechecked(QA,f,assignment,inc)
        clsB=classify_seven_prechecked(QB,f,assignment,inc)
        if clsA is not None and not A or clsB is not None and not B:
            raise AssertionError("historical accepted GF5 motif violates actual physical support")
        actual["A"].append(clsA);actual["B"].append(clsB)
        if A and B:
            shared=tuple(assignment[witness["line_ids"][i]] for i in range(4))
            extraA=tuple(assignment[witness["line_ids"][i]] for i in (4,5))
            extraB=tuple(assignment[witness["line_ids"][i]] for i in (6,7))
            classification=classify_four_common_completion(shared,extraA,extraB)
            pair_direct[classification]+=1
    if sum(pair_direct.values())!=gram["J"][0][0]:
        raise AssertionError("independently classified TRUE original Q pair disagree on mixed Gram")
    if set(pair_direct)!={case}:
        raise AssertionError("chosen true original pair changed its physical dichotomy type")
    return {
        "case":case,"source_W34_original_s":s,"original_LINE_factor_count":V,
        "genuine_original_distinct_QA_QB":(QA,QB),
        "packets":packets,"physical_8cube_A_active":masks["A_active"],
        "physical_8cube_B_active":masks["B_active"],
        "true_original_both_physical_joint":gram["J"][0][0],
        "independent_true_original_joint_classification":dict(pair_direct),
        "historical_GF5_original_center_QA":actual["A"][0],
        "historical_GF5_original_center_QB":actual["B"][0],
        "GF5_joint_historical_positive_maps":sum(
            a is not None and b is not None for a,b in zip(actual["A"],actual["B"])),
        "root_230":"OPEN_WITH_FORMAL_BLOCKER",
    }
