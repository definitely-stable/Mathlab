"""HYP-105 E1-K3-F2: mixed C4-diagonal operator and chord-to-motif ledger.

Exact finite-graph identities, applied only to ONE whole coherent legal
W(3,s) physical point/line labeling. This is a conditional diagnostic,
NOT a uniform Omega(s^6) seven-family obstruction or an infinite
counterexample.

Define W_uv = binom(|N(u) intersect N(v)|, 2) for MIXED physical
coordinate pairs u != v and 0 otherwise. Then for any vertex set H:
  Q(H) = sum_{u<v in H} W_uv = (1/2) 1_H^T W 1_H
  2 Q(H) + cut_W(H, H^c) = sum_{u in H} rho_u.
A row-strength upper and an exact-integer Frobenius/Cauchy upper can
be used without replacing all W_uv with their global maximum.

For every pair of C4s sharing exactly one edge and no further vertex,
their symmetric difference is a C6 with an antipodal chord. Count
proper (D6), distinct ORIGINAL six-column but improper (R3 only),
and repeated-original-column witnesses separately. Every C6 has at
most three antipodal chords, and the original six-column multiplicity
of ALL cycles is a separate K2 constraint. No seven-family conclusion
can be inferred from the improper witnesses alone.
"""
from collections import Counter, defaultdict
from itertools import combinations
from math import comb, isqrt
import json

from hyp105_g5e2b3e1k1_kikuchi_c6 import gq_pair_model, kikuchi_graph
from hyp105_g5e2b3e1k2_cycle_pattern_weights import four_cycles
from hyp105_g5e2b3e1k3_local_collisions import star_degree_tensor
from hyp105_g5e2b3e1k3e_weighted_codegrees import mixed_weighted_profile


def mixed_pair(u, v, a):
    return u//a != v//a and u%a != v%a


def weighted_diagonal_operator(model, *, max_pairs=40_000,
                               max_c4=40_000):
    """Construct the symmetric, diagonal-free weighted MIXED C4 operator.

    Fast construction by common neighbors. An independent oracle based
    on actual C4 edge sets and their opposite pairs lives in the tests.
    """
    if type(max_pairs) is not int or max_pairs < 0:
        raise ValueError("max_pairs must be a nonnegative integer")
    if type(max_c4) is not int or max_c4 < 0:
        raise ValueError("max_c4 must be a nonnegative integer")
    a = model["a"]
    g = kikuchi_graph(model)
    n = len(g)
    if n != a*a:
        raise ValueError("invalid Kikuchi vertex layout")
    if n*(n-1)//2 > max_pairs:
        raise RuntimeError("all unordered-pair budget exceeded")
    degrees = star_degree_tensor(model)
    if degrees != tuple(map(len,g)):
        raise AssertionError("original GQ star transport mismatch")
    rows = [dict() for _ in range(n)]
    energy = 0
    m2 = 0
    for u in range(n):
        for v in range(u+1,n):
            if not mixed_pair(u,v,a):
                continue
            common = len(g[u]&g[v])
            w = comb(common,2) if common>=2 else 0
            if not w:
                continue
            rows[u][v] = w
            rows[v][u] = w
            m2 += w
            energy += w*w
    c4 = len(four_cycles(g))
    if c4>max_c4:
        raise RuntimeError("C4 witness budget exceeded")
    if m2>2*c4:
        raise AssertionError("mixed diagonals cannot exceed 2 per C4")
    strengths = tuple(sum(row.values()) for row in rows)
    if sum(strengths)!=2*m2:
        raise AssertionError("operator handshake identity failed")
    return {"graph":g, "a":a, "rows":rows,"degree":degrees,
            "strength":strengths, "M2mixed":m2, "E2mixed":energy,
            "C4":c4}


def _universal_pair_bound(w, H):
    """Exact rational/square-root-free integer Frobenius cut upper."""
    h = len(H)
    count = h*(h-1)//2
    energy = w["E2mixed"]
    # Q(H)^2 <= C(h,2) * sum_{u<v mixed} W_uv^2.
    # As Q(H) is nonnegative integral, floor sqrt is valid.
    return isqrt(count*energy)


def weighted_cut_profile(w, H, *, max_selected=40_000):
    """Exact binary quadratic form, boundary identity, row/Frobenius caps."""
    if type(max_selected) is not int or max_selected < 0:
        raise ValueError("selected budget must be nonnegative integer")
    selected=frozenset(H)
    n=len(w["rows"])
    if len(selected)>max_selected:
        raise RuntimeError("selected-set budget exceeded")
    if any(type(u) is not int or u<0 or u>=n for u in selected):
        raise ValueError("invalid selected vertex")
    mass = sum(weight for u in selected for v,weight in w["rows"][u].items()
               if v in selected)//2
    boundary = sum(weight for u in selected
                   for v,weight in w["rows"][u].items() if v not in selected)
    row_sum=sum(w["strength"][u] for u in selected)
    if row_sum!=2*mass+boundary:
        raise AssertionError("weighted cut and row strength identity failed")
    maxweight=max((weight for row in w["rows"] for weight in row.values()),
                  default=0)
    h=len(selected)
    pair_cap=h*(h-1)//2*maxweight
    row_cap=row_sum//2
    frob_cap=_universal_pair_bound(w,selected)
    global_cap=w["M2mixed"]
    best=min(pair_cap,row_cap,frob_cap,global_cap)
    if mass>best:
        raise AssertionError("conditional weighted operator cap violated")
    return {
        "high_star_vertices":h,
        "Q_exact":mass,
        "weighted_boundary":boundary,
        "row_strength_sum":row_sum,
        "row_strength_upper":row_cap,
        "Frobenius_integer_upper":frob_cap,
        "max_weight_pair_upper":pair_cap,
        "global_M2_upper":global_cap,
        "operator_upper":best,
    }


def operator_tail_certificate(model, *, max_pairs=40_000,
                              max_c4=40_000):
    """Integer operator tail ledger, compared to K3-E's EXACT star upper.

    Recomputes h_k directly from the independent original GQ star
    transport. The sum of true Q_k^star is an upper for Bmixed but is
    map-dependent, exactly K3-E's source-star upper. The new operator
    cap uses row strengths and Frobenius concentration but cannot
    improve the known EXACT Qstar count on a fixed map.
    """
    w=weighted_diagonal_operator(model,max_pairs=max_pairs,max_c4=max_c4)
    k3e=mixed_weighted_profile(model,max_pairs=max_pairs,max_c4=max_c4)
    cmax=k3e["Cmax_girth8"]
    total_Q=0
    total_cap=0
    useful_row=useful_frob=0
    rows=[]
    for k in range(3,cmax+1):
        H=[u for u,d in enumerate(w["degree"]) if d>=k]
        val=weighted_cut_profile(w,H)
        if val["Q_exact"]!=int(k3e["source_star_upper_tail"].get(str(k),0)):
            raise AssertionError("operator quadratic form vs K3-E star tail")
        total_Q+=val["Q_exact"]
        total_cap+=val["operator_upper"]
        useful_row+=int(val["row_strength_upper"]<val["max_weight_pair_upper"])
        useful_frob+=int(val["Frobenius_integer_upper"]<val["max_weight_pair_upper"])
        rows.append({"threshold":k,**val})
    if total_Q!=k3e["B_upper_source_star"]:
        raise AssertionError("all k source-tail layer cake mismatch")
    if not k3e["B_mixed"]<=total_Q<=total_cap:
        raise AssertionError("operator bounds vs exact book mass")
    return {
        "B_mixed":k3e["B_mixed"],
        "M2_mixed":w["M2mixed"], "C4":w["C4"],
        "energy_sum_mixed_W_squared":w["E2mixed"],
        "B_upper_K3E_exact_source_star":total_Q,
        "B_upper_F2_operator":total_cap,
        "operator_row_better_than_pair_cap_layers":useful_row,
        "operator_Frobenius_better_than_pair_cap_layers":useful_frob,
        "all_h_Omega_s6_proved":False,
        "thresholds":rows,
    }


def original_column_lut(model):
    """One incidence label for each Kikuchi edge, never remap per motif."""
    a=model["a"]
    lut={}
    for index,(p,l) in enumerate(model["incidences"]):
        x,xx=model["left_labels"][p]
        y,yy=model["right_labels"][l]
        e1=frozenset((x*a+y,xx*a+yy))
        e2=frozenset((x*a+yy,xx*a+y))
        for e in (e1,e2):
            if e in lut and lut[e]!=index:
                raise AssertionError("not a coherent globally injective physical map")
            lut[e]=index
    return lut


def chorded_motif_extraction(model, *, max_c4=40_000,
                             max_incident_pairs=300_000):
    """Exact *conditional* chorded C6 -> proper D6/distinct-six census.

    Independent edge-set square enumeration drives overlap join; no
    unbounded GQ theorem is inferred. Explicit decomposition:
      H = Hproper + Himproper_distinct + Hrepeated;
    proper D6 >= ceil(Hproper/3), and distinct original six-column
    chorded C6 >= ceil((Hproper+Himproper_distinct)/3).
    Important: the second floor is NOT a floor for seven-family S.
    """
    if type(max_c4) is not int or max_c4<0 or (
        type(max_incident_pairs) is not int or max_incident_pairs<0
    ):
        raise ValueError("C4 and square-pair budgets must be nonnegative")
    graph=kikuchi_graph(model)
    squares=list(four_cycles(graph))
    if len(squares)>max_c4:
        raise RuntimeError("C4 budget exceeded")
    by_edge=defaultdict(list)
    verts=[]
    for i,q in enumerate(squares):
        verts.append(frozenset().union(*q))
        for e in q:
            by_edge[e].append(i)
    incidences=sum(len(qs)*(len(qs)-1)//2 for qs in by_edge.values())
    if incidences>max_incident_pairs:
        raise RuntimeError("shared C4 edge-pair budget exceeded")
    pairs=set()
    for qs in by_edge.values():
        pairs.update(combinations(sorted(qs),2))
    lookup=original_column_lut(model)
    a=model["a"]
    classes=Counter()
    unique={"proper":set(),"distinct_improper":set(),"repeated":set()}
    multiplicity=Counter()
    for i,j in pairs:
        q1,q2=squares[i],squares[j]
        common=q1&q2
        if len(common)!=1 or len(verts[i]&verts[j])!=2:
            continue
        cycle=frozenset(q1^q2)
        points=frozenset().union(*cycle)
        if len(cycle)!=6 or len(points)!=6:
            raise AssertionError("not a six-cycle")
        deg=Counter(z for e in cycle for z in e)
        if set(deg.values())!={2}:
            raise AssertionError("chorded symmetric difference not 2-regular")
        original=[lookup[e] for e in cycle]
        distinct=len(set(original))==6
        proper=(len({z//a for z in points})==6 and
                len({z%a for z in points})==6)
        if proper and not distinct:
            raise AssertionError("proper D6 cannot repeat original incidence")
        kind=("proper" if proper else
              "distinct_improper" if distinct else "repeated")
        classes[kind]+=1
        unique[kind].add(cycle)
        multiplicity[cycle]+=1
    if max(multiplicity.values(),default=0)>3:
        raise AssertionError("at most three antipodal chords per C6")
    H=sum(classes.values())
    if H!=sum(multiplicity.values()):
        raise AssertionError("witness counts failed")
    proper=classes["proper"]
    distinct=proper+classes["distinct_improper"]
    ceil3=lambda v:(v+2)//3
    return {
        "C4":len(squares),
        "H_chorded_total":H,
        "H_proper":proper,
        "H_distinct_improper":classes["distinct_improper"],
        "H_repeated_original_columns":classes["repeated"],
        "distinct_column_H_total":distinct,
        "D6_floor_by_chord_multiplicity":ceil3(proper),
        "six_distinct_column_C6_floor":ceil3(distinct),
        "unique_chorded_proper_C6":len(unique["proper"]),
        "unique_chorded_distinct_improper_C6":len(unique["distinct_improper"]),
        "unique_chorded_repeated_C6":len(unique["repeated"]),
        "max_antipodal_chord_multiplicity":max(multiplicity.values(),default=0),
        "branch_A_or_B_proved":False,
        "full_R3_is_not_seven_family_S":True,
    }


def report():
    result={
      "slice":"HYP-105-B3.2-E1-K3-F2",
      "status":"RESTRICTED_THEOREM_C_WEIGHTED_OPERATOR_AND_EXACT_CHORD_EXTRACTION",
      "uniform_seven_family_floor_proved":False,
      "models":{},
    }
    for h,scheme,seed in ((1,"lex",None),(1,"reverse-line",None),
                          (2,"lex",None),(2,"random",20261011)):
        m=gq_pair_model(h,scheme,seed)
        a=operator_tail_certificate(m)
        b=chorded_motif_extraction(m)
        a.pop("thresholds")
        result["models"]["s%s-%s%s"%(m["s"],scheme,
                 "-"+str(seed) if seed is not None else "")]={"operator":a,"motif":b}
    return result


if __name__=="__main__":
    print(json.dumps(report(),indent=2,sort_keys=True))
