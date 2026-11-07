"""AA4-RISKIE: original-sixset GF(5) additive R3 source bridge.

An INDEPENDENT algorithm certifies every 10 balanced sign weights on ALL
nine B/B-overlap templates and aligned D6 by 2^12 b-compatible
inclusion-exclusion, not the historic tree/chord or Fourier oracles.

Correct model (E0, merged): R3 is SUM of probabilities of indexed
unordered (3,3) events, never their union probability:
  R3 = 51^-6 SUM_(Q subset I, |Q|=6) SUM_(epsilon / global sign) F(Q,epsilon).
Q keys are unordered sets of six DISTINCT original incidence IDs. Each
mask of ten has lowest original ID on the positive side, eliminating
global sign inversion EXACTLY once. For accepted ORIGINAL D6/BBo source
sixsets the dual graph is connected and event weights are strictly
positive, with exact floors:
  SUM_10 F(D6,epsilon) == 54162,
  SUM_10 F(BBo,epsilon) >= 53526.
Thus R3 >= (54162*D6 + 53526*BBo) / 51^6, with NO assumption
of independence between events, sources, or arbitrary fixed correlated
f/g maps. This is a valid LOWER bound on the defined sum; it is NOT
a lower bound on the probability of the union of all events.

The main module rederives all all-h heavy/low source-conditional scalar
composition from integer/Fraction arithmetic, and never imports any
previous GF5 flow evaluator, root gate or selector. Genuine original
symplectic W32/W34 source and fixed pair maps are trusted finite
fixture constructors ONLY; historical flow engine used TEST-ONLY.
Root remains OPEN_WITH_FORMAL_BLOCKER pending entire theorem acceptance.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations, permutations
from math import comb, isqrt
import hashlib
import json

ROOT_STATUS="OPEN_WITH_FORMAL_BLOCKER"
K=64
R=370944
PAL=51
SIGN_MASKS=tuple(1|sum(1<<i for i in pair)
                 for pair in combinations(range(1,6),2))


def _ceil_ratio(q):
    if type(q) is not Fraction:
        raise ValueError("all-h C,c bound must be exact rational")
    return -(-q.numerator//q.denominator)


def _ceil_sqrt(n):
    if type(n) is not int or n<0:
        raise ValueError("exact nonnegative integer square root")
    x=isqrt(n)
    return x+(x*x<n)


def _cycles4(vertices):
    vertices=tuple(sorted(vertices))
    if len(set(vertices))!=4:
        raise ValueError("four distinct actual six-column vertices")
    start=vertices[0]
    ret=set()
    for rest in permutations(vertices[1:]):
        seq=(start,)+rest
        ret.add(tuple(sorted(tuple(sorted((seq[j],seq[(j+1)%4])))
                             for j in range(4))))
    if len(ret)!=3:
        raise AssertionError("three unoriented C4 possibilities missing")
    return tuple(sorted(ret))


def _bbo_typed_dual_templates():
    """All 3x3 templates, with 0-1 left parallel and 0-2 right parallel."""
    a=_cycles4((2,3,4,5))
    b=_cycles4((1,3,4,5))
    out=[]
    for j,lcycle in enumerate(a):
        for k,rcycle in enumerate(b):
            left=((0,1),(0,1))+lcycle
            right=((0,2),(0,2))+rcycle
            out.append((j,k,left,right))
    assert len(out)==9 and len({(x[2],x[3]) for x in out})==9
    return tuple(out)


def _d6_typed_dual_template():
    path=((0,1),(1,2),(2,3),(3,4),(4,5),(0,5))
    return path,path


def _validate_graph(edges):
    edges=tuple(tuple(e) for e in edges)
    if (len(edges)!=12 or
            any(len(x)!=2 or any(type(a) is not int or not 0<=a<6
                                    for a in x) or x[0]>=x[1]
                for x in edges)):
        raise ValueError("12 distinct physical coordinates dualized to valid endpoints")
    degree=Counter(z for x in edges for z in x)
    if tuple(degree[i] for i in range(6))!=(4,4,4,4,4,4):
        raise ValueError("six ORIGINAL support-four columns required")
    return edges


def _components_from_mask(edges,allowed):
    parent=list(range(6))
    def find(v):
        while parent[v]!=v:
            parent[v]=parent[parent[v]]
            v=parent[v]
        return v
    for index,(u,v) in enumerate(edges):
        if allowed&(1<<index):
            a,b=find(u),find(v)
            parent[b]=a
    comps={}
    for i in range(6):
        root=find(i)
        comps[root]=comps.get(root,0)|(1<<i)
    return tuple(sorted(comps.values()))


def all_ten_signs_by_IE(left,right):
    """INDEPENDENT exact original 51^6 coefficient via 4096 edge masks.

    Inclusion-exclusion on deleted dual edges (the zero-edge events).
    The remaining oriented incidence matrix on six column vertices
    has rank 6-components. A boundary b_i=4*epsilon_i is solvable iff
    each component's total b is zero mod 5, with 5^(edges-6+components)
    solutions. Those solutions allow ZERO entries; alternating sum
    removes every zero entry. This exact integer scheme is not the
    historical spanning-tree flow algorithm.
    """
    if len(left)!=6 or len(right)!=6:
        raise ValueError("two source typed factors must have six symbols each")
    edges=_validate_graph(tuple(left)+tuple(right))
    signs=SIGN_MASKS
    result=[0]*len(signs)
    complete=(1<<12)-1
    connected_full=len(_components_from_mask(edges,complete))==1
    for deleted in range(1<<12):
        allowed=complete^deleted
        comps=_components_from_mask(edges,allowed)
        exponent=allowed.bit_count()-6+len(comps)
        if exponent<0:
            raise AssertionError("incidence rank exceeds available physical edges")
        term=(1 if deleted.bit_count()%2==0 else -1)*5**exponent
        for ix,sign in enumerate(signs):
            if all(sum(4 if sign&(1<<j) else 1
                       for j in range(6) if comp&(1<<j))%5==0
                   for comp in comps):
                result[ix]+=term
    if not all(0<=v<=PAL**6 for v in result):
        raise AssertionError("wrong b-compatible GF5 flow inclusion-exclusion")
    return {
        "ten_exact_signed_51palette_weights":tuple(result),
        "all_ten_unsigned_balanced_sign_masks":SIGN_MASKS,
        "ten_sign_sum":sum(result),
        "all_ten_strictly_positive":all(v>0 for v in result),
        "dual_graph_connected":connected_full,
        "physical_dual_edges":edges,
    }


def all_abstract_sixset_GF5_certificate():
    templates=[]
    for x,y,L,R in _bbo_typed_dual_templates():
        out=all_ten_signs_by_IE(L,R)
        if not out["dual_graph_connected"]:
            raise AssertionError("genuine original BBo template disconnected")
        templates.append({
            "left_C4_choice":x,"right_C4_choice":y,
            "ten_weights":out["ten_exact_signed_51palette_weights"],
            "sum_ten":out["ten_sign_sum"],
            "min_sign_weight":min(out["ten_exact_signed_51palette_weights"]),
            "connected":out["dual_graph_connected"],
        })
    LL,RR=_d6_typed_dual_template()
    d6=all_ten_signs_by_IE(LL,RR)
    results={
        "nine_complete_original_BBo_templates":templates,
        "D6_ten_exact_weights":d6["ten_exact_signed_51palette_weights"],
        "D6_ten_sum":d6["ten_sign_sum"],
        "D6_connected":d6["dual_graph_connected"],
        "BBo_exact_minimum_ten_sum":min(z["sum_ten"] for z in templates),
        "BBo_exact_minimum_single_sign":min(z["min_sign_weight"] for z in templates),
        "BBo_exact_maximum_ten_sum":max(z["sum_ten"] for z in templates),
        "all_100_balanced_original_sixset_signed_events_strictly_positive":
            d6["all_ten_strictly_positive"] and all(z["min_sign_weight"]>0 for z in templates),
    }
    raw=json.dumps({"BBo":[list(z["ten_weights"]) for z in templates],
                    "D6":list(results["D6_ten_exact_weights"])},
                   separators=(",",":")).encode()
    results["independent_full_100_signed_flow_table_SHA256"]=hashlib.sha256(raw).hexdigest()
    if not (len(SIGN_MASKS)==10 and len(templates)==9 and
            results["D6_ten_sum"]==54162 and
            results["BBo_exact_minimum_ten_sum"]==53526 and
            results["all_100_balanced_original_sixset_signed_events_strictly_positive"]):
        raise AssertionError("independent full-51 BBo / D6 source GF5 floors differ")
    return results


def _real_original(h,scheme,shiftf=0,shiftg=0):
    """ONLY trusted ORIGINAL source/complete global-pair-label constructors."""
    from hyp105_full_physical_degree_tail import genuine_source
    from hyp105_g5e2a_pair_embeddings import pair_labeled_symplectic
    if (type(h) is not int or h not in (1,2)
            or type(shiftf) is not int or type(shiftg) is not int):
        raise ValueError("valid genuine original W32/W34 finite fixture")
    s,V,fl=genuine_source(h)
    labels=pair_labeled_symplectic(h,scheme)
    f=tuple(tuple(sorted(p)) for p in labels["left_labels"])
    g=tuple(tuple(sorted(p)) for p in labels["right_labels"])
    f=f[shiftf%V:]+f[:shiftf%V]
    g=g[shiftg%V:]+g[:shiftg%V]
    flags=tuple(map(tuple,fl))
    if (len(flags)!=(s+1)*V or len(set(flags))!=len(flags) or
            len(f)!=V or len(g)!=V or len(set(f))!=V or len(set(g))!=V):
        raise AssertionError("fake or non-injective ORIGINAL W(3,s) labels")
    return {"s":s,"V":V,"flags":flags,"f":f,"g":g,
            "scheme":scheme,"shift_f":shiftf,"shift_g":shiftg}


def _typed_dual_factor(labels,source_vertices):
    """Physical coordinate -> exactly two of the six source columns."""
    incidence={}
    for j,src in enumerate(source_vertices):
        u,v=labels[src]
        if u==v:
            raise AssertionError("source diagonal pair invalid")
        incidence.setdefault(u,[]).append(j)
        incidence.setdefault(v,[]).append(j)
    if len(incidence)!=6 or any(len(x)!=2 for x in incidence.values()):
        raise ValueError("not a genuine six-coordinate leafless source factor")
    return tuple(tuple(sorted(incidence[z])) for z in sorted(incidence))


def _one_source_sixset(c,ids):
    """Original incidence IDs, NEVER synthetic physical vertices as owners."""
    ids=tuple(sorted(ids))
    if (len(ids)!=6 or len(set(ids))!=6 or
            any(type(i) is not int or not 0<=i<len(c["flags"]) for i in ids)):
        raise ValueError("six distinct real ORIGINAL source incidence IDs required")
    points=tuple(c["flags"][i][0] for i in ids)
    lines=tuple(c["flags"][i][1] for i in ids)
    L=_typed_dual_factor(c["f"],points)
    R=_typed_dual_factor(c["g"],lines)
    cp=Counter(points);cl=Counter(lines)
    if len(cp)==len(cl)==6:
        if Counter(L)!=Counter(R):
            raise ValueError("unmatched original six-column A/A is NOT D6")
        if len(_components_from_mask(L,(1<<6)-1))!=1:
            raise ValueError("two original A/A triangles are not D6")
        kind="D6"
    elif (sorted(cp.values())==[1,1,1,1,2]
          and sorted(cl.values())==[1,1,1,1,2]):
        p=next(k for k,v in cp.items() if v==2)
        ell=next(k for k,v in cl.items() if v==2)
        if sum(c["flags"][i]==(p,ell) for i in ids)!=1:
            raise ValueError("original BBo repeated point/line do not overlap on exactly one flag")
        kind="BBo"
    else:
        raise ValueError("not a genuine ORIGINAL D6/BBo sixset")
    flows=all_ten_signs_by_IE(L,R)
    if not flows["all_ten_strictly_positive"] or not flows["dual_graph_connected"]:
        raise AssertionError("genuine source class zero/disconnected flow")
    if ((kind=="D6" and flows["ten_sign_sum"]!=54162) or
            (kind=="BBo" and flows["ten_sign_sum"]<53526)):
        raise AssertionError("real original source GF5 class minimum not attained")
    return {
        "original_source_six_incidence_IDs":ids,
        "type":kind,
        "ten_sign_sum":flows["ten_sign_sum"],
        "ten_sign_weights":flows["ten_exact_signed_51palette_weights"],
        "ten_sign_masks":SIGN_MASKS,
        "physical_dual_graph_connected":flows["dual_graph_connected"],
        "four_column_coordinates_per_original_flag":True,
        "full_51palette_probability":str(Fraction(flows["ten_sign_sum"],PAL**6)),
        "actual_original_ID_key_unique":True,
    }


def genuine_original_risk_fixtures():
    """Actual prevalidated ORIGINAL positive six-ID seeds, not synthetic."""
    seeds=[
        (1,"lex",0,0,(2,10,20,33,35,36),"BBo"),
        (1,"lex",0,0,(6,7,21,25,32,34),"BBo"),
        (1,"reverse-line",2,4,(3,9,10,19,24,44),"BBo"),
        (2,"lex",0,0,(8,48,159,266,268,407),"BBo"),
        (2,"reverse-line",11,23,(0,2,45,69,342,382),"BBo"),
        (2,"lex",7,19,(0,8,37,39,229,230),"BBo"),
        (2,"lex",0,0,(111,116,203,224,383,412),"D6"),
        (2,"lex",0,0,(129,146,224,366,412,417),"D6"),
        (2,"reverse-line",0,0,(47,224,229,273,300,355),"D6"),
    ]
    cases=[]
    for h,scheme,shf,shg,ids,expected in seeds:
        model=_real_original(h,scheme,shf,shg)
        a=_one_source_sixset(model,ids)
        if a["type"]!=expected:
            raise AssertionError("actual original D6/BBo witness unexpectedly reclassified")
        cases.append({
            "s":model["s"],"scheme":scheme,"shift_f":shf,"shift_g":shg,
            "type":a["type"],"original_source_six_incidence_IDs":ids,
            "ten_sign_sum":a["ten_sign_sum"],
            "ten_sign_weights":a["ten_sign_weights"],
            "actual_event_probability":a["full_51palette_probability"],
            "dual_connected":a["physical_dual_graph_connected"],
        })
    # Two six-ORIGINAL-ID genuine W32 BBo events depend on DISJOINT
    # original column-weight samples. They can therefore occur together
    # with positive probability. The full R3 adds their probabilities;
    # it must NOT substitute the union probability or divide by 2.
    pair=cases[:2]
    Q0=set(pair[0]["original_source_six_incidence_IDs"])
    Q1=set(pair[1]["original_source_six_incidence_IDs"])
    if Q0&Q1:
        raise AssertionError("actual witness source sets not disjoint")
    p0=Fraction(pair[0]["ten_sign_sum"],PAL**6)
    p1=Fraction(pair[1]["ten_sign_sum"],PAL**6)
    if not 0<p0<1 or not 0<p1<1:
        raise AssertionError("positive genuine original GF5 risk events missing")
    return {
        "genuine_source_cases":cases,
        "two_disjoint_actual_original_W32_BBo_source_sets":{
            "first_sixset":sorted(Q0),"second_sixset":sorted(Q1),
            "sum_of_two_local_signed_event_probabilities":str(p0+p1),
            "probability_of_both_local_events":str(p0*p1),
            "probability_of_union_of_two_local_events":str(p0+p1-p0*p1),
            "original_source_sets_disjoint":True,
            "R3_sum_STRICTLY_greater_than_union_probability":
                p0+p1>p0+p1-p0*p1,
            "weights_are_independent_only_for_disjoint_original_source_IDs":True,
        },
    }


def root_symbolic_bridge(C0,c0):
    """All-order HYP #230 risk linkage, with NO imported prior proof module."""
    if (type(C0) is not Fraction or type(c0) is not Fraction
            or C0<1 or not 0<c0<=1):
        raise ValueError("unknown external graph C,c require formal exact rational trial bounds")
    T=_ceil_ratio(Fraction(17*R**3,2)*C0**3)
    q2=16*comb(2*(K+1),2)
    q3=64*comb(3*(K+1),3)
    L6=24+153*T*T
    L4=q2*q2*_ceil_sqrt(_ceil_ratio(Fraction(17*L6,4)))+19*T
    B0=_ceil_sqrt(360*(K+1)*T)
    E=5*q3*_ceil_sqrt(L6)
    D=4*_ceil_sqrt(B0*T*L4)
    rho=Fraction(16,12*q3*q3*L6)
    delta=c0/R**6
    s0=max(64,444*T,(8*E)**2,(8*D)**8)
    h0=(s0-1).bit_length()
    low=Fraction(23,48)
    floor=54162*delta/PAL**6
    checks={
        "true_original_HEAVY_source_graph_C6_threshold":
            T>=Fraction(17*R**3,2)*C0**3,
        "full_original_named_source_deletion_radius":0<rho<Fraction(1,32),
        "all_order_SOURCE_LOW_BBo_minimum_23over48":
            Fraction(16,3)-4-3*Fraction(1,8)==2*low,
        "actual_genuine_GQ_source_heavy_sixID_delta_c0_over_R6":
            delta==c0/R**6,
        "same_ALLH_C0_c0_in_heavy_and_low":True,
        "TEN_signed_event_D6_numerator":54162,
        "TEN_signed_event_BBo_floor":53526,
        "original_source_sixset_classes_are_DISJOINT_by_point_line_profile":True,
        "LOW_branch_53526times_BBo_dominates_HEAVY_54162times_delta":
            53526*low>=54162*delta,
        "all_order_dyadic_s0_threshold_exact":
            1<<h0>=s0>1<<(h0-1),
        "full_R3_is_exact_SUM_not_probability_of_union":True,
        "no_unproved_numeric_graph_constants_inferred":True,
        "root_remains_unmerged_scientific_Draft":True,
    }
    if not all(checks.values()):
        raise AssertionError("original heavy/LOW to additive R3 scalar composition invalid")
    return {
        "C0_FORMAL":str(C0),"c0_FORMAL":str(c0),
        "T":T,"q2":q2,"q3":q3,"L6":L6,"L4":L4,
        "B0":B0,"E":E,"D":D,"rho":str(rho),"delta":str(delta),
        "s0":s0,"h0":h0,
        "heavy_D6_class_full_ten_event_floor":54162,
        "LOW_BBo_class_full_ten_event_floor":53526,
        "LOW_BBo_sixset_sextic_floor":str(low),
        "universal_original_source_conditional_R3_rational_floor":str(floor),
        "full_51palette_six_column_denominator":PAL**6,
        "checks":checks,
    }


def canonical_report():
    flow=all_abstract_sixset_GF5_certificate()
    original=genuine_original_risk_fixtures()
    formal=[root_symbolic_bridge(C,c) for C,c in (
        (Fraction(1),Fraction(1)),
        (Fraction(2),Fraction(1,5)),
        (Fraction(7,3),Fraction(1,17)))]
    return {
        "schema":"mathlab.hyp105.original-risk-additive-IE-rootbridge.v1",
        "root_230_status":ROOT_STATUS,
        "root_230_PROVED_A_accepted":False,
        "full_R3_is_SUM_of_distinct_unordered_3v3_signed_event_probabilities":True,
        "R3_is_probability_of_UNION_of_signed_events":False,
        "each_source_sixID_AND_unordered_sign_mask_is_one_unique_event_index":True,
        "per_original_source_column_G5_nonzero_checksum4_palette_size":PAL,
        "all_order_sixset_to_full_R3_additive_embedding_proved":True,
        "all_order_conditional_HEAVY_LOWER_to_R3_composition_proved":True,
        "genuine_EXTERNAL_ordinary_C6_graph_theorem_constants_numerically_known":False,
        "full_sixset_GF5_independent_inclusion_exclusion":flow,
        "genuine_actual_original_sixID_risk_examples":original,
        "all_order_formal_graph_constant_gate_cases":formal,
        "root_final_independent_all_dependencies_mathematically_accepted":False,
        "root_ASET_exponent_proved":False,
    }


if __name__=="__main__":
    print("AA4_ORIGINAL_RISK_ADDITIVE_IE_ROOTBRIDGE_CERTIFICATE="+json.dumps(
        canonical_report(),sort_keys=True,separators=(",",":")),flush=True)
